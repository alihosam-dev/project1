"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

# Note: You may add in other import statements here as needed
from game_data import PuzzleLocation, World, Item, Location, Player

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    world = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    player = Player(0, 0)  # set starting location of player; you may change the x, y coordinates here as appropriate
    prev_location = None

    # Create a list of required items for win codition
    required_item = {item for item in world.items if item.name == 'T-Card' or
                     item.name == 'Cheat Sheet' or
                     item.name == 'Lucky Exam Pen'}

    while not player.game_status:
        location = world.get_location(player.x, player.y)

        if location != prev_location:
            if not location.visited:
                print(location.full_desc)
                location.visited_before()
            else:
                print(location.short_desc)

            print("What to do? \n")
            print("[Menu]")
            menu_str = ''
            actions = world.available_actions(player)
            for i in range(len(actions) // 2):
                menu_str += '{0:30}  1}\n'.format(actions[2 * i], actions[2 * i + 1])
            print(menu_str, end='')

        prev_location = location
        choice = input("\nEnter action: ").upper()

        # Choice Handler
        if choice == 'GO NORTH':
            if world.get_location(player.x, player.y - 1):
                player.move(0, -1)
                player.use_move()
            else:
                print("\nOut of bounds. Move a differnt direction.")
        elif choice == 'GO EAST':
            if world.get_location(player.x + 1, player.y):
                player.move(1, 0)
                player.use_move()
            else:
                print("\nOut of bounds. Move a differnt direction.")
        elif choice == 'GO SOUTH':
            if world.get_location(player.x, player.y + 1):
                player.move(0, 1)
                player.use_move()
            else:
                print("\nOut of bounds. Move a differnt direction.")
        elif choice == 'GO WEST':
            if world.get_location(player.x - 1, player.y):
                player.move(-1, 0)
                player.use_move()
            else:
                print("\nOut of bounds. Move a differnt direction.")
        elif choice == 'LOOK':
            print(location.full_desc)
        elif choice == 'SEARCH':
            found = False
            for item in location.items:
                print(f'You found the item: {item.name}')
                found = True
            if not found:
                print('Nothing was found.')
        elif choice.split(' ')[0] == 'PICKUP':
            found = False
            pickup_item = str.join(' ', choice.split(' ')[1:])
            for item in location.items:
                if item.name.upper() == pickup_item:
                    found = True
                    player.pick_up_item(item, location)
                    print(f"{item.name} was picked up.")
            if not found:
                print("\nItem not found.")
        elif choice.split(' ')[0] == 'DROP':
            found = False
            drop_item = str.join(' ', choice.split(' ')[1:])
            for item in player.inventory:
                if item.name.upper() == drop_item:
                    found = True
                    player.drop_item(item, location)
                    print(f"{item.name} was dropped.")
            if not found:
                print("\nThat item is not in your inventory.")
        elif (len(choice.split(' ')) == 2) and (choice.split(' ')[0] == 'Use'):
            # Impliment this later
            ...
        elif choice == 'INVENTORY':
            print("[inventory]")
            for item in player.inventory:
                print(f'- {item.name}')
        elif choice == 'SCORE':
            print(player.score)
        elif choice == 'QUIT':
            player.victory(True)
        elif choice == 'TALK':
            if location is PuzzleLocation and (location.position == 4 or location.position == 13):
                location.play_puzzle()
        elif choice == 'MENU':
            print('[Menu]')
            menu_str = ''
            actions = world.available_actions(player)
            for i in range(len(actions) // 2):
                menu_str += '- {0:30}  - {1}\n'.format(actions[2 * i], actions[2 * i + 1])
            print(menu_str, end='')
        else:
            print("\nInvalid Command")

        # Win Condition
        if set(world.map_location_dict[17].items) & required_item == required_item:  # Set Intersection
            print(f'You made it! You reached the Exam Center with your T-Card, Cheat Sheet, and Lucky Exam Penn'
                  f'and you are ready to ace your exam. Your final score was: {player.score}!')
            player.victory(True)

        # Loss Condition
        if player.remaining_moves <= 0:
            print(f'Oh no... Your Exam started and you did not make it to the Exam Center with your T-Card, '
                  f'Cheat Sheet, and Lucky Exam Penn. You Lost :(')
            player.victory(True)
