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
from game_data import World, Item, Location, Player

# Note: You may add helper functions, classes, etc. here as needed

# Note: You may modify the code below as needed; the following starter template are just suggestions
if __name__ == "__main__":
    world = World(open("map.txt"), open("locations.txt"), open("items.txt"))
    player = Player(0, 0)  # set starting location of player; you may change the x, y coordinates here as appropriate

    while not player.game_status:
        location = world.get_location(player.x, player.y)

        if not location.visited:
            print(location.full_desc)
            location.visited_before()
        else:
            print(location.short_desc)

        print("What to do? \n")
        print("[menu]")
        for action in world.available_actions(player):
            print(action)
        choice = input("\nEnter action: ").upper()

        # Choice Handler
        if choice == 'GO NORTH':
            if world.get_location(player.x, player.y - 1):
                player.move(0, -1)
                player.use_move()
            else:
                print("\nInvalid Command")
        elif choice == 'GO EAST':
            if world.get_location(player.x + 1, player.y):
                player.move(1, 0)
                player.use_move()
            else:
                print("\nInvalid Command")
        elif choice == 'GO SOUTH':
            if world.get_location(player.x, player.y + 1):
                player.move(0, 1)
                player.use_move()
            else:
                print("\nInvalid Command")
        elif choice == 'GO WEST':
            if world.get_location(player.x - 1, player.y):
                player.move(-1, 0)
                player.use_move()
            else:
                print("\nInvalid Command")
        elif choice == 'LOOK':
            print(location.full_desc)
        elif choice == 'SEARCH':
            for item in location.items:
                print(f'You found the item: {item.name}')
        elif (len(choice.split(' ')) == 2) and (choice.split(' ')[0] == 'PICKUP'):
            found = False
            pickup_item = choice.split(' ')[1]
            for item in location.items:
                if item.name.upper() == pickup_item:
                    found = True
                    player.pick_up_item(item, location)
            if not found:
                print("\nInvalid Command")
        elif (len(choice.split(' ')) == 2) and (choice.split(' ')[0] == 'DROP'):
            found = False
            drop_item = choice.split(' ')[1]
            for item in player.inventory:
                if item.name.upper() == drop_item:
                    found = True
                    player.drop_item(item, location)
            if not found:
                print("\nInvalid Command")
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
            ...
        else:
            print("\nInvalid Command")
