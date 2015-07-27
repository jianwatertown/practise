//
//  PlayingCardDeck.m
//  Matchisomo
//
//  Created by Jian Wang on 7/26/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "PlayingCardDeck.h"
#import "PlayingCard.h"

@implementation PlayingCardDeck: Deck


// only do "alloc init" once
// send a message to a class and get a class of the same type
- (instancetype) init
{
    // wired, assigning something to yourself
    self = [self init];
    
    // in case, parent class is not initialized
    if(self){
        // over the suits
        for (NSString *suit in [PlayingCard validSuits]){
            // over the rank
            for (NSUInteger rank = 1; rank <= [PlayingCard maxRank]; rank++){
                PlayingCard *card = [[PlayingCard alloc] init];
                card.rank = rank;
                card.suit = suit;
                [self addCard:card];
            }
        }
    }
    return self;
}

@end