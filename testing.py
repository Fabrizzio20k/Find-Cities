import unittest
from unittest.mock import patch
from find_cities import Ciudad, Coordenada, ObtenerCoordenadasMock, ObtenerCoordenadasCSV, ObtenerCoordenadasAPI, calcular_distancia_haversine, ciudades_mas_cercanas

class TestCalculoDistancias(unittest.TestCase):

    def setUp(self):
        self.ciudad1 = Ciudad("Peru", "Lima")
        self.ciudad2 = Ciudad("Colombia", "Bogota")
        self.ciudad3 = Ciudad("Argentina", "Buenos Aires")
        self.metodo = ObtenerCoordenadasMock()

    def test_distancia_haversine(self):
        coord1 = Coordenada(-12.0464, -77.0428)
        coord2 = Coordenada(4.7110, -74.0721)
        distancia = calcular_distancia_haversine(coord1, coord2)
        self.assertAlmostEqual(distancia, 1892, delta=10)  # Ajustado a aproximadamente 1892 km

    def test_ciudades_mas_cercanas_exito(self):
        ciudades_cercanas, distancia = ciudades_mas_cercanas(self.ciudad1, self.ciudad2, self.ciudad3, self.metodo)
        self.assertIsNotNone(ciudades_cercanas)
        self.assertIsNotNone(distancia)

    def test_ciudad_no_existe(self):
        ciudad_inexistente = Ciudad("Fantasia", "CiudadFantasma")
        ciudades_cercanas, distancia = ciudades_mas_cercanas(ciudad_inexistente, self.ciudad2, self.ciudad3, self.metodo)
        self.assertIsNone(ciudades_cercanas)
        self.assertIsNone(distancia)

    def test_ciudad_repetida(self):
        ciudades_cercanas, distancia = ciudades_mas_cercanas(self.ciudad1, self.ciudad1, self.ciudad3, self.metodo)
        self.assertIsNotNone(ciudades_cercanas)
        self.assertIsNotNone(distancia)

if __name__ == "__main__":
    unittest.main()
