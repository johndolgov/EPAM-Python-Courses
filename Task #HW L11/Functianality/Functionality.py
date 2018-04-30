"""
Triangle area calculating module.
This module define to classes Point and Triangle
and function which create 3 Point and Triangle on it.
Also in this module define two classes InputError and TriangleError.
This module calculate area of Triangle

>>> Triangle(Point(0,0), Point(1,0), Point(0,1)).area()
Decimal('0.5')
>>> Triangle.length_of_side('a', Point(1,0))
Traceback (most recent call last):
...
TriangleError: Point should be instance of class Point

"""
from numbers import Number
from decimal import Decimal
from math import sqrt
import sys
import doctest


def exception_handler(type,exception,traceback = 0):
    """
    This function hide traceback of Exception, because
    a long traceback scares user

    :param type: Type of Exception
    :param exception: Exception
    :param traceback: Traceback of Exception
    :return: str with name of Exception

    >>> exception_handler(ValueError, 'Be nice!')
    Be nice!
    """
    print(f'{exception}')


# Use excepthook for hiding traceback of exception
sys.excepthook = exception_handler


class TriangleError(Exception):

    """Class which define Error in the triangle defenition
    >>> TriangleError(Exception)
    TriangleError(<class 'Exception'>,)

    """

    pass


class InputError(Exception):

    """Class which define Error in the input
    >>> InputError(Exception)
    InputError(<class 'Exception'>,)
    """

    pass


class Point:
    """
    Class which defined point in 2D

    >>> Point('a',1)
    Traceback (most recent call last):
    ...
    InputError: Coordinate should be number. Try again
    >>> Point(1,1,1)
    Traceback (most recent call last):
    ...
    TypeError: __init__() takes 3 positional arguments but 4 were given
    >>> Point(1,1) == Point(1,1)
    True
    >>> Point(1,1) == Point(2,1)
    False
    """

    def __init__(self, x, y):

        """
        Constructor of class Point

        :param x:
        :type instance of class Number
        :param y:
        :type instance of class Number

        >>> Point('a',1)
        Traceback (most recent call last):
         ...
        InputError: Coordinate should be number. Try again
        >>> Point(1,1,1)
        Traceback (most recent call last):
        ...
        TypeError: __init__() takes 3 positional arguments but 4 were given
        """
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise InputError('Coordinate should be number. Try again')
        else:
            self.x = Decimal(x)
            self.y = Decimal(y)

    def __eq__(self, other):

        """
        Overloading operator == for instance of class Point

        :param other:

        :return: bool

        >>> Point(1,1) == Point(1,1)
        True
        >>> Point(1,1) == Point(2,1)
        False
        """

        return (self.x == other.x) and (self.y == other.y)


