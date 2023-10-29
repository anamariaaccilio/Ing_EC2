import unittest
from Metodos_distancias import DistanceCalculatorFactory

#CASO DE ÉXITO
class TestDistanceCalculator1(unittest.TestCase):

    def test_CSV_method(self):
        distance = DistanceCalculatorFactory.create_distance_calculator("CSV", "Kolkata", "India", "Lagos", "Nigeria")
        self.assertAlmostEqual(distance, 9219.74141992384, places=2)

    def test_API_method(self):
        distance = DistanceCalculatorFactory.create_distance_calculator("API", "Kolkata", "India", "Lagos", "Nigeria")
        self.assertAlmostEqual(distance, 9218.040829550899, places=2)

    def test_MOOK_method(self):
        distance = DistanceCalculatorFactory.create_distance_calculator("MOOK", "Kolkata", "India", "Lagos", "Nigeria")
        self.assertAlmostEqual(distance, 9219.74141992384, places=2)

#CASO EXTREMO 1:
class TestDistanceCalculator2(unittest.TestCase):

    def test_nonexistent_city_csv(self):
        # Test when a city does not exist in the CSV data
        result = DistanceCalculatorFactory.create_distance_calculator("CSV", "Lima123", "Peru", "Quito", "Ecuador")
        self.assertEqual(result, "No se encuentra la ciudad en la base de datos")

    def test_nonexistent_city_api(self):
        # Test when a city does not exist in the Nominatim API
        result = DistanceCalculatorFactory.create_distance_calculator("API", "Lima123", "Peru", "Quito", "Ecuador")
        self.assertEqual(result, "No se encuentra la ciudad en la base de datos")

#CASO EXTREMO 2:

class TestDistanceCalculator3(unittest.TestCase):

    def test_repeated_city_csv(self):
        # Test when both country and citys repeated

        result = DistanceCalculatorFactory.create_distance_calculator("CSV", "Madrid", "Spain", "Madrid", "Spain")
        self.assertEqual(result, "Las ciudades son iguales")

    def test_repeated_city_api(self):
        # Test when both country and citys repeated

        result = DistanceCalculatorFactory.create_distance_calculator("API", "Madrid", "Spain", "Madrid", "Spain")
        self.assertEqual(result, "Las ciudades son iguales")    



if __name__ == '__main__':
    unittest.main()

