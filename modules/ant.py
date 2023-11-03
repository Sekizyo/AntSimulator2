from random import choice, choices

class Ant():
    def __init__(self, x: int, y: int, searching: bool = True) -> None:
        self.x = x
        self.y = y
        self.searching = searching
        self.trainStrenght = -100

    def swtichModeTo(self, searching):
        if searching:
            self.searching = True
            self.trainStrenght = 100
        else:
            self.searching = False
            self.trainStrenght = -100

    def switchModes(self):
        if self.searching:
            self.searching = False
            self.trainStrenght = 100
        else:
            self.searching = True
            self.trainStrenght = -100

    def move(self, x, y):
        self.x = x
        self.y = y

        # if self.searching:
        #     self.trainStrenght += 1
        # else:
        #     self.trainStrenght -= 1

    def removeTrailType(self, moves: list[int], values: list[int], searching: bool):
        for i, value in enumerate(values):
            if value == 0 and not searching:
                values[i] = 10
            elif value == 0 and searching:
                values[i] = -10

        if searching:
            values = [-num for num in values]

        removed = 0
        for i, value in enumerate(values.copy()):
            if value < 0:
                moves.pop(i-removed)
                values.pop(i-removed)
                removed += 1

        return moves, values

    def decide(self, moves, values):
        movesCopy = moves.copy()
        moves, values = self.removeTrailType(moves, values, searching=(not self.searching))
        
        if values:
            x, y = choices(moves, values)[0]
            if values[moves.index((x, y))] >= 101:
                self.switchModes()

        else:
            x, y = choice(movesCopy)
        
        self.move(x, y)
        return x, y, self.trainStrenght
