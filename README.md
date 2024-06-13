# Find Cities 

## Actividad de Desarrollo, Colaboración y Pruebas Unitarias

Curso: Ingeniería de Software (CS3081)

## Descripción

Esta actividad se centra en buscar las distancias entre tres ciudades de dos formas principales, consumiendo la api de [Nominatim](https://nominatim.openstreetmap.org/ui/search.html) o con el csv `worldcities.csv`. Asimismo, se realizaron test unitarios para verificar el correcto funcionamiento del código.

## Requerimientos

+ request
+ csv
+ pytest

## Ejecución
Para probar el código, ejecutar el siguiente comando en la raíz:
  
```bash
python find_cities.py
```

Deberá retornar un valor como el siguiente:

> Las ciudades más cercanas son Lima, Peru y Bogotá, Colombia con una distancia de 1887.13 km.

Para ejecutar los test unitarios, ejecutar el siguiente comando en la raíz:

```bash
pytest testing.py
```

Deberá retornar un valor como el siguiente:

> ========== test session starts ============ \
> platform win32 -- Python 3.12.4, pytest-8.1.1, pluggy-1.4.0 \
> rootdir: C:\Users\jeffr\GitHub\Find-Cities \
> plugins: anyio-4.3.0, Faker-25.2.0 \
> collected 4 items  \
> testing.py                       [100%]

> ========== 4 passed in 0.49s ========== 


## Autores

| **Fabrizzio Vilchez** | **Jeffrey Monja** |
|:------------:|:------------:|
| ![Fabrizzio Vilchez](https://avatars.githubusercontent.com/u/115495332?v=4) | ![Jeffrey Monja](https://avatars.githubusercontent.com/u/104637993?v=4) |
| [https://github.com/Fabrizzio20k](https://github.com/Fabrizzio20k) | [https://github.com/jeffreymonjacastro](https://github.com/jeffreymonjacastro) |