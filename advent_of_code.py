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


from collections import Counter


def get_max(data):
    if data['0'] > data['1']:
        return '0'
    else:
        return '1'


def get_min(data):
    if data['0'] > data['1']:
        return '1'
    else:
        return '0'


def get_oxygen(bit, position, lines):
    tmp = []
    for i in lines:
        i = i.strip()
        if i[position] == bit:
            tmp.append(i)
    return tmp


def advent_day_three_1(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        bits = [[] for x in lines[0].strip()]
        bits_count = []
        for i in range(len(lines)):
            line = lines[i].strip()
            for index, value in enumerate(line):
                bits[index].append(value)

        for i in bits:
            bits_count.append(Counter(i))

        gamma = ''.join([get_max(x) for x in bits_count])
        epsilon = ''.join([get_min(x) for x in bits_count])
        return int(gamma, 2) * int(epsilon, 2)


def advent_day_three_2(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        tmp, index = list(lines), 0
        while len(tmp) > 1:
            bits = [[] for x in tmp[0].strip()]
            for i in range(len(tmp)):
                line = tmp[i].strip()
                for _index, value in enumerate(line):
                    bits[_index].append(value)

            bits_count = Counter(bits[index])

            if bits_count['0'] == bits_count['1'] or bits_count['0'] < bits_count['1']:
                _bit = '1'
            else:
                _bit = '0'

            tmp = get_oxygen(_bit, index, tmp)

            index += 1

        oxygen = ''.join(tmp)
        tmp, index = list(lines), 0
        while len(tmp) > 1:
            bits = [[] for x in tmp[0].strip()]
            for i in range(len(tmp)):
                line = tmp[i].strip()
                for _index, value in enumerate(line):
                    bits[_index].append(value)

            bits_count = Counter(bits[index])

            if bits_count['0'] == bits_count['1'] or bits_count['0'] < bits_count['1']:
                _bit = '0'
            else:
                _bit = '1'

            tmp = get_oxygen(_bit, index, tmp)

            index += 1

        co_2 = ''.join(tmp)
        print('co_2', co_2)

        return int(oxygen, 2) * int(co_2, 2)

print('advent_day_three_2', advent_day_three_2('advent_day_three.txt'))
class TestAdventCode(unittest.TestCase):
    def test_day_one(self):
        self.assertEqual(7, advent_day_one_1('advent_day_one_test.txt'))
        self.assertEqual(5, advent_day_one_2('advent_day_one_test.txt'))
        self.assertEqual(150, advent_day_two_1('advent_day_two_test.txt'))
        self.assertEqual(900, advent_day_two_2('advent_day_two_test.txt'))
        self.assertEqual(198, advent_day_three_1('advent_day_three_test.txt'))
        self.assertEqual(230, advent_day_three_2('advent_day_three_test.txt'))


if __name__ == '__main__':
    unittest.main()
