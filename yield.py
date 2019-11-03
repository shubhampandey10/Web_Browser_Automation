"""Yield program

Make a function which takes parameter and "yield" the result of expression:   (num)+(56/90)+(98-100)/(10000*200)
Map the function with below list : [50000,63000,80001,7002,67890]
"""

import unittest


# It's not very clear how to use yield for this qustion, I have tried using in
# two ways below. Using unittest cases to demonstrate the functionality.


def calculate(numbers):
    """This takes list of numbers and yields their results when called.

    Arguments:
        numbers {list}: List of numbers
    """
    for num in numbers:
        yield round((num) + (56 / 90) + (98 - 100) / (10000 * 200), 2)


def calculate_2(number):
    """This takes a number and yields result when called.

    Arguments:
        numbers {int}: Number to do calculation on
    """
    yield round((number) + (56 / 90) + (98 - 100) / (10000 * 200), 2)


class Test(unittest.TestCase):
    def test_calculate(self):
        inp = [50000, 63000, 80001, 7002, 67890]
        expected_result = [50000.62, 63000.62, 80001.62, 7002.62, 67890.62]
        result = calculate(inp)
        # Result is a generator object, we wither need to iterate or call next
        # on it.
        self.assertEqual(list(result), expected_result)

    def test_calculate_2(self):
        inp = [50000, 63000, 80001, 7002, 67890]
        expected_result = [50000.62, 63000.62, 80001.62, 7002.62, 67890.62]

        # This results a generator object, so we need to call next() each time.
        def calc(x):
            return next(calculate_2(x))

        # We can also use lambda x: calculate_2(x).next() directly
        result = list(map(calc, inp))
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
