//
//  Card.h
//  Matchisomo
//
//  Created by Jian Wang on 7/25/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#ifndef Matchisomo_Card_h
#define Matchisomo_Card_h


#endif

@interface Card : NSObject

@property (strong, nonatomic) NSString *content;

// getter=isChosen is rename
@property (nonatomic, getter=isChosen) BOOL chosen;
@property (nonatomic, getter=isMatched) BOOL matched;


// return_type funct_name: type_you_return variable
-(int) match:(NSArray *) otherCards;
@end