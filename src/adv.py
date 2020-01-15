from src.room import Room
from src.player import Player, Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Testing', room['outside'])
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
def roomUpdater(roomUpdaterInput):
    if roomUpdaterInput == 'n':
        if newPlayer.currentRoom.n_to is None:
            print("there is no room to move there \n")
            return newPlayer.currentRoom
        else:
            return newPlayer.currentRoom.n_to
    if roomUpdaterInput == 's':
        if newPlayer.currentRoom.s_to is None:
            print("\n***There is no room to move there***\n")
            return newPlayer.currentRoom
        else:
            return newPlayer.currentRoom.s_to
    if roomUpdaterInput == 'w':
        if newPlayer.currentRoom.w_to is None:
            print("\n***There is no room to move there***\n")
            return newPlayer.currentRoom
        else:
            return newPlayer.currentRoom.w_to
    if roomUpdaterInput == 'e':
        if newPlayer.currentRoom.e_to is None:
            print("\n***There is no room to move there***\n")
            return newPlayer.currentRoom
        else:
            return newPlayer.currentRoom.e_to
    if roomUpdaterInput == 'q':
        quit()
    if roomUpdaterInput != ('n', 's', 'w', 'e', 'q'):
        print("\nInvalid input\n")
        quit()


while True:
    print(repr(newPlayer.currentRoom))
    userInput = input(
        "\nEnter n, s, e, w, or q to quit: ")
    newPlayer.currentRoom = roomUpdater(userInput)
