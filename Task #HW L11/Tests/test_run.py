import unittest
from Tests import Unittests


def test_functionality():
    test_load = unittest.TestLoader()
    suites = test_load.loadTestsFromModule(Unittests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suites)


if __name__ == '__main__':
    pass
