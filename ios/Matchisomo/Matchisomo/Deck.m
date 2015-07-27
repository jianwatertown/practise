//
//  Deck.m
//  Matchisomo
//
//  Created by Jian Wang on 7/25/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Deck.h"



// internal data structures
@interface Deck()
@property  (strong,nonatomic)   NSMutableArray *cards; // of Card
@end

@implementation Deck


-(NSMutableArray *) cards{
    // initlize an array
    // lazy initlization, do not to put into ini
    if(!_cards) _cards  = [[NSMutableArray alloc] init];
    return _cards;
}


- (void) addCard: (Card*)card atTop:(BOOL)atTop{
    if(atTop){
        [self.cards insertObject:card atIndex:0];
    }else{
        [self.cards addObject:card];
    }
}

- (void) addCard:(Card *)card{
    [self addCard:card atTop:NO];
}

- (Card*) drawRandomCard{
    Card *randomCard = nil;
    
    if([self.cards count])
    {
        unsigned index = arc4random() % [self.cards count];
        randomCard = self.cards[index];
        [self.cards removeObjectAtIndex:index]; // actuall change the size
    }
    return randomCard;
}

@end