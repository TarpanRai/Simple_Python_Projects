import random
import time

# Create deck
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4

# Define the value of the card
card_value = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}


# Function to calculate the value of the hand
def hand_value(hand):
    total_value = sum(card_value[i] for i in hand)
    # Check for aces and adjust the total if necessary
    aces = hand.count("A")
    while aces > 0 and total_value > 21:
        total_value -= 10
        aces -= 1
    return total_value


# Function to display the current cards after being dealt
def game_state(player_hand, dealer_hand, player_total):
    print(f"Dealer's hand: [{dealer_hand[0]}, *]")
    print(f"Your hand: {player_hand} ({player_total} total)")


# Game
def game():
    # Shuffle the deck(list) first
    random.shuffle(deck)

    # Deal the card to the player and the dealer
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Value of the card in players hand
    player_total = hand_value(player_hand)
    while True:
        game_state(player_hand, dealer_hand, player_total)
        if player_total == 21:
            print("Blackjack! You win!")
            break
        elif player_total > 21:
            print("You lose!")
            break
        else:
            # Player input hit or stand
            action = input("Hit or Stand?:").lower()
            # If hit, it will pop a card from the deck
            if action == "hit":
                player_hand.append(deck.pop())
                player_total = hand_value(player_hand)
            elif action == "stand":
                print("Dealer's turn... Good luck!")
                # Added delay to add suspense
                time.sleep(1)
                # Value of card in dealers hand
                dealer_total = hand_value(dealer_hand)
                # Dealer will keep hitting until 17
                while dealer_total < 17:
                    dealer_hand.append(deck.pop())
                    dealer_total = hand_value(dealer_hand)
                print("Your hand:", player_hand, "(", player_total, "total)")
                print("Dealer's hand:", dealer_hand, "(", dealer_total, "total)")
                if dealer_total > 21:
                    print("Dealer bust! You win!")
                elif dealer_total > player_total:
                    print("Dealer wins.")
                elif dealer_total < player_total:
                    print("You win!")
                else:
                    print("Push (tie).")
                break

    # Ask the player if they want to play again
    while True:
        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again == "y":
            game()
            break
        elif play_again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    game()
