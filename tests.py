# assert 1 == 1
# assert "t" in "text"
# assert bool("digits")
#
# try:
#     assert 1 < 0
#
# except AssertionError:
#     print("Isn't right!")
############################################################
# def get_sum(a, b):
#     """
#     >>> get_sum(10, 3)
#     13
#     >>> get_sum(10, 3) * 2 - get_sum(-11, 0)
#     3
#     """
#
#     return a + b
#
#
# get_sum(1, 1)
#
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
############################################################
import unittest


def sum_digit(a, b):
    if a == 0:
        print(a * a)
        raise ValueError()
    else:
        return a + b


class TestSum(unittest.TestCase):
    def test_sorted(self):
        with self.assertRaises(ValueError):
            self.assertEqual(sum_digit(0, 2), 4)

        self.assertEqual(sum_digit(2, 4), 6)
        self.assertEqual(sum_digit(2, 2), 4)


class TestBuiltins(unittest.TestCase):
    def setUp(self):
        self.digit = 404 - 500 + 200

    def test_sorted(self):
        self.assertEqual(sorted([3, 2, 1]), [1, 2, 3])
        self.assertEqual(sorted([-13, 0, -27]), [-27, -13, 0])

    def test_str(self):
        self.assertEqual(str(self.digit), "104")
        self.assertEqual(str(None), "None")

    def test_int(self):
        self.assertEqual(int("0"), 0)
        self.assertEqual(int(True), 1)

        with self.assertRaises(ValueError):
            int("1.0")

    @unittest.skip("bcs test is not correct")  # .skipIf(), .skipUnless()
    def test_float(self):
        self.assertIsNone(self.digit)


if __name__ == '__main__':
    unittest.main()

