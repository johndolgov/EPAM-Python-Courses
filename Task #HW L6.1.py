import abc
from decimal import Decimal
from numbers import Number

class CurrencyDescriptor(object):
    """Discriptor which creates dict of  courses"""

    def __init__(self):
        self.value = {}

    def __get__(self, instance, owner):
        def course(class_name):
            return (self.value[type(instance).__name__]/self.value[class_name.__name__])
        return course

    def __set__(self, instance, value):
        if not isinstance(value,Number):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.value[type(instance).__name__] = Decimal(value)

class Currency(metaclass=abc.ABCMeta):
    """Abstract class Currency
    creates general operations with money
    """

    course = CurrencyDescriptor()

    def __init__(self,value):
        if not isinstance(value, Number):
            raise TypeError
        self.value = Decimal(value)
        self.course = self.initial_course()

    def to(self,class_name):
        """Convert one currency to another"""

        return class_name(self.course(class_name)*self.value)

    def __eq__(self, other):
        return self.value == other.to(type(self)).value

    def __ne__(self, other):
        return self.value != other.to(type(self)).value

    def __gt__(self, other):
        return self.value > other.to(type(self)).value

    def __lt__(self, other):
        return self.value < other.to(type(self)).value

    def __ge__(self, other):
        return self.value >= other.to(type(self)).value

    def __le__(self, other):
        return self.value <= other.to(type(self)).value

    def __add__(self, other):
        return type(self)(self.value + other.to(type(self)).value)

    def __mul__(self, other):
        return type(self)(self.value*Decimal(other))

    def __sub__(self, other):
        return type(self)(self.value - other)

    def __truediv__(self, other):
        return type(self)(self.value / other)

    def __radd__(self, other):
        return type(self)(other + self.value)

    def __rmul__(self, other):
        return type(self)(self.value * other)

    def __str__(self):
        return '{} {}'.format(self.value, self.symbol())


    @abc.abstractmethod
    def initial_course(self):
        pass

    @abc.abstractmethod
    def symbol(self):
        pass

class Dollar(Currency):
    """Class Dollar"""

    def __init__(self,value):
        super(Dollar,self).__init__(value)

    def initial_course(self):
        return 1

    def symbol(self):
        return '$'

class Euro(Currency):
    """Class Euro"""

    def __init__(self,value):
        super(Euro,self).__init__(value)

    def initial_course(self):
        return 2

    def symbol(self):
        return '€'
class Rubble(Currency):
    """Class Rubble"""

    def __init__(self,value):
        super(Rubble,self).__init__(value)

    def initial_course(self):
        return 60

    def symbol(self):
        return '₽'

if __name__ == '__main__':
    e = Euro(5)
    m = Dollar(3)
    print(e)
    b = e+m
    print(b)
    print(e > Euro(6))
    print(e.to(Dollar))
    g = e*2
    print(g)
    k = e/2
    print(k)
    print(e.course(Dollar))
    r = sum([Euro(i) for i in range(5)])
    print(r)





