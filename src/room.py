# Implement a class to hold room information. This should have name and
# description attributes.

# class Item:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.n_to = None

    # def __str__(self):
    #     return f"Room name: {self.name}, Room description: , {self.description}"
    #
    def __repr__(self):
        return f"Current Room name:\n ({self.name})\n" \
               f"Room description:\n ({self.description})"


# new_room = Room("Testing Room", "Testing description")

# str is the string representation of the room, repr is the object representation of the room
# print(new_room)
# print("REPR name", repr(new_room.name), "REPR description", repr(new_room.description))
