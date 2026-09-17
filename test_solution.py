import unittest
from solution import Solution

class TestMaxAverage(unittest.TestCase):
    def test_example1(self):
        self.assertAlmostEqual(
            Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4), 12.75
        )

    def test_example2(self):
        self.assertEqual(Solution().findMaxAverage([5], 1), 5.0)

    def test_all_negative(self):
        self.assertAlmostEqual(
            Solution().findMaxAverage([-3, -1, -4, -2, -5], 3), -2.3333333333333335
        )

    def test_k_equals_n(self):
        self.assertEqual(Solution().findMaxAverage([10, 20, 30], 3), 20.0)

if __name__ == "__main__":
    unittest.main()
