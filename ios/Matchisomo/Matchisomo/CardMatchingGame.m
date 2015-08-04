//
//  CardMatchingGame.m
//  Matchisomo
//
//  Created by Jian Wang on 8/1/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import "CardMatchingGame.h"

@interface CardMatchingGame()
@property (nonatomic, readwrite) NSInteger score; // re-defining
@property (nonatomic, strong) NSMutableArray *cards; // of Cards
@end

@implementation CardMatchingGame


static const int MISMATCH_PENALTY = 4;
static const int MATCH_BONUS = 4;
static const int COST_TO_CHOOSE = 2;

- (NSMutableArray *) cards
{
    // the only reason to re-write is for lazy-initilization
    if (!_cards)
        _cards = [[NSMutableArray alloc] init];
    return _cards;
}


- (instancetype) initWithCardCount:(NSUInteger)count usingDeck:(Deck *)deck
{
    self = [super init];
    
    if (self){
        for (int i=0;i<count;i++){
            Card *card = [deck drawRandomCard];
            if(card){
                [self.cards addObject:card]; // self.cards[i] = card; this work too
            }
            else{
                self = nil; // self-destructive
                break;
            }
        }
        
        
    }
    return self;
}

- (Card *) cardAtIndex: (NSUInteger) index
{
    return (index < [self.cards count])? self.cards[index] : nil;
}

- (void) chooseCardAtIndex:(NSUInteger)index{

    
    Card *card = [self cardAtIndex:index];
    
    if(!card.isMatched){
        
        // toggle this field
        if(card.isChosen){
            card.chosen = NO;
        }else{
        // match against another card
            for (Card *otherCard in self.cards){
                if (otherCard.isChosen && !otherCard.isMatched){
                    int matchScore = [card match:@[otherCard]];  // create 1 array and put 1 card in it
                    NSLog(@"getting score = %d",matchScore);
                    if(matchScore){
                        self.score +=matchScore * MATCH_BONUS;
                        card.matched = YES;
                        otherCard.matched = YES;
                    }
                    else{
                        otherCard.chosen = NO;
                        self.score -= MISMATCH_PENALTY;
                    
                    }
                    break;
                }
            }
            self.score -= COST_TO_CHOOSE;
            card.chosen = YES;
        }
    }
}

@end