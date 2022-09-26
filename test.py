import unittest
from extract_map import *
from models import *
from controller import *
from view import *
import time

class Testmap(unittest.TestCase):
    def setUp(self):
        self.map = [['1','0','1','1'], ['0','0','0','0'], ['1','0','1','0']]
        self.map2 = [['1','1','1','1'], ['1','0','1','0'], ['1','1','1','0']]
        self.random = [[1, 0], [1, 1], [2, 1], [1, 2], [1, 3], [2, 3]]
        self.items = [[50, 100], [100, 50], [0, 50]]
        self.n = 4
        self.m = 3
        self.macgyver = McGyver(self.map)
        self.macgyver2 = McGyver(self.map2)
        self.display_temps = View.display_temps(self)

        #self.controlall = Controller.game_loop2(self, self.items, self.macgyver)
        #self.control = Controller.game_loop2(self.macgyver)

    def test_map_place(self):
        expected_value = [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2], [1, 3], [2, 3]]
        self.assertEqual(map_place(self.map, self.n, self.m), expected_value)


    def test_get_random_place(self):
        expected_value = 3
        self.assertEqual(len(get_random_place(self.random)), expected_value)

    #move on flore
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

    #don't move on wall
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
    
    #get item
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

    #end condition
    def test_end_game_win(self):
        self.macgyver.items = 3
        self.macgyver.position.x = 13
        self.macgyver.position.y = 1        
        expected_value = True
        self.assertEqual(Controller.end_conditions(self, self.macgyver), self.winorlose, expected_value)

    def test_end_game_lose(self):
        self.macgyver.items = 2
        self.macgyver.position.x = 13
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
        self.assertEqual(Controller.end_conditions(self, self.macgyver), self.winorlose, expected_value)
    
    #chrono
    def test_lauch_chrono(self):
        stopchrono = 1
        View.call_chrono(self, stopchrono)
        expected_value = True
        self.assertNotEqual(View.call_chrono(self, stopchrono), expected_value)

    def test_value_chrono(self):
        print(View.display_temps(self))
        stopchrono = 1
        time.sleep(1.0)
        View.call_chrono(self, stopchrono)
        print(View.display_temps(self))
        expected_value = 1
        self.assertEqual(int(View.display_temps(self)), 1)

    def test_stop_lauch_chrono(self):
        stopchrono = 2
        View.call_chrono(self, stopchrono)
        expected_value = False
        self.assertEqual(View.call_chrono(self, stopchrono), expected_value)
    
    #scoreboard
    def test_end_result_first(self):
        self.seconds = 9
        first = 10
        second = 15
        third = 20
        expected_value = 9, 10, 15
        self.assertEqual(View.check_score(self, first, second, third), expected_value)

    def test_end_result_first(self):
        self.seconds = 13
        first = 10
        second = 15
        third = 20
        expected_value = 10, 13, 15
        self.assertEqual(View.check_score(self, first, second, third), expected_value)

    def test_end_result_first(self):
        self.seconds = 18
        first = 10
        second = 15
        third = 20
        expected_value = 10, 15, 18
        self.assertEqual(View.check_score(self, first, second, third), expected_value)


if __name__ == "__main__":
    unittest.main()
