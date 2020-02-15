import unittest

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
    rows = capacity+1
    cols = num_items+1
    K = [[0 for x in range(cols)] for y in range(rows)]

    # Build table K[][] in bottom up manner
    for cap in range(rows):
        for weight in range(cols):
            if cap == 0 or weight == 0:
                K[cap][weight] = 0
            elif item_weights[cap-1] <= weight:
                K[cap][weight] = max(item_values[cap-1] +
                                     K[cap-1][weight-item_weights[cap-1]],  K[cap-1][weight])
            else:
                K[cap][weight] = K[cap-1][weight]

    return K[num_items][capacity]


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(knapsack_dp(10, [1, 2, 3], [2, 3, 1], 3), 6)
        # TODO: Add more tests


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
