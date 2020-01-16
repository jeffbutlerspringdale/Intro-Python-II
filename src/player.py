# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, playerName, currentRoom):
        self.playerName = playerName
        self.currentRoom = currentRoom
        self.playerItems = []

    def __str__(self):
        return f"Player name: {self.playerName}, Current Room: {self.currentRoom}"

    def __repr__(self):
        return f"Player REPR call\n Player name: ({self.playerName})\n" \
               f" Current Room: ({self.currentRoom})\n"

class Item(Player):
    def __init__(self, itemName, itemDescription, playerName, currentRoom):
        super(Item, self).__init__(playerName, currentRoom)
        self.itemName = itemName
        self.itemDescription = itemDescription

    def __repr__(self):
        return f"\nCurrent Items({self.itemName})\n" \
               f"\nItem Description: ({self.itemDescription})\n" \
