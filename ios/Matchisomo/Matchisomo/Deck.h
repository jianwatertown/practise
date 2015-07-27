//
//  Deck.h
//  Matchisomo
//
//  Created by Jian Wang on 7/25/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#ifndef Matchisomo_Deck_h
#define Matchisomo_Deck_h


#endif


#import <Foundation/Foundation.h>
#import "Card.h"

@interface Deck : NSObject


// function name "add card, at top"
// multiple-argument function
-(void) addCard: (Card*) card atTop:(BOOL) atTop;
- (void) addCard:(Card *)card;
-(Card*) drawRandomCard;

@end