from collections import defaultdict
import unittest

'''
Pot keeps track of each player's bids and community cards
'''


class Pot:

    def __init__(self):
        # pot starts with
        self.money = defaultdict(lambda: 0)
        self.folded_money = 0  # any money belonging to folded players
        self.cards = list()

    def add_bet(self, player, money):
        # TODO: at the player's entry in the money dictionary, add money
        pass

    def add_cards(self, cards):
        # for each card in cards, add the card to self.cards
        pass

    def balanced(self):
         # TODO:Return true if all the player's money in the pot is the same
        pass

    def amount_to_call(self, player):
		'''
        Return amount needed to call for a specific player
        '''
        highest_bid = max(value for value in self.money.values())
        return highest_bid - self.money[player]

    '''
	Remove folded player, adding their money to self.folded_money
	'''

    def remove_player(self, player):
        player_money = self.money[player]  # works??
        self.folded_money += player_money
        del self.money[player]

    def reward_winner(self, player):
        winnings = sum(self.money.values()) + self.folded_money
        player.add_winnings(winnings)


class MyTest(unittest.TestCase):

        # TODO write tests for the methods you wrote!


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
