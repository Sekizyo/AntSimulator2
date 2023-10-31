import pygame

from modules.__config__ import BLOCKSIZE, WIDTHBLOCKS, HEIGHTBLOCKS

class Render():
    def renderGrid(self, blockRect: list[pygame.Rect], blocks: list[int]) -> None:
        for y, col in enumerate(blockRect):
            for x, rect in enumerate(col):
                ants = blocks[y][x]
                self.renderBlock(ants, rect)

    def renderBlock(self, value: int, rect: list[pygame.Rect]) -> None:
        if value == 0:
            pygame.draw.rect(self.surface, (0, 0, 0), rect)
        elif 0 < value <= 255:
            pygame.draw.rect(self.surface, (0, value, 0), rect)
        elif value > 255:
            pygame.draw.rect(self.surface, (0, 255, 0), rect)
        elif 0 > value >= -100:
            pygame.draw.rect(self.surface, (abs(value), 0, 0), rect)
        elif value == -101:
            pygame.draw.rect(self.surface, (0, 0, 255), rect)
        
class Position():
    def checkBounds(self, x: int, y: int) -> bool:
        if (0 <= x < WIDTHBLOCKS) and (0 <= y < HEIGHTBLOCKS):
            return True
        else:
            return False

    def getGridPosFromPos(self, pos: tuple) -> int:
        x, y = pos
        return x//BLOCKSIZE, y//BLOCKSIZE
    
    def getBlockValue(self, x: int, y: int) -> int:
        return self.blocks[y][x]

    def updateBlock(self, x: int, y: int, value: int) -> None:
        if self.checkBounds(x, y) and self.blocks[y][x] != -1:
            self.blocks[y][x] += value

    def setBlock(self, x: int, y: int, value: int) -> None:
        if self.checkBounds(x, y) and self.blocks[y][x] != -1:
            self.blocks[y][x] += value

class Moves(Position):
    def getMoves(self, startX: int, startY: int, depth: int=4) -> list[tuple()]:
        moves = []
        for x in range(-depth,depth+1):
            Y = int((depth*depth-x*x)**0.5)
            for y in range(-Y,Y+1):
                
                x1 = x+startX
                y1 = y+startY

                if self.checkBounds(x1, y1):
                    moves.append((x1, y1))

        return moves

    def getBlockValuesFromPosList(self, pos: list[tuple]) -> list[int]:
        values = []
        for x, y in pos:
            val = self.getBlockValue(x, y)
            if val >= 0:
                values.append(val)
        return values
    
    def getAverageForList(self, list: list) -> float:
        if list:
            return sum(list) / len(list)    

class TrailExpiration(Moves):
    def update(self, blocks: list[int]) -> None:
        for y, col in enumerate(blocks):
            for x, block in enumerate(col):
                self.expirate(x, y, block)

    def expirate(self, x: int, y: int, value: int) -> None:
        if 0 < value <= 100:
            self.updateBlock(x, y, -1)
        elif 0 > value >= -100:
            self.updateBlock(x, y, 1)

class Trail(TrailExpiration):
    pass

class Controls():
    def createBlocks(self) -> None:
        for y in range(HEIGHTBLOCKS):
            tempX = []
            tempXRect = []
            for x in range(WIDTHBLOCKS):
                tempX.append(0)
                tempXRect.append(pygame.Rect(x*self.size, y*self.size, self.size, self.size))
                
            self.blocks.append(tempX)
            self.blockRect.append(tempXRect)

    def addAntNest(self, mouse: tuple()) -> None:
        x, y = self.getGridPosFromPos(mouse)
        self.antCounter += 1
        self.setBlock(x, y, -101)

    def addFood(self, mouse: tuple()) -> None:
        x, y = self.getGridPosFromPos(mouse)
        self.foodCounter += 10
        self.updateBlock(x, y, 10)

    def reset(self) -> None:
        self.blocks = []
        self.blockRect = []
        self.antCounter = 0
        self.foodCounter = 0

        self.createBlocks()

class Grid(Render, Trail, Controls):
    def __init__(self, surface: pygame.surface.Surface) -> None:
        self.surface = surface
        self.size = BLOCKSIZE

        self.blocks = []
        self.blockRect = []
        
        self.antCounter = 0
        self.foodCounter = 0
        self.createBlocks()

    def render(self) -> None:
        self.renderGrid(self.blockRect, self.blocks)

    def logic(self) -> None:
        self.update(self.blocks)
