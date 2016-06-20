import mock
import unittest

from nasa import NasaRover


class TestDirection(unittest.TestCase):
    rover = NasaRover()
    rover.Xn, rover.Yn = 5, 5

    def test_left_valid(self):
        self.assertEqual('E', self.rover.direction('L', 'S'))

    def test_right_valid(self):
        self.assertEqual('N', self.rover.direction('R', 'W'))

    def test_invalid_dir(self):
        with self.assertRaises(ValueError):
            self.rover.direction('T', 'W')


class TestGetCoordinate(unittest.TestCase):
    rover = NasaRover()
    rover.Xn, rover.Yn = 5, 5

    def test_left_valid(self):
        self.assertEqual((1, 2, 'W'), self.rover.get_coordinate(1, 2, 'N', 'L'))

    def test_move_north(self):
        self.assertEqual((1, 3, 'N'), self.rover.get_coordinate(1, 2, 'N', 'M'))

    def test_move_south(self):
        self.assertEqual((1, 1, 'S'), self.rover.get_coordinate(1, 2, 'S', 'M'))

    def test_move_east(self):
        self.assertEqual((2, 2, 'E'), self.rover.get_coordinate(1, 2, 'E', 'M'))

    def test_move_west(self):
        self.assertEqual((0, 2, 'W'), self.rover.get_coordinate(1, 2, 'W', 'M'))

    def test_move_out_of_border(self):
        self.rover.Xn, self.rover.Yn = 5, 5
        with self.assertRaises(ValueError):
            self.rover.get_coordinate(6, 6, 'E', 'M')


class TestMain(unittest.TestCase):
    rover = NasaRover()
    rover.Xn, rover.Yn = 5, 5

    def test_main_valid(self):
        with mock.patch('__builtin__.raw_input',
                        side_effect=['5 5', '1 2 N', 'LMLMLMLMM',
                                     '3 3 E', 'MMRMMRMRRM', '\n']):
            r = self.rover.main()
            self.assertEqual(r, ['1 3 N', '5 1 E'])

    def test_main_invalid(self):
        with mock.patch('__builtin__.raw_input',
                        side_effect=['invalid_input', '1 2 N', 'LMLMLMLMM',
                                     '3 3 E', 'MMRMMRMRRM', '\n']):
            with self.assertRaises(ValueError):
                r = self.rover.main()
                print r
