from Deck import Deck
from Hand import Hand
import unittest


class Player:

    def __init__(self, id_, money, hand=None):
        self.id = id_  # id determines order of play
        self.money = money
        self.hand = hand  # defaults to None

    def __repr__(self):
        return 'Player(id=%r, money=%r, hand=%r)' % (self.id, self.money, self.hand)

    def deal_hand(self, hand):
        self.hand = hand
        # TODO: show the player their hand, when they press enter, move on & print 50 newline characters

    '''
	Force a player's blind and return T/F if they can/cannot make the full blind
	'''

    def force_blind(self, type_, pot, blind_money):
        if self.money >= blind_money:
            self.money -= blind_money
            pot.add_bet(self, blind_money)
            print(' - Player', self.id, 'posts a',
                  type_, 'blind of', blind_money)
            return True
        else:  # player does not have enough money to post full blind, goes out
            print(' - Player', self.id, 'cannot post a full blind of',
                  blind_money, 'and goes out')
            return False

    def bid(self, pot, bid):
        # TODO: if the player doesn't have enough money to bid, print a warning. Otherwise, add the bet to the pot.

    def action(self, curr_round):
        amount_to_call = curr_round.pot.amount_to_call(self)
        print('Player', self.id, 'the amount you need to call is', amount_to_call)

        # check if player cannot make call
        if self.money < amount_to_call:
            print('Player', self.id, 'goes out with', self.money, 'left')
            # remove player from round and game
            curr_round.add_folded_player(self, True)

        res = input('Would you like to fold, call, or raise? (f/c/r) ')
        if res == 'c':
            action = Call(self, curr_round, amount_to_call)
        elif res == 'r':
            raise_by = input('How much would you like to raise? ')
            action = Raise(self, curr_round, amount_to_call, int(raise_by))
        else:  # assume 'f' for now
            action = Fold(self, curr_round)

        if action.is_valid():
            action.perform()
            print('')
        else:  # get a new action
            print('Action is not valid')
            self.action(curr_round)

    def add_winnings(self, winnings):
        # TODO: add winnings to the current player's money

        ######################################################################


class Action(object):
    def __init__(self, player, _round):
        self.player = player
        self.round = _round

    def is_valid():
        raise NotImplementedError("Can not validate Action")

    def perform():
        raise NotImplementedError("Can not validate Action")


class Fold(Action):
    def __init__(self, player, _round):
        super().__init__(player, _round)

    def is_valid(self):
        return self.player in self.round.player_order

    def perform(self):
        print(' - Player', self.player.id, 'folds')
        self.round.add_folded_player(self.player)
        self.round.pot.remove_player(self.player)


class Call(Action):
    def __init__(self, player, _round, amount_to_call):
        super().__init__(player, _round)
        self.amount_to_call = amount_to_call

    def is_valid(self):
        return self.player.money >= self.amount_to_call

    def perform(self):
        print(' - Player', self.player.id,
              'calls with a bet of', self.amount_to_call)
        self.player.bid(self.round.pot, self.amount_to_call)


class Raise(Action):
    def __init__(self, player, _round, amount_to_call, raise_by):
        super().__init__(player, _round)
        self.amount_to_call = amount_to_call
        self.raise_by = raise_by

    def is_valid(self):
        return self.player.money >= self.raise_by

    def perform(self):
        total_bid = self.amount_to_call + self.raise_by
        print(' - Player', self.player.id, 'raises',
              self.raise_by, 'for a total bid of', total_bid)
        self.player.bid(self.round.pot, total_bid)


#####################################################################

class MyTest(unittest.TestCase):

        # TODO write tests for some of the methods!


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
