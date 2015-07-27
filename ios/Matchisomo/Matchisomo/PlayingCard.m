//
//  PlayingCard.m
//  Matchisomo
//
//  Created by Jian Wang on 7/26/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Card.h"
#import "PlayingCard.h"

@implementation PlayingCard : Card



@synthesize suit = _suit; // becase we provided setter AND getter

// "@"some_string" makes a sring object
- (NSString *) contents
{
    // @ creates an array
    return [[PlayingCard rankStrings][self.rank] stringByAppendingString:self.suit];
}


// class method (static)
+ (NSArray *) validSuits
{
    return @[@"♣️",@"♥️",@"♠️",@"♦️"];
}

- (void) setSuit:(NSString *)suit
{
    if ([[PlayingCard validSuits] containsObject:suit]){
        _suit = suit;
    }
}

// override getter
-(NSString *) suit{
    return _suit ? _suit: @"?";
}

+ (NSArray *) rankStrings{
    return @[@"?",@"A",@"2",@"3",@"3",@"4",@"5",@"6",@"7",@"8",@"9",@"10",@"J",@"Q",@"K"];
}

+ (NSUInteger) maxRank {
    return [[self rankStrings] count]-1;
}


// override setter
- (void) setRank:(NSUInteger)rank
{
    if (rank <= [PlayingCard maxRank])
    {
        _rank = rank;
    }
}

@end