import shlex
import unittest


def advent_day_one_1(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(int, lines))
        counter = 0
        for i in range(1, len(lines)):
            if lines[i - 1] < lines[i]:
                counter += 1
        return counter


def advent_day_one_2(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = list(map(int, lines))
        counter = 0
        initial_sum = sum(lines[:3])
        for i in range(3, len(lines)):
            tmp_initial_sum = initial_sum + lines[i] - lines[i - 3]
            print(initial_sum, tmp_initial_sum)
            if initial_sum < tmp_initial_sum:
                counter += 1
            initial_sum = tmp_initial_sum
        return counter


def advent_day_two_1(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [tuple(x.split()) for x in lines]
        print(lines[0])

advent_day_two_1('advent_day_two_test.txt')

class TestAdventCode(unittest.TestCase):
    def test_day_one(self):
        self.assertEqual(7, advent_day_one_1('advent_day_one_test.txt'))
        self.assertEqual(5, advent_day_one_2('advent_day_one_test.txt'))


if __name__ == '__main__':
    unittest.main()
