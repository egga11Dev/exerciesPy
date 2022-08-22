import unittest
from unittest import result


def adult(age):
    if age >= 18:
        return True
    else:
        return False


class testCrystal(unittest.TestCase):

    def testAdult(self):
        age = 20

        resultAge = adult(age)
        self.assertEqual(resultAge, True)

    def testYounger(self):
        age = 17

        resultAge = adult(age)
        self.assertEqual(resultAge, False)


if __name__ == '__main__':
    unittest.main()
