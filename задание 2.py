# Шевякина Екатерина 44-22-122 задание 2
import math
import sys
import unittest


def main(*args):
    try:
        x = float(args[0][1])
        if x <= 1:
            return 1 / (x - 1)
        else:
            return 2 * math.sin ** 3 (x / 2)
    except:
        return "Произошла ошибка"

class SolverOfASystemOfEquationsTestCase(unittest.TestCase):
    def test_le(self):
        res = main(['...', 0.5])
        self.assertEqual(res, -0.12370454352734364)

    def test_r(self):
        res = main(['...', 0.9])
        self.assertEqual(res, 2.303504074299238)

    def test_error(self):
        res = main()
        self.assertEqual(res, "Произошла ошибка")