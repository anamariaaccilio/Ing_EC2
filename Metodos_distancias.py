
from haversine import haversine, Unit
import csv
import requests

class DistanceCalculator:
    def calculate_distance( city1, city2):
        return haversine(city1, city2, unit=Unit.KILOMETERS)       


class CSV_Method(DistanceCalculator):
    def calculate_distance(city1, country1, city2, country2):
        try:
            data = {}
            csv_file = 'worldcities.csv'
            with open(csv_file, 'r', encoding='utf-8') as archivo_csv:
                lector_csv = csv.DictReader(archivo_csv)
                for fila in lector_csv:
                    city = fila['city_ascii']
                    country = fila['country']
                    latitude = float(fila['lat'])
                    longitude = float(fila['lng'])
                    data[(city,country)] = (latitude, longitude)

            location1 = data[(city1,country1)]
            location2 = data[(city2,country2)]

            return DistanceCalculator.calculate_distance(location1, location2)
        except:
            return "No se encuentra la ciudad en la base de datos"               

class API_Method(DistanceCalculator):
    def calculate_distance(city1, country1, city2, country2):
        try:
            url1="https://nominatim.openstreetmap.org/search.php?q="
            url2="&format=jsonv2"

            # Realiza la solicitud GET a la API de Nominatim
            response_1 = requests.get(url1+city1+","+country1+url2)
            response_2 = requests.get(url1+city2+","+country2+url2)


            data1 = response_1.json()
            data2 = response_2.json()

            # Obtiene las coordenadas de la ciudad 1
            lat1 = float(data1[0]["lat"])
            lon1 = float(data1[0]["lon"])

            # Obtiene las coordenadas de la ciudad 2
            lat2 = float(data2[0]["lat"])
            lon2 = float(data2[0]["lon"])

            # Calcula la distancia entre las dos ciudades
            coordenadas1 = (lat1, lon1)
            coordenadas2 = (lat2, lon2)

            return DistanceCalculator.calculate_distance(coordenadas1, coordenadas2)
        except:
            return "No se encuentra la ciudad en la base de datos"


class MOOK_Method(DistanceCalculator):
    def calculate_distance( city1, country1, city2, country2):
        city_coordenadas = {
        ("Beijing", "China"): {
            "lat": 39.9040,
            "lng": 116.4075
        },
        ("Kolkata", "India"): {
            "lat": 22.5675,
            "lng": 88.3700
        },
        ("Bangkok", "Thailand"): {
            "lat": 13.7525,
            "lng": 100.4942
        },
        ("Shenzhen", "China"): {
            "lat": 22.5350,
            "lng": 114.0540
        },
        ("Lagos", "Nigeria"): {
            "lat": 6.4550,
            "lng": 3.3841
        },
        ("Istanbul", "Turkey"): {
            "lat": 41.0136,
            "lng": 28.9550
        },
        ("Karachi", "Pakistan"): {
            "lat": 24.8600,
            "lng": 67.0100
        },
        ("Bangalore", "India"): {
            "lat": 12.9789,
            "lng": 77.5917
        },
        ("Ho Chi Minh City", "Vietnam"): {
            "lat": 10.7756,
            "lng": 106.7019
        },
        }

        coordenada_city1 = city_coordenadas.get((city1, country1), None)
        coordenada_city2 = city_coordenadas.get((city2, country2), None)

        if coordenada_city1 is not None and coordenada_city2 is not None:
            lat1, long1 = coordenada_city1["lat"], coordenada_city1["lng"]
            lat2, long2 = coordenada_city2["lat"], coordenada_city2["lng"]

            coordenadas1 = (lat1, long1)
            coordenadas2 = (lat2, long2)

            return DistanceCalculator.calculate_distance(coordenadas1, coordenadas2)
        
        else:
            return "No se encuentra la ciudad en la base de datos"

        
# Crea una clase Factory
class DistanceCalculatorFactory:
    @staticmethod
    def create_distance_calculator(method,city1,country1,city2,country2):
        if (city1 == city2) and (country1 == country2):
            return "Las ciudades son iguales"
        if method == "CSV":
            return CSV_Method.calculate_distance(city1,country1,city2,country2)
        elif method == "API":
            return API_Method.calculate_distance(city1,country1,city2,country2)
        else:
            return MOOK_Method.calculate_distance(city1,country1,city2,country2)

