# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    current_room = "outside"
    items = []

    def list_items(self):
        if not len(self.items):
            print("You aren't carrying anything")
            return 0
        print("You have", end=" ")
        for item in self.items:
            print(f'a {item.name}', end=" ")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, itemName):
        for i, item in enumerate(self.items):
            if item.name == itemName:
                transferred = self.items.pop(i)
                return transferred
        return None
