import math
import unittest


def f(x):
    return math.e ** x + x - 3


def MPD(f, a, b, eps=1e-5):
    while abs(b - a) > eps:
        x = (a + b) / 2.0
        fx = f(x)
        fa = f(a)
        if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
            a = x
        else:
            b = x
    return x


x = MPD(f, 5, 1)
print(x)
print(f(x))



class DillutionTest(unittest.TestCase):
    def test_x(self):
        res = MPD(f,5,1)
        self.assertEqual(res, 1.0000076293945312)
    def test_f(self):
        res = f(1.0000076293945312)
        self.assertEqual(res, 0.7183172054)


if __name__ == '__main__':
    unittest.main()
