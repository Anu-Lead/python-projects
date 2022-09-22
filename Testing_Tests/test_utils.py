import unittest

from Testing_Tests.exceptions import MyCustomException
from . import utils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)  # add assertion here

    def test_add_func(self):
        """
        GIVEN:
        WHEN:
        THEN:


        """
        x = utils.adding_test(12, 8)
        self.assertEqual(20, x)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, 2)

    def test_that_add_throws_exception(self):
        # self.assertRaises(TypeError, utils.adding_test(15, '15'))

        with self.assertRaises(TypeError):
            utils.adding_test(45, '45')

        with self.assertRaises(MyCustomException):
            utils.adding_test(45, 45)


if __name__ == '__main__':
    unittest.main()
