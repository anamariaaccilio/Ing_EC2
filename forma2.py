import requests

url1="https://nominatim.openstreetmap.org/search.php?q="
url2="&format=jsonv2"


ciudad1=input("Ingrese la ciudad 1: ")
#pais=input("Ingrese el pais: ")
ciudad2=input("Ingrese la ciudad 2: ")

# Realiza la solicitud GET a la API de Nominatim
response_1 = requests.get(url1+ciudad1+","+"peru"+url2)
response_2 = requests.get(url1+ciudad2+","+"peru"+url2)


data1 = response_1.json()
data2 = response_2.json()

# Obtiene las coordenadas de la ciudad 1
lat1 = float(data1[0]["lat"])
lon1 = float(data1[0]["lon"])

# Obtiene las coordenadas de la ciudad 2
lat2 = float(data2[0]["lat"])
lon2 = float(data2[0]["lon"])

# Calcula la distancia entre las dos ciudades
from haversine import haversine, Unit
coordenadas1 = (lat1, lon1)
coordenadas2 = (lat2, lon2)
distancia = haversine(coordenadas1, coordenadas2)
print("La distancia entre", ciudad1, "y", ciudad2, "es: ",distancia, "km")




