import pygame


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define coordinate variables


class McGyver():

    def __init__(self, map=None, sprite=None):
        x = 1
        y = 1
        super().__init__()
        self.position = Position(x, y)  # self.position.x, self.position.y
        self.map = map
        self.sprite = pygame.image.load("ressource\\MacGyver.png")
        self.items = 0
        # define the hero coordinates on the map

    def move(self, input):
        a = True
        if (input == "HAUT" and
                self.map[self.position.x][self.position.y+1] == "0"):
            self.position.y += 1
        elif (input == "BAS" and
              self.map[self.position.x][self.position.y-1] == "0"):
            self.position.y -= 1
        elif (input == "DROITE" and
                       self.map[self.position.x+1][self.position.y] == "0"):
            self.position.x += 1
        elif (input == "GAUCHE" and
              self.map[self.position.x-1][self.position.y] == "0"):
            self.position.x -= 1

        return a
