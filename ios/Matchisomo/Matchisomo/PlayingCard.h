//
//  PlayingCard.h
//  Matchisomo
//
//  Created by Jian Wang on 7/26/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#ifndef Matchisomo_PlayingCard_h
#define Matchisomo_PlayingCard_h


#endif

#import <Foundation/Foundation.h>
#import "Card.h"

@interface PlayingCard: Card

@property (strong, nonatomic) NSString *suit;

// NSUInteger is almost unsigned interger
// 32bits on older iphone
@property (nonatomic) NSUInteger rank;

+ (NSArray *) validSuits;
+ (NSUInteger) maxRank;

@end