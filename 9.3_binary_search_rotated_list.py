import unittest

def binary_search_rotated(a_list, low, high, n):
    mid = (high + low) / 2

    if a_list[low] < a_list[high] or low == high:
        if a_list[low] > n or a_list[high] < n:
            return None
        else:
            return binary_search(a_list, low, high, n)
    else:
        l = binary_search_rotated(a_list, low, mid, n)
        if l != None:
            return l
        else:
            return binary_search_rotated(a_list, mid + 1, high, n)

def binary_search(a_list, low, high, n):
    mid = (high + low) / 2

    if high < low:
        return None
    else:
        if a_list[mid] < n:
            return binary_search(a_list, mid + 1, high, n)
        elif a_list[mid] > n:
            return binary_search(a_list, low, mid - 1, n)
        else:
            return mid

class Tests(unittest.TestCase):
    def test_binary_search_rotated(self):
        a_list = range(1000)
        a_list = a_list[400:] + a_list[:400]

        #test every number in the array for kicks
        for i in xrange(1000):
            found_index = binary_search_rotated(a_list, 0, len(a_list) - 1, i)
            self.assertEqual(a_list[found_index], i)

    def test_repeated_numbers(self):
        a_list = [ 6, 6, 6, 6, 0, 6, 6 ]

        i = binary_search_rotated(a_list, 0, len(a_list) - 1, 0)
        self.assertEqual(a_list[i], 0)

    def test_binary_search(self):
        a_list = range(1000)

        #test every number in the array for kicks
        for i in xrange(0, 1000, 2):
            found_index = binary_search(a_list, 0, len(a_list) - 1, i)
            self.assertEqual(a_list[found_index], i)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)
