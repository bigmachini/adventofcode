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
            if initial_sum < tmp_initial_sum:
                counter += 1
            initial_sum = tmp_initial_sum
        return counter


def advent_day_two_1(filename):
    with open(filename, 'r') as file:
        location = [0, 0]
        operations = {
            'forward': lambda x: location[0] + int(x),
            'down': lambda x: location[1] + int(x),
            'up': lambda x: location[1] - int(x),
        }
        lines = file.readlines()
        lines = [tuple(x.split()) for x in lines]
        for i in lines:
            if i[0] == 'forward':
                location[0] = operations[i[0]](i[1])
            else:
                location[1] = operations[i[0]](i[1])

        return int(location[0]) * int(location[1])


def advent_day_two_2(filename):
    def forward_movement(x, aim, location):
        location[0] += x
        location[1] += x * aim
        return location

    with open(filename, 'r') as file:
        aim = 0
        location = [0, 0]
        operations = {
            'forward': forward_movement,
            'down': lambda x: aim + x,
            'up': lambda x: aim - x,
        }
        lines = file.readlines()
        lines = [tuple(x.split()) for x in lines]
        for i in lines:
            if i[0] == 'forward':
                location = operations[i[0]](int(i[1]), aim, location)
            else:
                aim = operations[i[0]](int(i[1]))
        return int(location[0]) * int(location[1])


print('advent_day_two_2', advent_day_two_2('advent_day_two.txt'))


class TestAdventCode(unittest.TestCase):
    def test_day_one(self):
        self.assertEqual(7, advent_day_one_1('advent_day_one_test.txt'))
        self.assertEqual(5, advent_day_one_2('advent_day_one_test.txt'))
        self.assertEqual(150, advent_day_two_1('advent_day_two_test.txt'))
        self.assertEqual(900, advent_day_two_2('advent_day_two_test.txt'))


if __name__ == '__main__':
    unittest.main()
