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

    menu = ["look", "inventory", "score", "quit", "back"]

    while not player.victory:
        location = world.get_location(player.x, player.y)

        # TODO: ENTER CODE HERE TO PRINT LOCATION DESCRIPTION
        # Depending on whether or not it's been visited before,
        # print either full description (first time visit) or brief description (every subsequent visit)

        print("What to do? \n")
        print("[menu]")
        for action in location.available_actions():
            print(action)
        choice = input("\nEnter action: ").upper()

        if choice == "[MENU]":
            print("Menu Options: \n")
            for option in menu:
                print(option)
            choice = input("\nChoose action: ")

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
            print("do something")
        elif choice == 'INVENTORY':
            print("do something")
        elif choice == 'SCORE':
            print("do something")
        elif choice == 'QUIT':
            print("do something")
        elif choice == 'BACK':
            print("do something")
            ...
        else:
            print("\nInvalid Command")


        # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
        #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
        #  the choice the player made was just a movement, so only updating player's position is enough to change the
        #  location to the next appropriate location
        #  Possibilities:
        #  A helper function such as do_action(w, p, location, choice)
        #  OR A method in World class w.do_action(p, location, choice)
        #  OR Check what type of action it is, then modify only player or location accordingly
        #  OR Method in Player class for move or updating inventory
        #  OR Method in Location class for updating location item info, or other location data etc....
