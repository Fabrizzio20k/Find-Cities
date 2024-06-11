import csv
import requests
import math
from abc import ABC, abstractmethod


class Coordenada:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


class Ciudad:
    def __init__(self, nombre_pais, nombre_ciudad):
        self.nombre_pais = nombre_pais
        self.nombre_ciudad = nombre_ciudad


class IObtenerCoordenadas(ABC):
    @abstractmethod
    def obtener_coordenadas(self, ciudad):
        pass


class ObtenerCoordenadasCSV(IObtenerCoordenadas):
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    def obtener_coordenadas(self, ciudad):
        with open(self.archivo_csv, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['city'].lower() == ciudad.nombre_ciudad.lower() and row['country'].lower() == ciudad.nombre_pais.lower():
                    return Coordenada(float(row['lat']), float(row['lng']))
        return None

class ObtenerCoordenadasMock(IObtenerCoordenadas):
    def obtener_coordenadas(self, ciudad):
        if ciudad.nombre_ciudad.lower() == "ciudadfantasma":
            return None
        return Coordenada(0.0, 0.0)


class ObtenerCoordenadasAPI(IObtenerCoordenadas):
    def obtener_coordenadas(self, ciudad):
        url = f'https://nominatim.openstreetmap.org/search?q={ciudad.nombre_ciudad},{ciudad.nombre_pais}&format=json'
        data = requests.get(url)
        data = data.json()
        if data:
            latitud = float(data[0]['lat'])
            longitud = float(data[0]['lon'])
            return Coordenada(latitud, longitud)
        return None


def calcular_distancia_haversine(coord1, coord2):
    R = 6371.0  # Radio de la Tierra en kilómetros

    lat1, lon1 = math.radians(coord1.latitud), math.radians(coord1.longitud)
    lat2, lon2 = math.radians(coord2.latitud), math.radians(coord2.longitud)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c
    return distancia


def obtener_coordenadas(ciudad, metodo):
    return metodo.obtener_coordenadas(ciudad)


def ciudades_mas_cercanas(ciudad1, ciudad2, ciudad3, metodo):
    coord1 = obtener_coordenadas(ciudad1, metodo)
    coord2 = obtener_coordenadas(ciudad2, metodo)
    coord3 = obtener_coordenadas(ciudad3, metodo)

    if coord1 is None or coord2 is None or coord3 is None:
        return None, None

    dist1 = calcular_distancia_haversine(coord1, coord2)
    dist2 = calcular_distancia_haversine(coord1, coord3)
    dist3 = calcular_distancia_haversine(coord2, coord3)

    distancias = {(ciudad1, ciudad2): dist1, (ciudad1, ciudad3): dist2, (ciudad2, ciudad3): dist3}
    ciudades_cercanas = min(distancias, key=distancias.get)
    return ciudades_cercanas, distancias[ciudades_cercanas]




def main():
    ciudad1 = Ciudad("Peru", "Lima")
    ciudad2 = Ciudad("Colombia", "Bogota")
    ciudad3 = Ciudad("Argentina", "Buenos Aires")

    metodo = ObtenerCoordenadasAPI()

    ciudades_cercanas, distancia = ciudades_mas_cercanas(ciudad1, ciudad2, ciudad3, metodo)

    if ciudades_cercanas:
        ciudadA, ciudadB = ciudades_cercanas
        print(f'Las ciudades más cercanas son {ciudadA.nombre_ciudad}, {ciudadA.nombre_pais} y {ciudadB.nombre_ciudad}, {ciudadB.nombre_pais} con una distancia de {distancia:.2f} km.')
    else:
        print("No se pudieron obtener las coordenadas de una o más ciudades.")


if __name__ == "__main__":
    main()
