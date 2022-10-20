import pygame
from constants import X_SIZE, Y_SIZE, list
from extract_map import map, lieu
from pickle import load, dump

pygame.init()

pygame.display.set_caption("Chrono")
fpsClock = pygame.time.Clock()
TpsZero = pygame.time.get_ticks()


class View:

    def __init__(self):
        self.init_window()

    def init_window(self):
        window_resolution = (750, 750)
        self.white_color = (255, 255, 255)
        self.window_surface = pygame.display.set_mode(window_resolution)
        self.window_surface.fill(self.white_color)
        self.map = map
        self.lenx = 15
        self.leny = 15
        pygame.display.flip()

        return True
        # initiate the pygame windows(size and background color)

    def display_temps(self):
        self.seconds = (pygame.time.get_ticks() - TpsZero) / 1000
        return self.seconds

    def wall_ground_xy(self):
        self.wallxy = []
        self.floorxy = []
        for i in range(0, self.lenx):
            for j in range(0, self.leny):
                if self.map[i][j] == '1':
                    self.wallxy.append([i, j])
                else:
                    self.floorxy.append([i, j])

    def display_all(self):
        self.convert_image("ressource\\wall.png", - 25, - 22)
        for x in range(0, len(self.wallxy)):
            self.window_surface.blit(self.name, [self.wallxy[x][0]*X_SIZE,
                                                 self.wallxy[x][1]*Y_SIZE])

        self.convert_image("ressource\\floor.png", - 31, - 32)
        for x in range(0, len(self.floorxy)):
            self.window_surface.blit(self.name, [self.floorxy[x][0]*X_SIZE,
                                                 self.floorxy[x][1]*Y_SIZE])

        for x in list:
            self.convert_image(x[0], x[1], x[2])
            self.window_surface.blit(self.name, x[3])

        return lieu

        # wall read load and position

    def convert_image(self, path, sx, sy):
        self.name = pygame.image.load(path)
        self.name = pygame.transform.scale(self.name,
                                           [self.name.get_width() + sx,
                                            self.name.get_height() + sy])
        return True

    def display_hero(self, mcgyver):
        self.convert_image("ressource\\MacGyver.png", 10, 7)
        self.window_surface.blit(self.name, [mcgyver.position.x*X_SIZE,
                                             mcgyver.position.y*Y_SIZE])

    def display_remove(self, x, y):
        self.convert_image("ressource\\floor.png", - 31, - 32)
        self.window_surface.blit(self.name, [x*X_SIZE, y*Y_SIZE])

    def display(self, mcgyver):
        self.wall_ground_xy()
        return self.display_all()
        self.display_hero(mcgyver)

    def stop_game(self):
        pygame.quit()

        # close pygame window

    def play_game(self, stopchrono):
        pygame.init()
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    xtouche = event.key
                    direc = self.direction(xtouche)
                    return direc

            self.call_chrono(stopchrono)
            self.convert_image("ressource\\black.png", 25, -25)
            self.window_surface.blit(self.name, [0, 0])
            self.display_text(str(self.seconds), 1, 1, 255, 0, 0)
            pygame.display.flip()

    def direction(self, xtouche):
        if xtouche == pygame.K_UP:
            print(xtouche)
            return "BAS"
        elif xtouche == pygame.K_DOWN:
            return "HAUT"
        elif xtouche == pygame.K_RIGHT:
            return "DROITE"
        elif xtouche == pygame.K_LEFT:
            return "GAUCHE"
        elif xtouche == pygame.K_ESCAPE:
            continuer = False
            return continuer

    def call_chrono(self, stopchrono):
        if stopchrono:
            fpsClock.tick(60)
            self.display_temps()
            return True
        else:
            return False

    def sauvegarde(self, wol):
        if wol:
            f = open("db.py", "rb")
            first = load(f)
            second = load(f)
            third = load(f)
            f.close()
            self.check_score(first, second, third)
        else:
            return False

    def check_score(self, first, second, third):
        newscore = self.seconds
        if newscore <= first or first == 0:
            third = second
            second = first
            first = newscore
        elif newscore <= second or second == 0:
            third = second
            second = newscore
        elif newscore <= third or third == 0:
            third = newscore
        self.one = first
        self.two = second
        self.three = third
        return first, second, third

    def display_text(self, position, imx, imy, x, y, z):
        police = pygame.font.SysFont("monospace", 30)
        image_texte = police.render(position, 1, (x, y, z))
        self.window_surface.blit(image_texte, (imx, imy))
        return True

    def score_board(self, wol):
        first = self.one
        second = self.two
        third = self.three
        f = open("db.py", "wb")
        dump(first, f)
        dump(second, f)
        dump(third, f)
        f.close()
        self.window_surface.fill(self.white_color)
        f = open("db.py", "rb")
        first = load(f)
        second = load(f)
        third = load(f)
        self.display_text(str(self.seconds), 300, 270, 255, 0, 0)
        if wol:
            self.display_text("YOU WIN", 300, 300, 255, 0, 0)
        else:
            self.display_text("YOU LOSE", 300, 300, 255, 0, 0)

        list2 = [[str(first), 300, 360, 0, 0, 0],
                 ["first:", 180, 360, 0, 0, 0],
                 [str(second), 300, 390, 0, 0, 0],
                 ["second:", 180, 390, 0, 0, 0],
                 [str(third), 300, 420, 0, 0, 0],
                 ["third:", 180, 420, 0, 0, 0]]

        for x in list2:
            self.display_text(x[0], x[1], x[2], x[3], x[4], x[5])

        pygame.display.flip()
