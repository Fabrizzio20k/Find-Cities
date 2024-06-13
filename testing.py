import pytest
from find_cities import Ciudad, Coordenada, ObtenerCoordenadasMock, calcular_distancia_haversine, ciudades_mas_cercanas

class TestCalculoDistancias:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ciudad1 = Ciudad("Peru", "Lima")
        self.ciudad2 = Ciudad("Colombia", "Bogotá")
        self.ciudad3 = Ciudad("Argentina", "Buenos Aires")
        self.metodo = ObtenerCoordenadasMock()

    def test_distancia_haversine(self):
        coord1 = Coordenada(-12.0464, -77.0428)
        coord2 = Coordenada(4.7110, -74.0721)
        distancia = calcular_distancia_haversine(coord1, coord2)
        print("Distancia:", distancia)
        assert pytest.approx(distancia, 10) == 1892  # Aproximadamente 1892 km

    def test_ciudades_mas_cercanas_exito(self):
        ciudades_cercanas, distancia = ciudades_mas_cercanas(self.ciudad1, self.ciudad2, self.ciudad3, self.metodo)
        ciudadA, ciudadB = ciudades_cercanas
        print(f'Las ciudades más cercanas son {ciudadA.nombre_ciudad}  y {ciudadB.nombre_ciudad}, con una distancia de {distancia:.2f} km.')
        assert ciudades_cercanas is not None
        assert distancia is not None

    def test_ciudad_no_existe(self):
        ciudad_inexistente = Ciudad("Fantasia", "CiudadFantasma")
        ciudades_cercanas, distancia = ciudades_mas_cercanas(ciudad_inexistente, self.ciudad2, self.ciudad3, self.metodo)
        print(ciudades_cercanas, distancia)
        assert ciudades_cercanas is None
        assert distancia is None

    def test_ciudad_repetida(self):
        ciudades_cercanas, distancia = ciudades_mas_cercanas(self.ciudad1, self.ciudad1, self.ciudad3, self.metodo)
        ciudadA, ciudadB = ciudades_cercanas
        print(f'Las ciudades más cercanas son {ciudadA.nombre_ciudad}  y {ciudadB.nombre_ciudad}, con una distancia de {distancia:.2f} km.')
        assert ciudades_cercanas is not None
        assert distancia is not None
