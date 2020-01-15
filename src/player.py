# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, playerName, currentRoom):
        self.playerName = playerName
        self.currentRoom = currentRoom

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
        return f"Item REPR Call\n Player name: ({self.playerName})\n" \
               f" Current Room: ({self.currentRoom})\n" \
               f" Item Name: ({self.itemName})\n" \
               f" Item Description: ({self.itemDescription})\n" \


# new_Player = Player(
#     playerName="Player 1",
#     currentRoom="outside",
#     playerID=1
# )
#
# new_Item = Item(
#     currentRoom=0,
#     playerID=0,
#     playerName=0,
#     itemDescription="testing item desc",
#     itemName="Testing Item Name"
# )
# print(repr(new_Item))
# print(repr(new_Player))
