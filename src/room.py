# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    n_to = e_to = s_to = w_to = None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, itemName):
        for i, item in enumerate(self.items):
            if item.name == itemName:
                transferred = self.items.pop(i)
                return transferred
        return None

    def list_items(self):
        if not len(self.items):
            print("You don't see anything here")
            return 0
        print("You see", end=" ")
        for item in self.items:
            print(f'a {item.name}', end=" ")
