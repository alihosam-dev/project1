"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - name: The name of the location
        - position: The position that cooresponds to where the location is found in the map
        - points: How many points the player recieves for going to that location
        - short_desc: The short description shown after the player visits the location more than one time
        - full_desc: The full description shown the the player when the first visit a location
        - commands: a list of available commands/directions
        - items: a list of items found stored in this location

    Representation Invariants:
        - name != ''
        - position == -1 or pos > 0
        - points > 0
        - short_desc != ''
        - full_desc != ''
    """

    name: str
    position: int
    points: int
    short_desc: str
    full_desc: str
    commands: list[str]
    items: list
    visited: bool

    def __init__(self, name: str, position: int, points: int, short_desc: str, full_desc: str) -> None:
        """Initialize a new location.
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.
        self.name = name
        self.position = position
        self.points = points
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.items = []
        self.visited = False

    def available_actions(self):
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        # TODO: Complete this method, if you'd like or remove/replace it if you're not using it

    def visited(self, visit: bool):
        """
        Change the status of whether the location has been visited before
        """
        self.visited = visit


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - # TODO

    Representation Invariants:
        - # TODO
    """

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: The x coordinate of the player as an int, it increases as the player moves to the right
        - y: The y coordinate of the player as an int, it increases as the player moves downwards
        - inventory: A list that stores the items the player has obtained
        - victory: A boolean that represents whether the player has won

    Representation Invariants:
        - x >= 0
        - y >= 0
    """

    x: int
    y: int
    inventory: list[Item]
    victory: bool

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False

    def move_horizontal(self, command: str) -> None:
        """
        Moves the player east or west
        """
        if command == "Go east":
            self.x += 1
        else:
            self.x -= 1

    def move_vertical(self, command: str) -> None:
        """
        Moves the player north or south
        """
        if command == 'Go south':
            self.y += 1
        else:
            self.y -= 1

    def pick_up_item(self, item: Item) -> None:
        """
        Adds the item given to the player's inventory
        """
        self.inventory.append(item)

    def victory(self, status: bool) -> None:
        """
        Changes the player's victory attribute based on the boolean given
        """
        self.victory = status


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - map_location_dict: a dictionary that returns a location based on cooresponding map number

    Representation Invariants:
        - # TODO
    """
    map: list[list[int]]
    items: list[Item]
    locations: list[Location]
    map_location_dict: dict[int, Location]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)

        self.load_item(items_data)

        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """
        map_so_far = []
        for line in map_data:
            map_so_far.append([int(num) for num in line.split()])
        return map_so_far

    def load_item(self, items_data: TextIO) -> None:
        """
        Creates new Item instances for each item in the item_data file. Item instances are stored in thier
        cooresponding locations.
        """

        for line in items_data:
            item_lst = line.split()

            item_name = item_lst[0].replace('_', ' ')
            item_start = int(item_lst[1])
            item_target = int(item_lst[2])
            item_target_points = int(item_lst[3])

            location = self.map_location_dict[item_start]
            new_item = Item(item_name, item_start, item_target, item_target_points)
            location.items.append(new_item)

    # TODO: Add methods for loading location data and item data (see note above).

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """

        return self.map_location_dict[self.map[y][x]]
