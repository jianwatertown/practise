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
}

- (IBAction)touchCardButton:(UIButton *)sender {
    [sender setBackgroundImage:[ UIImage imageNamed:@"whiteRound"] forState:UIControlStateNormal];
    Card *card = [self.deck drawRandomCard];
    if(card){
        [sender setTitle: card.content forState: UIControlStateNormal];
        self.flipCount++;
    }
    else{
        [sender setTitle: @"" forState: UIControlStateNormal];
        [sender setBackgroundImage:[ UIImage imageNamed:@"cardback"] forState:UIControlStateNormal];
    }
}


- (Deck *) deck{
    if(!_deck) {
        _deck = [self createDeck];
    }
    return _deck;
}


-(Deck *)createDeck{
    return [[PlayingCardDeck alloc] init];
}

@end
