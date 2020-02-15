# TODO: Import statements

######################### read from our list of zombie distances ########################
# TODO: open and read from Zombie.txt

# TODO: extract zombie data

####################### make a map of distances so we can see zombies ##################


def map_zombies(zombie_data):
    # TODO: Define the dimentions of our map

    # TODO: Put a ' ' as placeholders in our map

    # TODO: extract name and distance for the zombies
    # TODO: place a zombie emoji in each coordinate
    pass

################################ Implement the heap ####################################


def order_to_kill(zombie_data):
      # TODO: create empty heap and result lists

      # TODO: extract name and distance again
      # TODO: add the distance and zombie name to the heap

      # TODO get the zombies starting at the shortest distance

      # TODO: print out the map
      # TODO: print the result
    pass


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(order_to_kill(zombie_data), [
                         'A', 'C', 'B', 'H', 'D', 'I', 'J', 'K', 'F', 'E', 'G'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
