import random
import time

# Define the cards as dictionaries
cards = [
    {"Name": "Diablo", "Health": 100, "Attack": 90, "Defense": 60},
    {"Name": "Medusa", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Jester", "Health": 120, "Attack": 60, "Defense": 90},
    {"Name": "Troll", "Health": 150, "Attack": 40, "Defense": 94},
    {"Name": "Specter", "Health": 100, "Attack": 70, "Defense": 70},
    {"Name": "Mist", "Health": 100, "Attack": 75, "Defense": 65},
    {"Name": "Savage", "Health": 100, "Attack": 90, "Defense": 50},
    {"Name": "Marauder", "Health": 100, "Attack": 85, "Defense": 50},
    {"Name": "Wimp", "Health": 110, "Attack": 40, "Defense": 85},
    {"Name": "Sorcerer", "Health": 100, "Attack": 70, "Defense": 55}
]


# Function to create a random deck of 5 cards
def create_deck():
    return random.sample(cards, 5)


# Function to display card details
def display_card(card):
    print(f"Name: {card['Name']}")
    print(f"Health: {card['Health']}")
    print(f"Attack: {card['Attack']}")
    print(f"Defense: {max(0, card['Defense'])}")  # Display 0 if defense is negative


# Function to get valid card index from player
def get_player_card_index(player_deck):
    for i in range(len(player_deck)):
        display_card(player_deck[i])
        print(f"{i + 1}. {player_deck[i]['Name']}")
    while True:
        try:
            chosen_card_index = int(input("Choose a card to fight (enter card index): ")) - 1
            if 0 <= chosen_card_index < len(player_deck):
                return chosen_card_index
            else:
                print("Invalid index, please try again.")
        except ValueError:
            print("Please enter a valid number.")


# Function to simulate a round of the game
def play_round(player_deck, opponent_deck):
    # Display player's deck
    print("Your deck:")
    for card in player_deck:
        display_card(card)
    print("\n")

    # Draw a random card for the opponent
    opponent_card = random.choice(opponent_deck)
    print("Opponent's card:")
    display_card(opponent_card)
    print("\n")

    # Player chooses a card to fight
    chosen_card_index = get_player_card_index(player_deck)
    player_card = player_deck[chosen_card_index]

    # Simulate the fight
    damage = max(0, player_card['Attack'] - opponent_card['Defense'])
    opponent_card['Defense'] = max(0, opponent_card['Defense'] - player_card['Attack'])
    opponent_card['Health'] = max(0, opponent_card['Health'] - damage)

    # Check if opponent is defeated
    if opponent_card['Health'] <= 0:
        opponent_deck.remove(opponent_card)
        print(f"{opponent_card['Name']} has been defeated!")
    else:
        print(
            f"{opponent_card['Name']} now has Health: {opponent_card['Health']} and Defense: {opponent_card['Defense']}")

    # Pause for dramatic effect
    time.sleep(3)

    # Opponent's turn
    if opponent_deck:
        print("It's the opponent's turn.")
        opponent_card = random.choice(opponent_deck)
        print("Opponent's card:")
        display_card(opponent_card)
        print("\n")

        # Opponent chooses a random card from player's deck
        chosen_card_index = random.randint(0, len(player_deck) - 1)
        player_card = player_deck[chosen_card_index]

        # Simulate the fight
        damage = max(0, opponent_card['Attack'] - player_card['Defense'])
        player_card['Defense'] = max(0, player_card['Defense'] - opponent_card['Attack'])
        player_card['Health'] = max(0, player_card['Health'] - damage)

        # Check if player's card is defeated
        if player_card['Health'] <= 0:
            player_deck.remove(player_card)
            print(f"You have lost {player_card['Name']}!")
        else:
            print(
                f"{player_card['Name']} now has Health: {player_card['Health']} and Defense: {player_card['Defense']}")

        # Pause for dramatic effect
        time.sleep(3)
    else:
        print("Opponent has no cards left. You win!")


# Main game loop
def main():
    player_deck = create_deck()
    opponent_deck = create_deck()

    while player_deck and opponent_deck:
        play_round(player_deck, opponent_deck)

    if player_deck:
        print("You are the winner!")
    else:
        print("Opponent won!")


# Start the game
if __name__ == "__main__":
    main()