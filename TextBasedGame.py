# Tyler Bryant.

import copy  # Import the 'copy' module to create deep copies of data structures.


def show_intro(player_name=None):
    # Print the introduction to the game, including the storyline.
    print('\nWelcome to Sir Toiletry Saves the Day!,', player_name + '!', '\n', '------------------------------', '\n',
          '*** STORYLINE ***', '\n',
          'You and Sir Toiletry, were given a request by the king to eliminate any Evil Plumbers.', '\n',
          'So, being the nobles men you both are, you willingly accept the king request and venture out', '\n',
          'in search of Evil Plumbers. On your journey you see an Evil Plumber walk into an old castle', '\n',
          'and so you follow after him, but sadly after you entered the castle you tripped and lost your stuff.', '\n',
          "Now you must get your stuff back as you'll need them in order to defeat the Evil Plumber.")


def show_instructions():
    # Print the instructions for how to play the game.
    print('------------------------------', '\n', '*** INSTRUCTIONS ***', '\n',
          'To move about, type commands: go South, go North, go East, go West', '\n',
          'To add an item to your inventory, type the word: get or grab and the "item name" (without quotes)', '\n',
          'To show the instructions again, type: instructions', '\n',
          'To quit the game, type: quit or exit', '\n', '------------------------------')


def move_between_rooms(current_room, move, rooms):
    # This function handles moving between rooms by updating the current room.
    current_room = rooms[current_room][move]  # Get the next room based on the direction.
    return current_room  # Return the new room name.


def grab_item(current_room, rooms, inventory):
    # This function allows the player to pick up an item from the current room.
    if 'item' in rooms.get(current_room, {}):  # Check if there's an item in the current room.
        item_name = rooms[current_room]['item']  # Get the item's name from the room.
        print(f'You picked up the {item_name}')  # Notify the player they picked up the item.
        inventory.append(item_name)  # Add the item to the player's inventory.
        del rooms[current_room]['item']  # Remove the item from the room after it's picked up.

        # If the room is empty after picking up the item, notify the player.
        if 'item' not in rooms[current_room]:
            print('The room is empty.')


def main():
    # Dictionary defining the rooms and their connections. Each room contains directions and possibly an item.
    initial_rooms = {
        'Lobby': {'South': 'Bathroom', 'North': 'Dining room', 'West': 'Entry way', 'East': 'Kitchen'},
        'Entry way': {'West': 'Lobby', 'item': 'Trash can'},
        'Dining room': {'South': 'Lobby', 'West': 'Library', 'item': 'Toilet brush'},
        'Kitchen': {'West': 'Basement', 'East': 'Lobby', 'item': 'Bar of soap'},
        'Library': {'East': 'Dining room', 'item': 'Toilet paper roll'},
        'Basement': {'South': 'Garden', 'East': 'Kitchen', 'West': 'Evil Lair', 'item': 'Turd'},
        'Garden': {'North': 'Basement', 'East': 'Bathroom', 'item': 'Rusty faucet'},
        'Bathroom': {'North': 'Lobby', 'West': 'Garden', 'item': 'Plunger'},
        'Evil Lair': {}  # The Evil Lair is an end game, you will need all items to win, if you don't have all items you lose
    }

    # Create a deep copy of the initial rooms to allow the game to reset later.
    rooms = copy.deepcopy(initial_rooms)

    # Initialize the player's inventory as an empty list.
    inventory = []

    # Set the player's starting room to the 'Lobby'.
    current_room = 'Lobby'

    # Prompt the player for their name.
    player_name = input("Enter your name, player: ")

    # Show the game introduction using the player's name.
    show_intro(player_name)

    # Show the game instructions.
    show_instructions()

    # Game loop: the game continues until the player quits or wins.
    while True:
        # Check if the player is in the 'Evil Lair' (final room).
        if current_room == 'Evil Lair':
            # If the player has collected all 7 items, they win the game.
            if len(inventory) == 7:
                print('Congratulations, you managed to find your stuff and defeated the Evil Plumber!'
                      , player_name + '!')
                break  # End the game after winning.
            else:
                # If the player hasn't collected all 7 items, they lose.
                print('Oh NO! You forgot to collect the 7 items you needed to help you win.')
                print('So now you and Sir Toiletry have been killed by the Evil Plumber! Well that smells.')
                print('Thank you for playing Sir Toiletry Saves the Day!', player_name + '.')

                # Ask if the player wants to replay the game.
                replay = input('Do you want to replay? (Yes/No)\n').title()
                if replay == 'Yes':
                    # Reset the game to the initial state.
                    rooms = copy.deepcopy(initial_rooms)
                    current_room = 'Lobby'  # Start in the Lobby again.
                    inventory = []  # Clear the inventory.
                else:
                    print('Thank you for playing Sir Toiletry Saves the Day!')
                    break  # End the game if the player chooses not to replay.

        # Display the current room the player is in.
        print('You are in the ' + current_room)

        # Display the player's current inventory.
        if not inventory:  # If the inventory is empty, print a message.
            print('You do not have any items in your inventory.')
        else:  # If there are items in the inventory, list them.
            print('Your inventory contains:', ', '.join(inventory))

        # If there is an item in the room, display it.
        if current_room != 'Evil Lair' and 'item' in rooms[current_room].keys():
            print('You found a {}, let\'s pick it up.'.format(rooms[current_room]['item']))

        # Prompt the player for their next move.
        print('------------------------------')
        move = input('Enter your next move: ').title().split()  # Get the player's move and split into a list.

        # Handle movement to a new room.
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            # If the move is valid (direction exists in the current room), change the room.
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue  # Skip the rest of the loop and continue with the new room.

        # Check if the player is trying to grab an item from the room.
        item_in_room = 'item' in rooms[current_room]  # Check if there's an item in the current room.
        item_name = rooms[current_room]['item'].lower() if item_in_room else None  # Get the item name (lowercase).
        command = move[0].lower() if len(move) >= 2 else None  # Get the command (e.g., "get").
        item_to_get = ' '.join(move[1:]).lower() if len(move) >= 2 else None  # Get the item name after "get".

        # If the player types 'get' followed by the correct item name, pick it up.
        if command == 'get' or 'grab' and item_to_get == item_name:
            print(f'You picked up the {rooms[current_room]["item"]}')  # Notify the player.
            print('------------------------------')
            grab_item(current_room, rooms, inventory)  # Add the item to inventory and remove it from the room.

        # If the player types 'instructions', show the instructions again.
        elif move == ['Instructions']:
            show_instructions()
            continue  # Restart the loop to allow for another command.

        # If the player types 'quit' or 'exit', exit the game.
        elif move == ['Quit'] or move == ['Exit']:
            print('You have quit the game, Thank you for playing', player_name + '.')
            break  # End the game.

        # If the command is invalid, ask the player to try again.
        else:
            print('Invalid command, please try again')
            continue  # Restart the loop for the next command.


# Start the game.
main()
