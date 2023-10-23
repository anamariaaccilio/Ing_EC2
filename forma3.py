from haversine import haversine

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

def obtener_dict(city, country):
    return city_coordenadas.get((city, country), None)

def main():
    city1 = input("Ingrese la Ciudad 1: ")
    country1 = input(f"Ingrese el País de {city1}: ")
    city2 = input("Ingrese la Ciudad 2: ")
    country2 = input(f"Ingrese el País de {city2}: ")
    coordenada_city1 = obtener_dict(city1, country1)
    coordenada_city2 = obtener_dict(city2, country2)

    if coordenada_city1 and coordenada_city2:
        lat1, long1 = coordenada_city1["lat"], coordenada_city1["lng"]
        lat2, long2 = coordenada_city2["lat"], coordenada_city2["lng"]

        distance = haversine((lat1, long1), (lat2, long2))

        print(
            f"La distancia entre {city1}, {country1}, y {city2}, {country2} es {distance} km"
        )
        print(
            f"Las coordenadas de {city1}, {country1} => Latitud: {lat1}, Longitud: {long1}"
        )
        print(
            f"Las coordenadas de {city2}, {country2} => Latitud: {lat2}, Longitud: {long2}"
        )
    else:
        print("Ciudad y/o país no encontrados en la base de datos.")

if __name__ == "__main__":
    main()