class Triangle:
    """
    Class which defines triangle

    >>> Triangle([1,1], Point(1,1), Point(2,2))
    Traceback (most recent call last):
    ...
    TriangleError: Point should be instance of class Point
    >>> Triangle(Point(1,1), Point(2,2), Point(1,1))
    Traceback (most recent call last):
    ...
    TriangleError: Points should be different. Try again!
    >>> Triangle(Point(0,0), Point(1,1), Point(2,2))
    Traceback (most recent call last):
    ...
    TriangleError: Points should not be located on the one line. Try again!
    >>> Triangle(Point(0,0),Point(2,1),Point(1,2),Point(3,5))
    Traceback (most recent call last):
    ...
    TypeError: __init__() takes 4 positional arguments but 5 were given
    >>> Triangle(Point(0,0), Point(1,0), Point(0,1)).perimeter()
    Decimal('3.414213562373095145474621859')
    >>> Triangle(Point(0,0), Point(1,0), Point(0,1)).area()
    Decimal('0.5')
    >>> Triangle(Point('a',0), Point(1,0), Point(0,1)).perimeter()
    Traceback (most recent call last):
    ...
    InputError: Coordinate should be number. Try again
    >>> Triangle(1, Point(1,0), Point(0,1)).perimeter()
    Traceback (most recent call last):
    ...
    TriangleError: Point should be instance of class Point
    >>> Triangle(Point('a',0), Point(1,0), Point(0,1)).area()
    Traceback (most recent call last):
    ...
    InputError: Coordinate should be number. Try again
    >>> Triangle(1, Point(1,0), Point(0,1)).area()
    Traceback (most recent call last):
    ...
    TriangleError: Point should be instance of class Point
    >>> Triangle.length_of_side(Point(0,0), Point(1,0))
    Decimal('1')
    >>> Triangle.length_of_side('a', Point(1,0))
    Traceback (most recent call last):
    ...
    TriangleError: Point should be instance of class Point
    """

    def __init__(self, point_1, point_2, point_3):

        """
        Constructor of class Triangle

        :param point_1:
        :type: Point
        :param point_2:
        :type: Point
        :param point_3:
        :type: Point

        >>> Triangle([1,1], Point(1,1), Point(2,2))
        Traceback (most recent call last):
        ...
        TriangleError: Point should be instance of class Point
        >>> Triangle(Point(1,1), Point(2,2), Point(1,1))
        Traceback (most recent call last):
        ...
        TriangleError: Points should be different. Try again!
        >>> Triangle(Point(0,0), Point(1,1), Point(2,2))
        Traceback (most recent call last):
        ...
        TriangleError: Points should not be located on the one line. Try again!

        """

        if not isinstance(point_1, Point) or not isinstance(point_2, Point) or not isinstance(point_3, Point):
            raise TriangleError('Point should be instance of class Point')

        elif point_1 == point_2 or point_1 == point_3 or point_2 == point_3:
            raise TriangleError('Points should be different. Try again!')

        elif ((point_1.y * point_2.x - point_2.y * point_1.x)
              + point_3.x * (point_2.y - point_1.y) == point_3.y * (point_2.x - point_1.x)):
            raise TriangleError('Points should not be located on the one line. Try again!')

        else:
            self.point1 = point_1
            self.point2 = point_2
            self.point3 = point_3

    @staticmethod
    def length_of_side(p1, p2):
        """

        Static method for calculating length of the side of triangle using
        two Point coordinate

        :param p1:
        :type:  Point
        :param p2:
        :type: Point

        :return: Decimal -- length of side

         >>> Triangle.length_of_side(Point(0,0), Point(1,0))
         Decimal('1')
        """
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TriangleError('Point should be instance of class Point')
        return Decimal(sqrt((p2.y - p1.y)**2 + (p2.x - p1.x)**2))

    def perimeter(self):

        """
        Method which calculate perimeter of triangle

        :return: Decimal -- perimeter of Triangle

        >>> Triangle(Point(0,0), Point(1,0), Point(0,1)).perimeter()
        Decimal('3.414213562373095145474621859')
        """
        return Decimal(self.length_of_side(self.point1, self.point2) \
               + self.length_of_side(self.point1, self.point3) \
               + self.length_of_side(self.point2, self.point3))

    def area(self):
        """
        Method which calculate area of triangle using Heron's formula

        :return: Decimal -- area of the triangle

        >>> Triangle(Point(0,0), Point(1,0), Point(0,1)).area()
        Decimal('0.5')
        """
        p = self.perimeter()/2
        s = Decimal(sqrt(p * (p - self.length_of_side(self.point1, self.point2))
                 * (p - self.length_of_side(self.point1, self.point3))
                 * (p - self.length_of_side(self.point2, self.point3))))
        return Decimal(s)


def get_input(text):
    return input(text)


def triangle_defining():
    """
    This function define Triangle using 3 Point
    and calculate area of the Triangle using method of Triangle object

    :return: area
    :type: Decimal

    """
    print('If you read it, it means, that you want to create some Triangle and calculate his Area''\n')
    print('You should input 3 coordinate pairs for 3 Points')
    point_list = []
    for i in range(3):
        try:
            coordinates = list(map(float, get_input(f'Please input X, Y coordinates for {i+1} Point: ').split()))

        except ValueError:
            raise InputError('Mistake happens! Coordinate should be a number! Please let try one more time')

        if len(coordinates) != 2:
            raise InputError('You should input 2 numbers for coordinates. Try again!')
        point = Point(coordinates[0], coordinates[1])
        point_list.append(point)
    triangle = Triangle(point_list[0], point_list[1], point_list[2])
    print(f'This triangle has area equal {triangle.area()}')


if __name__ == '__main__': # pragma: no cover
    doctest.testmod()
