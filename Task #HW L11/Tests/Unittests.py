from Functianality import Functionality
import unittest
from unittest.mock import patch
from decimal import Decimal
from io import StringIO


class Test_Of_Inner_Functianality_Without_Console(unittest.TestCase):

    def test_of_exception_handler(self):
        self.assertEqual(None, Functionality.exception_handler(ValueError, 'Be Nice!'))

    def test_of_triangle_error(self):
        self.assertEqual('<class \'Exception\'>', str(Functionality.TriangleError(Exception)))

    def test_of_input_error(self):
        self.assertEqual('<class \'Exception\'>', str(Functionality.InputError(Exception)))

    def test_of_point_initiation_with_wrong_type_argument(self):
        with self.assertRaises(Functionality.InputError) as raised_exception:
            Functionality.Point('a', 1)
        self.assertEqual(raised_exception.exception.args[0], 'Coordinate should be number. Try again')

    def test_of_point_equal_operator_with_right_statement(self):
        self.assertEqual(True, Functionality.Point(1, 1) == Functionality.Point(1, 1))

    def test_of_point_equal_operator_with_wrong_statement(self):
        self.assertEqual(False, Functionality.Point(2, 1) == Functionality.Point(1, 1))

    def test_of_point_contanting_to_x(self):
        self.assertEqual(Decimal('1'), Functionality.Point(1, 1).x)

    def test_of_point_contanting_to_y(self):
        self.assertEqual(Decimal('2'), Functionality.Point(1, 2).y)

    def test_of_triangle_with_wrong_type_of_argument(self):
        with self.assertRaises(Functionality.TriangleError) as raised_exception:
            Functionality.Triangle(2, Functionality.Point(1, 1), Functionality.Point(2, 1))
        self.assertEqual(raised_exception.exception.args[0], 'Point should be instance of class Point')

    def test_of_triangle_with_points_on_one_line(self):
        with self.assertRaises(Functionality.TriangleError) as raised_exception:
            Functionality.Triangle(Functionality.Point(0, 0), Functionality.Point(1, 1), Functionality.Point(2, 2))
        self.assertEqual(raised_exception.exception.args[0], 'Points should not be located on the one line. Try again!')

    def test_of_triangle_with_equal_points(self):
        with self.assertRaises(Functionality.TriangleError) as raised_exception:
            Functionality.Triangle(Functionality.Point(1, 1), Functionality.Point(1, 1), Functionality.Point(2, 2))
        self.assertEqual(raised_exception.exception.args[0], 'Points should be different. Try again!')

    def test_of_triangle_contanting_to_point1(self):
        self.assertEqual(Functionality.Point(1, 1), Functionality.Triangle(Functionality.Point(1, 1),
                                                                           Functionality.Point(0, 2),
                                                                           Functionality.Point(3, 3)).point1)

    def test_of_triangle_contanting_to_point2(self):
        self.assertEqual(Functionality.Point(0, 2), Functionality.Triangle(Functionality.Point(1, 1),
                                                                           Functionality.Point(0, 2),
                                                                           Functionality.Point(3, 3)).point2)

    def test_of_triangle_contanting_to_point3(self):
        self.assertEqual(Functionality.Point(3, 3), Functionality.Triangle(Functionality.Point(1, 1),
                                                                           Functionality.Point(0, 2),
                                                                           Functionality.Point(3, 3)).point3)

    def test_of_triangle_length_of_side_with_wrong_type_argument(self):
        with self.assertRaises(Functionality.TriangleError) as raised_exception:
            Functionality.Triangle.length_of_side(2, Functionality.Point(1, 1))
        self.assertEqual(raised_exception.exception.args[0], 'Point should be instance of class Point')

    def test_of_triangle_length_of_side(self):
        self.assertEqual(Decimal('1'), Functionality.Triangle.length_of_side(Functionality.Point(0, 0),
                                                                             Functionality.Point(1, 0)))

    def test_of_triangle_perimeter_on_right_triangle(self):
        test_triangle = Functionality.Triangle(Functionality.Point(0, 0),
                                               Functionality.Point(0, 1),
                                               Functionality.Point(1, 0))

        self.assertEqual(Decimal('3.414213562373095145474621859'), test_triangle.perimeter())

    def test_of_triangle_perimeter_on_sharp_triangle(self):
        test_triangle = Functionality.Triangle(Functionality.Point(1, 2),
                                               Functionality.Point(2, 5),
                                               Functionality.Point(5, 2))

        self.assertEqual(Decimal('11.40491834728766429307711405'), test_triangle.perimeter())

    def test_of_triangle_perimeter_on_obtuse_triangle(self):
        test_triangle = Functionality.Triangle(Functionality.Point(1, 3),
                                               Functionality.Point(3, 5),
                                               Functionality.Point(9, 3))

        self.assertEqual(Decimal('17.15298244508294933652337022'), test_triangle.perimeter())

    def test_of_right_triangle_area(self):
        test_triangle = Functionality.Triangle(Functionality.Point(0, 0),
                                               Functionality.Point(0, 1),
                                               Functionality.Point(1, 0))
        self.assertEqual(Decimal('0.5'), test_triangle.area())

    def test_of_triangle_area_of_sharp_triangle(self):
        test_triangle = Functionality.Triangle(Functionality.Point(1, 2),
                                               Functionality.Point(2, 5),
                                               Functionality.Point(5, 2))

        self.assertEqual(Decimal('6'), test_triangle.area())

    def test_of_triangle_area_of_obtuse_triangle(self):
        test_triangle = Functionality.Triangle(Functionality.Point(1, 3),
                                               Functionality.Point(3, 5),
                                               Functionality.Point(9, 3))
        self.assertEqual(Decimal('8.0000000000000017763568394002504646778106689453125'), test_triangle.area())


