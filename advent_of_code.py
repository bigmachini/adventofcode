import unittest


def advent_day_one(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(int, lines))
        counter = 0
        for i in range(1, len(lines)):
            if lines[i - 1] < lines[i]:
                counter += 1
        return counter


class TestAdventCode(unittest.TestCase):
    def test_day_one(self):
        self.assertEqual(7, advent_day_one('advent_day_one_test.txt'))


if __name__ == '__main__':
    unittest.main()
