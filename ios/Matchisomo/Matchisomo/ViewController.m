//
//  ViewController.m
//  Matchisomo
//
//  Created by Jian Wang on 7/12/15.
//  Copyright (c) 2015 Jian Game House. All rights reserved.
//

#import "ViewController.h"
#import "PlayingCardDeck.h"
#import "PlayingCard.h"
#import "Card.h"

@interface ViewController ()

@end

@implementation ViewController


- (void)viewDidLoad {
    [super viewDidLoad];
    [self setDeck:[[PlayingCardDeck alloc] init]];
    NSLog(@"we have got a deck!!!");
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void) setFlipCount:(int)flipCount
{
    _flipCount = flipCount;
    self.flipsLable.text = [NSString stringWithFormat:@"Flip: %d", self.flipCount];
    NSLog(@"flipCount=%d",self.flipCount);
}

- (IBAction)touchCardButton:(UIButton *)sender {

    Card *card = [self.deck drawRandomCard];
    NSLog(@"new card content=%@",card.content);
    [sender setTitle: card.content forState: UIControlStateNormal];
    self.flipCount++;
}



@end
