from ddt import ddt, data, unpack
import unittest
import math
from HumidexTemperature import dewpoint, dewpoint2, humidex

@ddt
class TestHumidexTemperature(unittest.TestCase):
    @data(
            {"t": 27.0, "h": 100.0, "expected": 27.0, "exact": True},
            {"t": 28.0, "h": 20.0, "expected": 2.9},
            {"t": 27.0, "h": 62.0, "expected": 19.0},
            {"t": 20.0, "h": 50.0, "expected": 9.0},
            {"t": 20.0, "h": 30.0, "expected": 2.0},
            {"t": 25.0, "h": 52.0, "expected": 15.0},
            {"t": 10.0, "h": 52.0, "expected": 0.0}
        )
    @unpack
    def test_dewpoint(self, t, h, expected, exact=False):
        # expected value evaluated here: http://www.dpcalc.org
        result = dewpoint(t, h)
        print("dewpoint: {:5.2f} - {:5.2f}".format(result, expected))
        if not exact: 
            self.assertTrue(math.isclose(result, expected, abs_tol=1.0))
        else: 
            self.assertEqual(result, expected)
    
    @data(
            {"t": 27.0, "h": 100.0, "expected": 41.0, "exact": False},
            {"t": 30.0, "h": 70.0, "expected": 41.0},
            {"t": 28.0, "h": 20.0, "expected": 27.0}, 
            {"t": 20.0, "h": 50.0, "expected": 21.0},
            {"t": 20.0, "h": 30.0, "expected": 18.0},
            {"t": 25.0, "h": 52.0, "expected": 29.0},
            {"t": 10.0, "h": 52.0, "expected": 8.0}
        )
    @unpack
    def test_humidex(self, t, h, expected, exact=False):
        # expected value evaluated here: http://www.ohcow.on.ca/edit/files/general_handouts/heat-stress-calculator.html
        result = humidex(t, h)
        print("humidex: {:5.2f} - {:5.2f}".format(result, expected))
        if not exact: 
            self.assertTrue(math.isclose(result, expected, abs_tol=1.0))
        else: 
            self.assertEqual(result, expected)


if __name__ == '__main__':
        unittest.main()

