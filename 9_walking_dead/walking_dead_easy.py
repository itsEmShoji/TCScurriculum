# BEGINNER SKELETON
# TODO: Import statements
from heapq import heappush, heappop

######################### read from our list of zombie distances ########################
f = open("Zombies.txt", "r")

if f.mode == 'r':
    content = f.read()

zombie_data = [s.split(' ') for s in content.split('\n') if s != '']

####################### make a map of distances so we can see zombies ##################


def map_zombies(zombie_data):
    # TODO: Define the dimensions of our map

    map = [[' ' for x in range(length)] for y in range(width)]

    # TODO: Make our for loop
    # TODO: extract name and distance for the zombies
    map[int(distance)-1][i] = u'\U0001F9DF' + ' ' + name

    print('\n closest -------------------------------------------> furthest')
    for row in zip(*map):
        print(" ".join(row))

################################ Implement the heap ####################################


def order_to_kill(zombie_data):
    # TODO: create empty heap and result lists

    for zombie_idx in range(len(zombie_data)):
        # TODO: extract name and distance again
        # TODO: add the distance and zombie name to the heap

    while heap:
        # TODO get the zombies starting at the shortest distance

    return result

# TODO: print the zombie map and result using the methods defined above

######### Testing #######


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(order_to_kill(zombie_data), [
                         'A', 'C', 'B', 'H', 'D', 'I', 'J', 'K', 'F', 'E', 'G'])
    # TODO: Add more tests


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
