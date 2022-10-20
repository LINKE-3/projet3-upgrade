import unittest
from extract_map import get_random_place, map_place
from models import McGyver
from controller import Controller
from view import View
import time
import pygame


class Testmap(unittest.TestCase):
    def setUp(self):
        self.map = [['1', '0', '1', '1'],
                    ['0', '0', '0', '0'],
                    ['1', '0', '1', '0']]
        self.map2 = [['1', '1', '1', '1'],
                     ['1', '0', '1', '0'],
                     ['1', '1', '1', '0']]
        self.map3 = [['1', '1', '1', '1', '1'],
                     ['1', '0', '0', '0', '1'],
                     ['1', '1', '1', '0', '1'],
                     ['1', '0', '0', '0', '1']]
        self.random = [[1, 0], [1, 1], [2, 1], [1, 2], [1, 3], [2, 3]]
        self.items = [[50, 100], [100, 50], [0, 50]]
        self.n = 4
        self.m = 3
        self.END_X = 3
        self.END_Y = 1
        self.lenx = 3
        self.leny = 4
        self.macgyver = McGyver(self.map)
        self.macgyver2 = McGyver(self.map2)
        self.macgyver3 = McGyver(self.map3)
        self.display_temps = View.display_temps(self)
        path = "ressource\\MacGyver.png"
        sizex = 5
        sizey = 5
        self.convert_image = View.convert_image(self, path, sizex, sizey)

    # read_map

    def test_map_place(self):
        expected_value = [[1, 0], [0, 1], [1, 1],
                          [2, 1], [1, 2], [1, 3], [2, 3]]
        self.assertEqual(map_place(self.map, self.n, self.m), expected_value)

    def test_get_random_place(self):
        expected_value = 3
        self.assertEqual(len(get_random_place(self.random)), expected_value)

    # move on flore
    def test_move_up(self):
        expected_value = 2
        self.macgyver.move("HAUT")
        self.assertEqual(self.macgyver.position.y, expected_value)

    def test_move_down(self):
        expected_value = 0
        self.macgyver.move("BAS")
        self.assertEqual(self.macgyver.position.y, expected_value)

    def test_move_right(self):
        expected_value = 2
        self.macgyver.move("DROITE")
        self.assertEqual(self.macgyver.position.x, expected_value)

    def test_move_left(self):
        expected_value = 0
        self.macgyver.move("GAUCHE")
        self.assertEqual(self.macgyver.position.x, expected_value)

    # don't move on wall
    def test_dont_move_up(self):
        expected_value = 1
        self.macgyver.move("HAUT")
        self.assertEqual(self.macgyver2.position.y, expected_value)

    def test_dont_move_down(self):
        expected_value = 1
        self.macgyver.move("BAS")
        self.assertEqual(self.macgyver2.position.y, expected_value)

    def test_dont_move_right(self):
        expected_value = 1
        self.macgyver.move("DROITE")
        self.assertEqual(self.macgyver2.position.x, expected_value)

    def test_dont_move_left(self):
        expected_value = 1
        self.macgyver.move("GAUCHE")
        self.assertEqual(self.macgyver2.position.x, expected_value)

    # get item
    def test_get_item(self):
        expected_value = 1
        self.macgyver.move("GAUCHE")
        Controller.game_loop2(self, self.items, self.macgyver)
        self.assertEqual(self.macgyver.items, expected_value)

    def test_dont_get_item(self):
        expected_value = 0
        self.macgyver.move("BAS")
        Controller.game_loop2(self, self.items, self.macgyver)
        self.assertEqual(self.macgyver.items, expected_value)

    # end condition
    def test_end_game_win(self):
        self.macgyver.items = 3
        self.macgyver.position.x = 3
        self.macgyver.position.y = 1
        expected_value = True
        self.assertEqual(Controller.end_conditions(self, self.macgyver),
                         self.winorlose, expected_value)

    def test_end_game_lose(self):
        self.macgyver.items = 2
        self.macgyver.position.x = 3
        self.macgyver.position.y = 1
        expected_value = False
        Controller.end_conditions(self, self.macgyver)
        self.assertEqual(self.winorlose, expected_value)

    def test_end_game_none(self):
        self.macgyver.items = 2
        self.macgyver.position.x = 1
        self.macgyver.position.y = 1
        expected_value = False
        Controller.end_conditions(self, self.macgyver)
        self.assertEqual(Controller.end_conditions(self, self.macgyver),
                         self.winorlose, expected_value)

    def test_end_game_advanced(self):
        self.macgyver.items = 2
        self.macgyver.position.x = 13
        self.macgyver.position.y = 1
        expected_value = True
        Controller.end_conditions(self, self.macgyver)
        self.assertEqual(Controller.end_conditions(self, self.macgyver),
                         expected_value)

    def test_end_game_advanced2(self):
        self.macgyver.items = 3
        self.macgyver.position.x = 13
        self.macgyver.position.y = 1
        expected_value = True
        Controller.end_conditions(self, self.macgyver)
        self.assertEqual(Controller.end_conditions(self, self.macgyver),
                         expected_value)

    # scénario tests fonctionnels
    def test_win(self):
        self.END_X = 3
        self.END_Y = 1
        self.macgyver3.items = 0
        self.macgyver3.position.x = 1
        self.macgyver3.position.y = 1
        self.items = [[50, 100], [100, 150], [150, 100]]
        self.macgyver3.move("HAUT")
        Controller.game_loop2(self, self.items, self.macgyver3)
        self.assertEqual(self.macgyver3.items, 1)
        self.macgyver3.move("HAUT")
        self.macgyver3.move("DROITE")
        Controller.game_loop2(self, self.items, self.macgyver3)
        self.assertEqual(self.macgyver3.items, 2)
        self.macgyver3.move("DROITE")
        self.macgyver3.move("BAS")
        Controller.game_loop2(self, self.items, self.macgyver3)
        self.assertEqual(self.macgyver3.items, 3)
        self.macgyver3.move("BAS")
        print(self.macgyver3.position.x, self.macgyver3.position.y)
        self.assertEqual(Controller.end_conditions(self, self.macgyver3),
                         False)
        first = 23
        second = 27
        third = 29
        self.seconds = 21
        expected_value = 21, 23, 27
        self.assertEqual(View.check_score(self, first, second, third),
                         expected_value)

    def test_loose(self):
        self.END_X = 3
        self.END_Y = 1
        self.macgyver3.items = 0
        self.macgyver3.position.x = 1
        self.macgyver3.position.y = 1
        self.items = [[50, 100], [150, 150], [150, 100]]
        self.macgyver3.move("HAUT")
        Controller.game_loop2(self, self.items, self.macgyver3)
        self.assertEqual(self.macgyver3.items, 1)
        self.macgyver3.move("HAUT")
        self.macgyver3.move("DROITE")
        Controller.game_loop2(self, self.items, self.macgyver3)
        self.assertEqual(self.macgyver3.items, 1)
        self.macgyver3.move("DROITE")
        self.macgyver3.move("BAS")
        Controller.game_loop2(self, self.items, self.macgyver3)
        self.assertEqual(self.macgyver3.items, 2)
        self.macgyver3.move("BAS")
        print(self.macgyver3.position.x, self.macgyver3.position.y)
        self.assertEqual(Controller.end_conditions(self, self.macgyver3),
                         self.winorlose, False)
        self.assertEqual(View.sauvegarde(self, self.winorlose), False)

    # chrono
    def test_lauch_chrono(self):
        stopchrono = False
        View.call_chrono(self, stopchrono)
        expected_value = True
        self.assertNotEqual(View.call_chrono(self, stopchrono), expected_value)

    def test_value_chrono(self):
        print(View.display_temps(self))
        stopchrono = False
        time.sleep(1.0)
        View.call_chrono(self, stopchrono)
        print(View.display_temps(self))
        expected_value = 1
        self.assertEqual(int(View.display_temps(self)), expected_value)

    def test_stop_lauch_chrono(self):
        stopchrono = False
        View.call_chrono(self, stopchrono)
        expected_value = False
        self.assertEqual(View.call_chrono(self, stopchrono), expected_value)

    # scoreboard
    def test_end_result_first(self):
        self.seconds = 9
        first = 10
        second = 15
        third = 20
        expected_value = 9, 10, 15
        self.assertEqual(View.check_score(self, first, second, third),
                         expected_value)

    def test_end_result_first1(self):
        self.seconds = 13
        first = 10
        second = 15
        third = 20
        expected_value = 10, 13, 15
        self.assertEqual(View.check_score(self, first, second, third),
                         expected_value)

    def test_end_result_first2(self):
        self.seconds = 18
        first = 10
        second = 15
        third = 20
        expected_value = 10, 15, 18
        self.assertEqual(View.check_score(self, first, second, third),
                         expected_value)

    # view
    def test_convert_image(self):
        expected_value = True
        path = "ressource\\MacGyver.png"
        self.assertEqual(View.convert_image(self, path, 0, 0),
                         expected_value)

    def test_wall_origine_display(self):
        expected_value = [[0, 0], [0, 2], [0, 3], [2, 0], [2, 2]]
        View.wall_ground_xy(self)
        self.assertEqual(self.wallxy, expected_value)

    def test_Floor_origine_display(self):
        expected_value = [[0, 1], [1, 0], [1, 1],
                          [1, 2], [1, 3], [2, 1], [2, 3]]
        View.wall_ground_xy(self)
        self.assertEqual(self.floorxy, expected_value)

    def test_init_window(self):
        expected_value = True
        self.assertEqual(View.init_window(self), expected_value)

    def test_key_pad_down(self):
        expected_value = 'BAS'
        xinput = 1073741906
        View.direction(self, xinput)
        self.assertEqual(View.direction(self, xinput), expected_value)

    def test_key_pad_up(self):
        expected_value = 'HAUT'
        xinput = 1073741905
        View.direction(self, xinput)
        self.assertEqual(View.direction(self, xinput), expected_value)

    def test_key_pad_right(self):
        expected_value = 'DROITE'
        xinput = 1073741903
        View.direction(self, xinput)
        self.assertEqual(View.direction(self, xinput), expected_value)

    def test_key_pad_left(self):
        expected_value = 'GAUCHE'
        xinput = 1073741904
        View.direction(self, xinput)
        self.assertEqual(View.direction(self, xinput), expected_value)

    def test_key_pad_esc(self):
        expected_value = False
        xinput = 27
        View.direction(self, xinput)
        self.assertEqual(View.direction(self, xinput), expected_value)

    def test_sauvegarde(self):
        expected_value = False
        wol = False
        self.assertEqual(View.sauvegarde(self, wol), expected_value)

    def test_display_text(self):
        expected_value = True
        position = "YOU WIN"
        window_resolution = (750, 750)
        self.window_surface = pygame.display.set_mode(window_resolution)
        imx = 300
        imy = 300
        x = 255
        y = 0
        z = 0
        self.assertEqual(View.display_text(self, position, imx, imy, x, y, z),
                         expected_value)


if __name__ == "__main__":
    unittest.main()
