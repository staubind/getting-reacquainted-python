import unittest
from city_functions import get_formatted_city_name

class TestCityFormatCases(unittest.TestCase):
    """Test cases for the get_formatted_city_name function"""

    def test_city_country(self):
        """Test that it works for names like Santiago, Chile """
        formatted_name = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Test that it works for names like Santiago, Chile - population 5000000"""
        formatted_name = get_formatted_city_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5000000')


unittest.main()