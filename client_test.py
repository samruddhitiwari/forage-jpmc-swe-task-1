import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
def test_getRatio():
    # Test case where price_b is zero
    assert getRatio(5, 0) is None  # Expecting None as there's no return value when price_b is zero

    # Test case where price_a is zero
    assert getRatio(0, 10) == 0.0  # Expecting ratio to be 0.0 when price_a is zero

    # Test case where both price_a and price_b are positive
    assert getRatio(10, 5) == 2.0  # Expecting ratio to be 2.0 when price_a is twice price_b

    # Test case where both price_a and price_b are negative
    assert getRatio(-10, -5) == 2.0  # Expecting ratio to be 2.0 when both prices are negative

    # Test case where price_a is negative and price_b is positive
    assert getRatio(-10, 5) == -2.0  # Expecting ratio to be -2.0 when price_a is negative and price_b is positive

    # Test case where price_a is positive and price_b is negative
    assert getRatio(10, -5) == -2.0  # Expecting ratio to be -2.0 when price_a is positive and price_b is negative

    # Test case where price_a and price_b are equal
    assert getRatio(5, 5) == 1.0  # Expecting ratio to be 1.0 when price_a equals price_b

    print("All tests passed!")

# Run the unit tests
test_getRatio()



if __name__ == '__main__':
    unittest.main()
