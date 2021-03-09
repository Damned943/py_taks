# if you use this way:
# _from random import shuffle_
# then shuffle is made like:
# _shuffle(list_to_shuffle)_

# if you use this way:
# _import random_
# then shuffle is made like:
# _random.shuffle(list_to_shuffle)_

# the book used 1st option
# but I don't know does it save memory or not
# but it seems more good looking anyway


from random import shuffle


class Cards:
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return self.values[self.value] + " of " \
            + self.suits[self.suit]


class Deck():
    def __init__(self):
        self.cards = []
        for v in range(2, 15):
            for s in range(4):
                self.cards.append(Cards(v, s))
        shuffle(self.cards)

    def rn_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player():
    def __init__(self, name):
        self.wins = 0
        # self.card = None  #This variable is not used further
        # and I dunno why it was introduced in the book
        self.name = name


class Game():
    def __init__(self):
        pl1nm = 'Andrew'  # input('input player 1 name: ')
        pl2nm = 'Bob'  # input('input player 2 name: ')
        self.a_deck = Deck()
        self.pl1 = Player(pl1nm)
        self.pl2 = Player(pl2nm)

    def cur_winner(self, plnm):
        winner = '{} wins this round'
        winner = winner.format(plnm)
        print(winner)

    def cur_move(self, pl1nm, pl1c, pl2nm, pl2c):
        txt = '\n{} picks [{}] and {} picks [{}]'
        txt = txt.format(pl1nm, pl1c, pl2nm, pl2c)
        print(txt)

    def final_winner(self):
        if self.pl1.wins > self.pl2.wins:
            winner = self.pl1.name
        elif self.pl1.wins == self.pl2.wins:
            winner = 'Friendship'
        else:
            winner = self.pl2.name
        print('\n{} wins the whole game!\n'.format(winner))

    def play(self):
        print("\n\n\nLet the game begin!\n")
        cur_cards = self.a_deck.cards
        while len(cur_cards) >= 2:
            # msg = '\ninput X to quit ar anything(or nothing) for the next round: \n'
            # usr_inp = input(msg)
            # if usr_inp.upper() == 'X':
            #     break
            p1c = self.a_deck.rn_card()
            p2c = self.a_deck.rn_card()
            p1n = self.pl1.name
            p2n = self.pl2.name
            self.cur_move(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.cur_winner(self.pl1.name)
                self.pl1.wins += 1
            else:
                self.cur_winner(self.pl2.name)
                self.pl2.wins += 1
            print('current state [{}[{}:{}]{}]'.format(
                p1n, self.pl1.wins, self.pl2.wins, p2n
            ))
        self.final_winner()


a_game = Game()
a_game.play()
