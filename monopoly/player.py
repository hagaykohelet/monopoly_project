from monopoly.board import Board


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.money = 1500
        self.property_list = []

    def property(self, prop):
        self.property_list.append(prop)

    def pay(self, oper):
        self.money -= oper

    def get_money(self, amount):
        self.money += amount

    def move(self):
        Board.move(self.location)

    def purchase(self, amount):
        self.money -= amount
