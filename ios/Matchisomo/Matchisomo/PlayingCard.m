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
- (NSString *) content
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

-(int) match:(NSArray *) otherCards
{
    int score=0; // local variable starts with 0
    
    if([otherCards count]==1){
        PlayingCard *card = [otherCards firstObject];
        
    // we only use . when setting properties
    // getter() isEqualToString getter()
    if([card.content isEqualToString:self.content]){
        score =100;
    }
    else if (card.rank == self.rank ){
        score = 20;
    }
    
    else if ([card.suit isEqualToString:self.suit]){
        score = 5;
    }
    }
    return score;
}

@end