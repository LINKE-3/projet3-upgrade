import pygame
from pygame.locals import*
from constants import X_SIZE, Y_SIZE
from extract_map import map, lieu
from pickle import *

pygame.init()

pygame.display.set_caption("Chrono")
fpsClock = pygame.time.Clock()
TpsZero = pygame.time.get_ticks()



class View: 
     ## Départ
    def __init__(self):
        self.init_window()

    def init_window(self):

        window_resolution = (750, 750)
        white_color = (255, 255, 255)
        self.window_surface = pygame.display.set_mode(window_resolution)
        self.window_surface.fill(white_color)
        pygame.display.flip()
        # initiate the pygame windows(size and background color)

    def display_temps(self):
        """
        Wall = pygame.image.load("ressource\\wall.png")
        Wall.convert()
        Wall = pygame.transform.scale(Wall, [Wall.get_width() - 25,
                                             Wall.get_height() - 22])
        self.window_surface.blit(Wall, [0, 0])
        self.window_surface.blit(Wall, [50, 0])
        self.window_surface.blit(Wall, [100, 0])
        """
        self.seconds = (pygame.time.get_ticks() - TpsZero) / 1000
        """
        police = pygame.font.SysFont("monospace" ,30)
        image_texte = police.render ( str(self.seconds), 1 , (255,0,0) )
        self.window_surface.blit(image_texte, (1, 1))
        pygame.display.flip()
        """
        return self.seconds

    def display_wall(self):
        Wall = pygame.image.load("ressource\\wall.png")
        Wall.convert()
        Wall = pygame.transform.scale(Wall, [Wall.get_width() - 25,
                                             Wall.get_height() - 22])
        for i in range(0, 15):
            for j in range(0, 15):
                if map[i][j] == '1':
                    self.window_surface.blit(Wall, [i*X_SIZE, j*Y_SIZE])
        pygame.display.flip()

        # wall read load and position

    def display_floor(self):
        Floor = pygame.image.load("ressource\\floor.png")
        Floor.convert()
        Floor = pygame.transform.scale(Floor, [Floor.get_width() - 31,
                                               Floor.get_height() - 32])
        for i in range(0, 15):
            for j in range(0, 15):
                if map[i][j] == '0':
                    self.window_surface.blit(Floor, [i*X_SIZE, j*Y_SIZE])

        pygame.display.flip()

        # floor read load and position

    def display_hero(self, mcgyver):
        MacGyver = pygame.image.load("ressource\\MacGyver.png")
        # load image
        MacGyver.convert()
        # convert l'image
        MacGyver = pygame.transform.scale(MacGyver,
                                          [MacGyver.get_width() + 10,
                                           MacGyver.get_height() + 7])
        # resize l'image
        self.window_surface.blit(MacGyver, [mcgyver.position.x*X_SIZE,
                                            mcgyver.position.y*Y_SIZE])
        pygame.display.flip()

        # hero read load and position

    def display_items(self):
        needle = pygame.image.load("ressource\\1.png")
        needle = pygame.transform.scale(needle, [needle.get_width() - 500,
                                                 needle.get_height() - 650])
        needle.convert()
        Ether = pygame.image.load("ressource\\2.png")
        Ether = pygame.transform.scale(Ether, [Ether.get_width() - 175,
                                               Ether.get_height() - 175])
        Ether.convert()
        syringe = pygame.image.load("ressource\\0.png")
        syringe = pygame.transform.scale(syringe, [syringe.get_width() - 40,
                                                   syringe.get_height() - 40])
        syringe.convert()
        self.window_surface.blit(needle, lieu[0])
        self.window_surface.blit(Ether, lieu[1])
        self.window_surface.blit(syringe, lieu[2])
        return lieu

        # items read load and position

    def arrive(self):
        black = pygame.image.load("ressource\\black.png")
        black = pygame.transform.scale(black, [black.get_width() - 10,
                                               black.get_height() - 10])
        black.convert()
        guardian = pygame.image.load("ressource\\guardian.png")
        guardian.convert()
        self.window_surface.blit(black, [13*X_SIZE, 1*Y_SIZE])
        self.window_surface.blit(guardian, [13*X_SIZE, 1*Y_SIZE])

        # arrive read load and position

    def display_remove(self, x, y):
        Floor = pygame.image.load("ressource\\floor.png")
        Floor.convert()
        Floor = pygame.transform.scale(Floor, [Floor.get_width() - 31,
                                               Floor.get_height() - 32])
        self.window_surface.blit(Floor, [x*X_SIZE, y*Y_SIZE])

        pygame.display.flip()

        # floor read load and position

    def display(self, mcgyver):

        self.display_floor()
        self.display_wall()
        self.display_hero(mcgyver)
        self.arrive()

        return self.display_items()

        # display sprite on the pygame window

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
                    if event.key == pygame.K_UP:
                        return"BAS"
                    elif event.key == pygame.K_DOWN:
                        return"HAUT"
                    elif event.key == pygame.K_RIGHT:
                        return"DROITE"
                    elif event.key == pygame.K_LEFT:
                        return"GAUCHE"
                    elif event.key == K_ESCAPE:
                        continuer = False
            self.call_chrono(stopchrono)
            Wall = pygame.image.load("ressource\\wall.png")
            Wall.convert()
            Wall = pygame.transform.scale(Wall, [Wall.get_width() - 25,
                                                 Wall.get_height() - 22])
            self.window_surface.blit(Wall, [0, 0])
            self.window_surface.blit(Wall, [50, 0])
            self.window_surface.blit(Wall, [100, 0])
            police = pygame.font.SysFont("monospace" ,30)
            image_texte = police.render ( str(self.seconds), 1 , (255,0,0) )
            self.window_surface.blit(image_texte, (1, 1))
            pygame.display.flip()



    def call_chrono(self, stopchrono):
        if stopchrono == 0:
            fpsClock.tick(60)
            self.display_temps()
            return True
        else:
            return False     

    def sauvegarde(self, wol):
        if wol == True:
            f = open ("db.py", "rb")
            first = load (f)
            second = load (f)
            third = load (f)
            f.close()
            self.check_score(first, second, third)


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

    def score_board(self, wol):
        first = self.one 
        second = self.two
        third = self.three
        f = open ("db.py","wb")
        dump(first,f)
        dump(second,f)
        dump(third,f)
        f.close() 
        white_color = (255, 255, 255)
        self.window_surface.fill(white_color)
        f = open ("db.py", "rb")
        first = load (f)
        second = load (f)
        third = load (f)

        police = pygame.font.SysFont("monospace" ,30)
        image_texte = police.render (str(self.seconds), 1 , (255,0,0) )
        self.window_surface.blit(image_texte, (300, 270))
        if wol == True:
            police = pygame.font.SysFont("monospace" ,30)
            image_texte = police.render ( "YOU WIN", 1 , (255,0,0) )
            self.window_surface.blit(image_texte, (300, 300))
        else :
            police = pygame.font.SysFont("monospace" ,30)
            image_texte = police.render ( "YOU LOSE", 1 , (255,0,0) )
            self.window_surface.blit(image_texte, (300, 300))

        police = pygame.font.SysFont("monospace" ,30)
        image_texte = police.render (str(first), 1 , (0,0,0) )
        image_texte2 = police.render ("first:", 1 , (0,0,0) )
        self.window_surface.blit(image_texte, (300, 360))
        self.window_surface.blit(image_texte2, (180, 360))

        police = pygame.font.SysFont("monospace" ,30)
        image_texte = police.render (str(second), 1 , (0,0,0) )
        image_texte2 = police.render ("second:", 1 , (0,0,0) )
        self.window_surface.blit(image_texte, (300, 390))
        self.window_surface.blit(image_texte2, (180, 390))

        police = pygame.font.SysFont("monospace" ,30)
        image_texte = police.render (str(third), 1 , (0,0,0) )
        image_texte2 = police.render ("third:", 1 , (0,0,0) )
        self.window_surface.blit(image_texte, (300, 420))
        self.window_surface.blit(image_texte2, (180, 420))

        pygame.display.flip()

        # takes player action
