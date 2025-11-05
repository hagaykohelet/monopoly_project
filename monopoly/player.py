from monopoly.board import Board


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.money = 1500
        self.property_list = []

    def property(self, prop):
        self.property_list.append(prop)

    def operations(self, oper):
        if oper == "move":
            move = Board()
            self.location += move.move()

        elif oper == "got":
            self.money += 100

        elif oper == "pay":
            how_much = int(input("how much money you need to pay? "))
            self.money -= how_much
