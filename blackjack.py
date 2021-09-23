from deck import Deck
from player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.show()

        if p_status == 1:
            print("You got Blackjack! Congrats!")
            if d_status == 1:
                print("You and the dealer got Blackjack! It's a tie!")
            return 1

        cmd = ""
        while cmd != "Stand":
            bust = 0
            cmd = input("Hit or Stand? ")

            if cmd == "Hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("Player busted. Good Game!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("Tough, the Dealer got Blackjack! Better luck next time!")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. LETS GOOOOO")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print("It's a Tie. Better luck next time!")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer wins. Good Game!")
        elif self.dealer.check_score() < self.player.check_score():
            print("You win. Congratulations!")

b = Blackjack()
b.play()