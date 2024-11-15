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
import random
import time


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - name: The name of the location
        - position: The position that cooresponds to where the location is found in the map
        - points: How many points the player recieves for going to that location
        - short_desc: The short description shown after the player visits the location more than one time
        - full_desc: The full description shown the player when the first visit a location
        - commands: a list of available commands/directions
        - items: a list of items found stored in this location
        - the position id used to coorespond the location to the map

    Representation Invariants:
        - name != ''
        - (position == -1) or (position > 0)
        - short_desc != ''
        - full_desc != ''
        - len(full_desc) >= len(short_desc)
    """

    name: str
    points: int
    short_desc: str
    full_desc: str
    commands: list[str]
    items: list
    visited: bool
    position: int

    def __init__(self, name: str, points: int, short_desc: str, full_desc: str, position: int) -> None:
        """Initialize a new location.
        """

        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.
        self.name = name
        self.points = points
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.items = []
        self.visited = False
        self.position = position

    def visited_before(self) -> None:
        """
        Change the status of whether the location has been visited before.

        >>> new_location = Location('New Location', 0, 'Short description', 'this is a longer description', -2)
        >>> new_location.visited == False
        True
        >>> new_location.visited_before()
        >>> False == new_location.visited
        False
        """
        self.visited = True


class PuzzleLocation(Location):
    """
    A Location object that contains an additonal attribute and a puzzle method that can be played by the player
    in the game

        Instance Attributes:
            - name: The name of the location
            - position: The position that cooresponds to where the location is found in the map
            - points: How many points the player recieves for going to that location
            - short_desc: The short description shown after the player visits the location more than one time
            - full_desc: The full description shown the player when the first visit a location
            - commands: a list of available commands/directions
            - items: a list of items found stored in this location
            - position: the position id used to coorespond the location to the map
            - access : boolean for whether player has access to the location
            - game_won: integer representing if the player has won the game at the puzzle location

        Representation Invariants:
            - name != ''
            - (position == -1) or (position > 0)
            - short_desc != ''
            - full_desc != ''
            - len(full_desc) >= len(short_desc)
            - game_won == 0 or game_won == 1
        """

    name: str
    points: int
    short_desc: str
    full_desc: str
    commands: list[str]
    items: list
    visited: bool
    position: int
    access: bool
    game_won: int

    def __init__(self, name: str, points: int, short_desc: str, full_desc: str, position: int) -> None:
        """Initialize a new location.
        """

        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.
        super().__init__(name, points, short_desc, full_desc, position)
        self.name = name
        self.points = points
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.items = []
        self.visited = False
        self.position = position
        self.access = False
        self.game_won = 1

    def play_puzzle(self) -> int:
        """
        Allows the player to play a puzzle depending on the specific Location the player is currently at.
        Returns and integer value for the number of points the player recieves for the result of playing the puzzle.
        """
        if self.position == 4:  # change
            print("Chet just got done with math lecture here and he's feeling pretty confident! He bets "
                  "he can answer more multiplication questions in 30 seconds than you! Wanna play?")
            while True:
                choice = input('Would you like to Begin or Exit: ').upper()
                if choice == 'EXIT':
                    return 0
                elif choice != 'BEGIN':
                    print('Invalid Choice')
                else:
                    score = 0
                    start_time = time.time()
                    while time.time() - start_time < 30:
                        x1 = random.randint(0, 12)
                        x2 = random.randint(0, 12)
                        answer = int(input(f'What is {x1} x {x2}: '))
                        if answer == x1 * x2:
                            score += 1
                    if score >= 10:
                        print(f'You passed the test with {score} correct answers!')
                        prize = score * 4 * self.game_won
                        self.game_won = 0
                        return prize
                    else:
                        print('You did not pass the test :(. You may retake the test.')

        elif self.position == 13:  # change
            print('Ali challenges you to a dance battle! Hit the right notes (D, F, J, K) to dance'
                  'like a star! Warm up your legs!')
            while True:
                choice = input('Would you like to Begin or Exit: ').upper()
                if choice == 'EXIT':
                    return 0
                elif choice != 'BEGIN':
                    print('Invalid Choice')
                else:
                    score = 0
                    start_time = time.time()
                    while time.time() - start_time < 30:
                        options = ['D', 'F', 'J', 'K']
                        random_index = random.randint(0, 3)
                        answer = input(f'Hit {options[random_index]}: ').upper()
                        if answer == options[random_index]:
                            score += 1
                    if score >= 22:
                        print(f'You passed the test with {score} correct hits!')
                        prize = score * self.game_won
                        self.game_won = 0
                        return prize
                    else:
                        print('You did not pass the test :(. You may retake the test.')

    def grant_access(self):
        """
        Changes the status of whether the player has access to the location
        """
        self.access = True


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name : The name of the item
        - start : The starting position of the item
        - target : The position of the target location of the item
        - target_points: The nummber of points the player receives for taking the item to the target

    Representation Invariants:
        - name != ""
        - start > 0
        - target > 0
    """

    name: str
    start_position: int
    target_position: int
    target_points: int

    def __init__(self, name: str, start: int, target: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.

        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points


class UsableItem(Item):
    """A usable item in our text adventure game world. Inherits Item class

        Instance Attributes:
            - name : The name of the item
            - start : The starting position of the item
            - target : The position of the target location of the item
            - use_locations: List of position of locations where the item can be used
            - target_points: The nummber of points the player receives for taking the item to the target

        Representation Invariants:
            - name != ""
            - start > 0
            - target > 0
        """

    name: str
    start_position: int
    target_position: int
    target_points: int
    use_locations: list[int]

    def __init__(self, name: str, start: int, target: int, target_points: int, use_locations: list[int]) -> None:
        """Initialize a new usable item.
        """
        Item.__init__(self, name, start, target, target_points)
        self.name = name
        self.start_position = start
        self.target_position = target
        self.target_points = target_points
        self.use_locations = use_locations


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x: The x coordinate of the player as an int, it increases as the player moves to the right
        - y: The y coordinate of the player as an int, it increases as the player moves downwards
        - remaining_moves: The number of remain move the player has before they lose the game
        - inventory: A list that stores the items the player has obtained
        - game_status: A boolean that represents whether the player has won
        - score: An integer that represents the current score of the player

    Representation Invariants:
        - x >= 0
        - y >= 0
        - remaining_moves >= 0
    """

    x: int
    y: int
    remaining_moves: int
    inventory: list[Item | UsableItem]
    game_status: bool
    score: int

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        self.x = x
        self.y = y
        self.inventory = []
        self.game_status = False
        self.score = 0
        self.remaining_moves = 40  # Change for more moves

    def move(self, dx: int, dy: int) -> None:
        """
        Moves the player

        >>> new_player = Player(2,2)
        >>> (new_player.x, new_player.y)
        (2, 2)
        >>> new_player.move(1,0)
        >>> (new_player.x, new_player.y)
        (3, 2)
        """

        self.x += dx
        self.y += dy

    def use_move(self):
        """
        Use one of the player's remaining moves

        >>> new_player = Player(2,2)
        >>> starting_moves = new_player.remaining_moves
        >>> new_player.use_move()
        >>> starting_moves == new_player.remaining_moves + 1
        True
        """

        self.remaining_moves -= 1

    def pick_up_item(self, item: Item | UsableItem, location: Location) -> None:
        """
        Adds the item given to the player's inventory

        >>> new_player = Player(2,2)
        >>> new_item = Item('New Item', 1, 2, 3)
        >>> new_location = Location('New Location', 0, 'Short description', 'this is a longer description', -2)
        >>> new_location.items.append(new_item)
        >>> new_location.items == [new_item]
        True
        >>> new_player.inventory
        []
        >>> new_player.pick_up_item(new_item, new_location)
        >>> new_player.inventory == [new_item]
        True
        >>> new_location.items == []
        True
        """
        self.inventory.append(item)
        if item.name == 'Laptop':
            print("You found your laptop! You left this here yesterday in the panic of realizing you have to go to "
                  "bed! You might wanna take this with you to the exam centre.")
        location.items.remove(item)

    def drop_item(self, item: Item, location: Location) -> None:
        """
        Removes the item given from the player's inventory

        >>> new_player = Player(2,2)
        >>> new_item = Item('New Item', 1, 2, 3)
        >>> new_player.inventory.append(new_item)
        >>> new_location = Location('New Location', 0, 'Short description', 'this is a longer description', -2)
        >>> new_location.items == []
        True
        >>> new_player.inventory == [new_item]
        True
        >>> new_player.drop_item(new_item, new_location)
        >>> new_player.inventory == []
        True
        >>> new_location.items == [new_item]
        True
        """
        self.inventory.remove(item)
        location.items.append(item)
        if item.target_position == location.position:
            if item.name == 'Rotman Backpack':
                print("Tiana: You found it! Thank you so much, I don't know how to thank you, this backpack is almost"
                      "my entire personality.")
            self.score += item.target_points
            item.target_points = 0

    def use_item(self, item: UsableItem, location: PuzzleLocation):
        """
        Uses the item at the given location, item stays in player inventory
        """
        if location.position in item.use_locations:
            location.grant_access()

    def victory(self, status: bool) -> None:
        """
        Changes the player's victory attribute based on the boolean given

        >>> new_player = Player(2,2)
        >>> new_player.game_status
        False
        >>> new_player.victory(True)
        >>> new_player.game_status
        True
        """
        self.game_status = status


class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - items: A list of all the items in the world
        - locations: a list of all the locations in the world
        - map_location_dict: a dictionary that returns a location based on cooresponding map number

    Representation Invariants:
        - all({location.position >= -1 for location in locations})
        - map_location_dict != {}
        - map != []
    """
    map: list[list[int]]
    items: list[Item | UsableItem]
    locations: list[Location | PuzzleLocation]
    puzzle_locations: list[PuzzleLocation]
    map_location_dict: dict[int, Location]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO, usable_items_data: TextIO,
                 puzzle_locations_data: TextIO) -> None:
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
        self.map_location_dict = {}

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.locations = self.load_location(location_data, puzzle_locations_data)
        self.items = self.load_item(items_data, usable_items_data)

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

    def load_location(self, location_data: TextIO, puzzle_locations_data: TextIO) -> list[Location]:
        """
        Creates new Location intances from the locations in location_data. Updates the self.map_location_dict with
        the cooresponding mapping of the position of the location to the location itself
        """

        locations = []

        while location_data.readline() != '':
            first_line = location_data.readline().split()
            name = first_line[0]
            position = int(first_line[1])

            points = int(location_data.readline().strip())
            short_desc = location_data.readline().strip()
            full_desc = ''
            curr_line = location_data.readline().strip()
            while curr_line != 'END':
                full_desc += curr_line + ' '
                curr_line = location_data.readline().strip()

            new_location = Location(name, points, short_desc, full_desc, position)
            locations.append(new_location)
            self.map_location_dict[position] = new_location

        while puzzle_locations_data.readline() != '':
            first_line = puzzle_locations_data.readline().split()
            name = first_line[0]
            position = int(first_line[1])

            points = int(puzzle_locations_data.readline().strip())
            short_desc = puzzle_locations_data.readline().strip()
            full_desc = ''
            curr_line = puzzle_locations_data.readline().strip()
            while curr_line != 'END':
                full_desc += curr_line + ' '
                curr_line = puzzle_locations_data.readline().strip()

            new_location = PuzzleLocation(name, points, short_desc, full_desc, position)
            locations.append(new_location)
            self.map_location_dict[position] = new_location

        return locations

    def load_item(self, items_data: TextIO, usable_items_data: TextIO) -> list[Item]:
        """
        Creates new Item instances for each item in the item_data file. Item instances are stored in thier
        cooresponding locations.
        """

        items = []
        for line in items_data:
            item_lst = line.split()

            item_name = item_lst[0].replace('_', ' ')
            item_start = int(item_lst[1])
            item_target = int(item_lst[2])
            item_target_points = int(item_lst[3])

            location = self.map_location_dict[item_start]
            new_item = Item(item_name, item_start, item_target, item_target_points)
            items.append(new_item)
            location.items.append(new_item)
        usable_line_1 = usable_items_data.readline()
        item_lst = usable_line_1.split()
        item_name = item_lst[0].replace('_', ' ')
        item_start = int(item_lst[1])
        item_target = int(item_lst[2])
        item_target_points = int(item_lst[3])
        location = self.map_location_dict[item_start]
        usable_line_2 = usable_items_data.readline()
        use_locations = [int(item) for item in usable_line_2.split()]
        new_item = UsableItem(item_name, item_start, item_target, item_target_points, use_locations)
        items.append(new_item)
        location.items.append(new_item)
        return items

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location] | Optional[PuzzleLocation]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """

        location_in_bounds = (0 <= x < len(self.map[0])) and (0 <= y < len(self.map))

        if location_in_bounds and self.map[y][x] != -1:
            return self.map_location_dict[self.map[y][x]]
        else:
            return None

    def available_actions(self, player: Player) -> list[str]:
        """
        Return the available actions in this location.
        The actions should depend on the items available in the location
        and the x,y position of this location on the world map.
        """

        # NOTE: This is just a suggested method
        # i.e. You may remove/modify/rename this as you like, and complete the
        # function header (e.g. add in parameters, complete the type contract) as needed

        actions_list = []

        go_list = []
        if self.get_location(player.x, player.y - 1):
            go_list.append('north')
        if self.get_location(player.x + 1, player.y):
            go_list.append('east')
        if self.get_location(player.x, player.y + 1):
            go_list.append('south')
        if self.get_location(player.x - 1, player.y):
            go_list.append('west')
        go_str = ''
        for direction in go_list:
            go_str += ', ' + direction
        go_str = go_str[2:]
        actions_list.append(f'- Go [{go_str}]')

        if (type(self.get_location(player.x, player.y)) is PuzzleLocation
                and (self.get_location(player.x, player.y).position == 4 or
                     self.get_location(player.x, player.y).position == 13)):
            actions_list.append('- Talk')

        actions_list.extend(['- Use/Drop/Pickup {item}', '- Search', '- Look', '- Score',
                             '- Inventory', '- Menu', '- Quit'])

        if len(actions_list) % 2 != 0:
            actions_list.append('')

        return actions_list
