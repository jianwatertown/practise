//
//  ViewController.h
//  Matchisomo
//
//  Created by Jian Wang on 7/12/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "PlayingCardDeck.h"
#import "Deck.h"

@interface ViewController : UIViewController
// we want this to be weak because it is hold by the button
@property (weak, nonatomic) IBOutlet UILabel *flipsLable;


@end

