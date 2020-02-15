######## COMPLETE WalkingDead.py ############

import unittest
from heapq import heappush, heappop

######################### read from our list of zombie distances ########################
f = open("Zombies.txt", "r")

if f.mode == 'r':
    content = f.read()

# turn the distances into a list of ints
zombie_data = [s.split(' ') for s in content.split('\n') if s != '']

####################### make a map of distances so we can see zombies ##################


def map_zombies(zombie_data):
    length = len(zombie_data)
    width = max([int(zombie[1]) for zombie in zombie_data])

    map = [[' ' for x in range(length)] for y in range(width)]

    for i in range(len(zombie_data)):
        name, distance = zombie_data[i]
        map[int(distance)-1][i] = u'\U0001F9DF' + ' ' + name

    print('\n closest -------------------------------------------> furthest')
    for row in zip(*map):
        print(" ".join(row))

################################ Implement the heap ####################################


def order_to_kill(zombie_data):
    heap = []
    result = []

    for zombie_idx in range(len(zombie_data)):
        name, distance = zombie_data[zombie_idx]
        heappush(heap, (distance, name))

    while heap:
        result.append(heappop(heap)[1])

    return result


map_zombies(zombie_data)
print('\nto survive, kill the zombies in this order: ' +
      ', '.join(order_to_kill(zombie_data)))


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(order_to_kill(zombie_data), [
                         'A', 'C', 'B', 'H', 'D', 'I', 'J', 'K', 'F', 'E', 'G'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
