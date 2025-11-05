class Tile:
    def __init__(self,name, type):
        self.name = name
        self.type = type
        self.available = True


class PropertyTile(Tile):
    def __init__(self,name, type, city, price, rent):
        super().__init__(name, type)
        self.city = city
        self.price = price
        self.rent = rent
        self.owner = None

class RailTile(PropertyTile):
    pass

class BonusTile(Tile):
    def bonus(self, amount):
        return amount

class TaxTile(Tile):
    def tax(self,amount):
        return amount

class JailTile(Tile):
    pass

class GoToJailTile(Tile):
    pass


