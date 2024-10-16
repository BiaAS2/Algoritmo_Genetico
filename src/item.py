class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"Item(name='{self.name}', weight={self.weight}, value={self.value})"