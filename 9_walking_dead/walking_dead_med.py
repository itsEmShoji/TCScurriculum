# INTERMEDIATE SKELETON
# TODO: Import statements

######################### read from our list of zombie distances ########################

# TODO: open Zombies.txt

# TODO: Open and extract the contents from Zombies.txt

zombie_data = [s.split(' ') for s in content.split('\n') if s != '']

####################### make a map of distances so we can see zombies ##################


def map_zombies(zombie_data):
    # TODO: Define the dimensions of our map

    map = [[' ' for x in range(length)] for y in range(width)]

    for i in range(len(zombie_data)):
        # TODO: extract name and distance for the zombies
        map[int(distance)-1][i] = u'\U0001F9DF' + ' ' + name

    print('\n closest -------------------------------------------> furthest')
    # TODO: Print the map

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
