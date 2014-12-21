import unittest

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

class FibTests(unittest.TestCase):
    def test_fib(self):
        fib_vals = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        for i, v in enumerate(fib_vals):
            y = fib(i + 1)
            self.assertEqual(y, v, "i = %s, v = %s, fib(i + 1) = %s" % (i, v, y))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FibTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
