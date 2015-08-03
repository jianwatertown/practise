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
#import "CardMatchingGame.h"
#import "Card.h"

@interface ViewController ()
@property (nonatomic) int scoreLabel;
@property (strong, nonatomic) Deck *deck;
@property (nonatomic, strong) CardMatchingGame *game;
@property (strong, nonatomic) IBOutletCollection(UIButton) NSArray *cardButtons;
@end

@implementation ViewController


-(CardMatchingGame *) game{ // notice this lazy pattern again
if(!_game)
    _game = [[CardMatchingGame alloc] initWithCardCount:[self.cardButtons count] usingDeck:[self createDeck]];
    return _game;
}

-(Deck *)createDeck{
    return [[PlayingCardDeck alloc] init];
}



- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void) setScoreLabel:(int)score
{
    _scoreLabel = score;
    self.flipsLable.text = [NSString stringWithFormat:@"Score: %d", _scoreLabel];
}

- (IBAction)touchCardButton:(UIButton *)sender
{
    int cardIndex = [self.cardButtons indexOfObject:sender]; // location of the sending button, "sender" is only 1 of them
    [self.game chooseCardAtIndex:cardIndex];
    [self updateUI];
    [self setScoreLabel: [self.game score]];
}

-(void) updateUI{
    for (UIButton *cardButton in self.cardButtons){
        int cardIndex = [self.cardButtons indexOfObject:cardButton];
        Card *card = [self.game cardAtIndex:cardIndex];
        [cardButton setFont:[UIFont fontWithName:@".HelveticaNeueInterface-Regular" size:32]];
        [cardButton setTitle: [self titleForCard: card] forState:UIControlStateNormal];
        [cardButton setBackgroundImage:[self backgroundImageForCard: card]
                              forState:UIControlStateNormal];
        cardButton.enabled = !card.isMatched; // only enable card when it's not matched
    }
}

- (NSString *) titleForCard: (Card *) card{
    return card.isChosen? card.content: @"";
}

- (UIImage *) backgroundImageForCard: (Card *) card
{
    return [UIImage imageNamed: card.isChosen? @"whiteRound" : @"cardback"];

}

@end
