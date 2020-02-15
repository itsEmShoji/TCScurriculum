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
#	Must use recursion!


def knapSack(capacity, item_weights, item_values, num_items):
    # Base Case
    if num_items == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than the capacity,
    # then this item cannot be included in the optimal solution
    if (item_weights[num_items-1] > capacity):
        return knapSack(capacity, item_weights, item_values,
                        num_items-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(item_values[num_items-1] +
                   knapSack(capacity-item_weights[num_items-1],
                            item_weights, item_values, num_items-1),
                   knapSack(capacity, item_weights, item_values,
                            num_items-1))


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(knapSack(0, [], [], 0), 0)
        # TODO: Add more tests


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
