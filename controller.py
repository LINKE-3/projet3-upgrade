# TODO pour la semaine prochaine faire les liens entre la game loop et le front
from models import McGyver
from view import View
from extract_map import read_map
from constants import X_SIZE, Y_SIZE


class Controller:

    def __init__(self):
        self.view = View()
        self.mcGyver = McGyver(map=self.extract_map())
        self.items = []
        self.game_loop()
        return True

        # calls and initiates classes and methods

    def extract_map(self):
        map = read_map()
        return map

        # use the map extraction method here

    def game_loop(self):
        self.items = self.view.display(self.mcGyver)
        alpha = self.items
        beta = self.mcGyver
        stopchrono = True

        while True:
            input = self.view.play_game(stopchrono)
            if input:
                x = self.mcGyver.position.x
                y = self.mcGyver.position.y
                if self.mcGyver.move(input):
                    self.view.display_hero(self.mcGyver)
                    self.view.display_remove(x, y)

                self.game_loop2(alpha, beta)
                if self.end_conditions(self.mcGyver):
                    stopchrono = False
                    wol = self.winorlose
                    self.view.sauvegarde(wol)
                    self.view.score_board(wol)

    def game_loop2(self, alpha, beta):
        self.items = alpha
        self.mcGyver = beta
        for item in self.items:
            if item == [self.mcGyver.position.x*X_SIZE,
                        self.mcGyver.position.y*Y_SIZE]:
                self.mcGyver.items += 1
                self.items.remove(item)

    # make the calls to the view for display ex : self.view.display()
    # get the inputs self.view.handle_input()
    # collection of items
    # check the end condition

    def end_conditions(self, mcGyver):
        if (mcGyver.items == 3 and
            mcGyver.position.x == 13 and
                mcGyver.position.y == 1):
            self.winorlose = True
            print("you win")
            return True

        elif (mcGyver.items < 3 and
              mcGyver.position.x == 13 and
                mcGyver.position.y == 1):
            self.winorlose = False
            print("you lose")
            return True

        else:
            self.winorlose = False
            return False
        # check the end condition
