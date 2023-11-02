from random import randint
class Ant():
    def __init__(self, x: int, y: int, searching: bool = True) -> None:
        self.x = x
        self.y = y
        self.searching = searching
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

        if self.searching:
            self.trainStrenght -= 1
        else:
            self.trainStrenght += 1

    def decide(self, moves, values):
        if self.searching:
            best = max(values)
            if best > 100:
                self.switchModes()
        else:
            best = min(values)
            if best == -101:
                self.switchModes()

        x, y = moves[values.index(best)]
        self.move(x, y)

        return x, y, self.trainStrenght


