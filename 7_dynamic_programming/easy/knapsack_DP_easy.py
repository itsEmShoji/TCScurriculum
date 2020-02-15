# TODO: imports

# REQUIRES: num_items >= 0, capacity >= 0,
#     	 size of item_values >= num_items,
#     	 size of item_weights >= num_items,
#     	 item_values are all >= 0, item_weights are all >= 0
# EFFECTS: Computes the max value that can be obtained by picking
#	 	 from a set of num_items items without exceeding the given
#	 	 capacity. Choosing item i produces the value item_values[i]
#	 	 but uses weight item_weights[i] out of the available
#	 	 capacity.
#	Must use dynamic programming!


def knapsack_dp(capacity, item_weights, item_values, num_items):
    # TODO: declare rows and columns
     K = [[0 for x in range(cols)] for y in range(rows)]

    # Build table K[][] in bottom up manner
    # TODO: loop through items
    # TODO: second loop through weights upto capacity
    # TODO: if statement
    # TODO: set item and weight to 0
    # TODO: if item weights[item-1] is less than weight
    K[cap][weight] = max(item_values[cap-1] +
                         K[cap-1][weight-item_weights[cap-1]],  K[cap-1][weight])
    # TODO: else
    # TODO: set k[item][weight] to previously found answer

    # TODO: return K at num_items and capacity


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(knapsack_dp(0, [], [], 0), 0)
        # TODO: Add more tests


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
