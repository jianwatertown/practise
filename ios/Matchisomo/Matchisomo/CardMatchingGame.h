//
//  CardMatchingGame.h
//  Matchisomo
//
//  Created by Jian Wang on 8/1/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#ifndef Matchisomo_CardMatchingGame_h
#define Matchisomo_CardMatchingGame_h


#endif


#import <Foundation/Foundation.h>
#import "Deck.h"


@interface CardMatchingGame: NSObject

// designated initializer
- (instancetype) initWithCardCount: (NSUInteger) count usingDeck: (Deck *)deck;

@property (nonatomic, readonly) NSInteger score; // readonly is means no setter



- (void) chooseCardAtIndex: (NSUInteger) index;
- (Card *) cardAtIndex: (NSUInteger) index;

@end

