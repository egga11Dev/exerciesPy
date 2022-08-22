import unittest


def plusNumber(numberOne, numberTwo):
    return numberOne + numberTwo


class TestCase(unittest.TestCase):

    def test_plus_of_two_numbers(self):
        numberOne = 10
        numberTwo = 5

        result = plusNumber(numberOne, numberTwo)

        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
