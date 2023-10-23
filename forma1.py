from haversine import haversine, Unit
import csv

class CSVDataProcessor:
    def get_city_data(self, city_name, country_name):
        pass

class WorldCitiesCSVProcessor(CSVDataProcessor):
    def __init__(self, csv_file):
        self.city_data = self.load_data(csv_file)

    def load_data(self, csv_file):
        data = {}
        with open(csv_file, 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                city = fila['city_ascii']
                country = fila['country']
                latitude = float(fila['lat'])
                longitude = float(fila['lng'])
                data[(city, country)] = (latitude, longitude)
        return data

    def get_city_data(self, city_name, country_name):
        key = (city_name, country_name)
        if key in self.city_data:
            return self.city_data[key]
        else:
            return None

# Factory Method para crear instancias de procesadores de datos CSV
class CSVDataProcessorFactory:
    @staticmethod
    def create_processor(csv_file):
        return WorldCitiesCSVProcessor(csv_file)

# Función para calcular la distancia entre dos ciudades
def calculate_distance(city1, country1, city2, country2, data_processor):
    location1 = data_processor.get_city_data(city1, country1)
    location2 = data_processor.get_city_data(city2, country2)

    if location1 and location2:
        return haversine(location1, location2, unit=Unit.KILOMETERS)
    else:
        return None

def main():
    csv_file = 'worldcities.csv'
    data_processor = CSVDataProcessorFactory.create_processor(csv_file)
    city1 = input("Ingresa el nombre de la ciudad 1: ")
    country1 = input("Ingresa el nombre del país 1: ")
    city2 = input("Ingresa el nombre de la ciudad 2: ")
    country2 = input("Ingresa el nombre del país 2: ")

    distance = calculate_distance(city1, country1, city2, country2, data_processor)
    if distance is not None:
        print(f'Distancia entre {city1}, {country1} y {city2}, {country2}: {distance:.2f} kilómetros')
    else:
        print('Datos no encontrados en el archivo CSV.')

if __name__ == "__main__":
    main()

