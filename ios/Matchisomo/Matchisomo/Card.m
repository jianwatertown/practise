
//
//  Card.m
//  Matchisomo
//
//  Created by Jian Wang on 7/25/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Card.h"  // import header file


// private declartions inside this class
@interface Card()

@end


@implementation Card

-(int) match: (NSArray *) otherCards;{
    int score=0;
    
    // always class name + * card
    // use "." for no-argument funciton call
    for(Card *card in otherCards){
        if([card.content isEqualToString:self.content]){
            score =1;
        }
    }
    return score;

}

@end
