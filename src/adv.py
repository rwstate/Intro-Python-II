from room import Room
from player import Player
from item import Item
# from textWrap import wrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('sword', 'a cool sword')]
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('sword', 'a cool sword')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

first_run = True

while True:
    if first_run:
        print(f'-------{room[player.current_room].name}-------')
        print(room[player.current_room].description)
        room[player.current_room].list_items()
        print()
        first_run = False
    playerCmd = input('What will you do? ')
    while not len(playerCmd):
        print()
        playerCmd = input('What will you do? ')
    if playerCmd.split()[0] not in 'n s e w q i inventory get drop look'.split():
        print("I don't understand ")
        continue
    if playerCmd.split()[0] in 'n s e w q':
        if len(playerCmd.split()) > 1:
            print("I don't understand ")
            continue
        if playerCmd == 'q':
            print('Goodbye')
            break
        if not getattr(room[player.current_room], f'{playerCmd}_to'):
            print('No obvious exits in that direction')
            continue
        player.current_room = getattr(
            room[player.current_room], f'{playerCmd}_to')
        print(f'-------{room[player.current_room].name}-------')
        print(room[player.current_room].description)
        room[player.current_room].list_items()
        print()
        continue
    if playerCmd.split()[0] in 'i inventory':
        if len(playerCmd.split()) > 1:
            print("I don't understand ")
            continue
        player.list_items()
        continue
    if playerCmd.split()[0] in 'l look':
        if len(playerCmd.split()) > 1:
            print("I don't understand ")
            continue
        print(f'-------{room[player.current_room].name}-------')
        print(room[player.current_room].description)
        room[player.current_room].list_items()
        print()
        continue
    if len(playerCmd.split()) > 2:
        print("I don't understand")
        continue
    if playerCmd.split()[0] == 'get':
        result = room[player.current_room].remove_item(playerCmd.split()[1])
        if not result:
            print("I don't see that item here")
        else:
            result.on_get()
            player.add_item(result)
    else:
        result = player.remove_item(playerCmd.split()[1])
        if not result:
            print("That item is not in your inventory")
        else:
            result.on_drop()
            room[player.current_room].add_item(result)