class Test_Of_Inner_Functianality_Console_Only(unittest.TestCase):

    def pattern_for_positive_input_tests(self, given_answer, expected_out):
        with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
            Functionality.triangle_defining()
            self.assertEqual(fake_out.getvalue().strip(), expected_out)

    def pattern_for_negative_input_tests(self, given_answer, exception_type, exception_msg):
        with self.assertRaises(exception_type) as raised_exception:
            with patch('builtins.input', side_effect=given_answer), patch('sys.stdout', new=StringIO()) as fake_out:
                Functionality.triangle_defining()
        self.assertEqual(raised_exception.exception.args[0], exception_msg)

    def test_of_triangle_with_valid_data(self):
        self.pattern_for_positive_input_tests(['0 0', '1 0', '0 1'], 'If you read it, it means, '
                                                            'that you want to create some '
                                                            'Triangle and calculate his Area\n\n'
                                                            'You should input 3 coordinate pairs '
                                                            'for 3 Points\n'
                                                            'This triangle has area equal 0.5')

    def test_of_triangle_with_invalid_quantity_of_coordinates(self):
        self.pattern_for_negative_input_tests(['0 0 0', '1 0', '0 1'], Functionality.InputError,
                                             'You should input 2 numbers for coordinates. Try again!')

    def test_of_triangle_with_invalid_type_of_argument(self):
        self.pattern_for_negative_input_tests(['a 0', '1 0', '0 1'], Functionality.InputError,
                                             'Mistake happens! Coordinate should be '
                                             'a number! Please let try one more time')

    def test_of_triangle_input_3_points_on_line(self):
        self.pattern_for_negative_input_tests(['0 0', '1 1', '2 2'], Functionality.TriangleError,
                                             'Points should not be located on the one line. Try again!')

    def test_of_triangle_input_2_equal_points(self):
        self.pattern_for_negative_input_tests(['1 1', '1 1', '2 2'], Functionality.TriangleError,
                                             'Points should be different. Try again!')


if __name__ == '__main__':
    unittest.main()