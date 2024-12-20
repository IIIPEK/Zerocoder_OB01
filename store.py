class Item:
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}\tPrice: {self.price}"

    def __getitem__(self, item):
        return {self.name:self.price}

class Store:
    def __init__(self, name="", address=""):
        self.name = name
        self.address = address
        self.items = []

    def additem(self, item):
        self.items.append(item)
        print(f"+++ Item\n{item}\n+++ Added")

    def removeitem(self, itemname):
        for item in self.items:
            if item.name == itemname:
                print(f"--- Item\n{item}\n--- Removed")
                self.items.remove(item)
                break

    def displayitems(self):
        print("Items:")
        for item in self.items:
            print(item)

    def countitems(self):
        return len(self.items)

    def __str__(self):
        return f"Name: {self.name}\tAddress: {self.address}\tItems: {self.items}"

