import unittest

def num_moves(n, x, y):

    if n == 0:
        return 0

    moves_possible = 0

    if x < n - 1 and y < n - 1:
        moves_possible += num_moves(n, x + 1, y) + num_moves(n, x, y + 1)
    else:
        return 1

    return moves_possible

class Tests(unittest.TestCase):
    def test_num_moves(self):
        answers = [ 0, 1, 2, 6 ]

        for i in range(0, 3):
            self.assertEqual(num_moves(i, 0, 0), answers[i])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
