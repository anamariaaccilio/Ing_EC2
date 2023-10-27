import requests
import Metodos_distancias


#Test Data  - MOOK

def calculate_distance():
    assert calculate_distance(("Kolkata", "India"), ("Lagos", "Nigeria"))== 2.34
    assert calculate_distance(("Istanbul", "Turkey"), ("Karachi", "Pakistan"))== 0
    

if __name__ == '__main__':
    pruebas.main()    


#Test steps:
# 1. Tener una rutal para acceder a la aplicación/página web
# 2. Ingresar ciudades que estén en la data/CSV
# 3. Ingresar países que se encuentren en la data/CSV
# 4. Click en uno de los 3 botones para escoger el formato en que se quiere calcular la distancia.
# 5. Mostrar un resultado con la distancia