# isMutant
API para encontrar ADN mutante

## Features
- Implementacion sobre Docker o sobre el Host
- Valida que la matriz suminstrada sea consistente (que todas las filas tengan la misma cantidad de columnas)
- Valida que la matriz tenga el tamaño suficiente para albergar secuencias del tamaño requerido
- Contempla matrices donde la cantidad de filas es distinta a la cantidad de columnas
- Valida que los valores de cada celda sean valores permitidos ( A, T, G, C)
- Todos los valores controlados son parametrizables
- Recorre la matriz de forma vertical, horizontal, y en las 2 diagonales buscando la secuencia correcta

## To do
- Validar todas las secuencias que caben en una linea, tener en cuenta que cuando una secuencia coincide con una secuencia mutante no puede reutilizarse. Ej AAAAAG no puede devolver 2 coincidencias
- Mejorar documentacion sobre instalacion sobre host 
- Configuarar la implementación sobre Docker
- Mejorar Dockerfile utilizando mutli-stage builds https://www.docker.com/blog/containerized-python-development-part-1/
- Crear API REST que devuelve http 200-OK si un humano es mutante y HTTP 403-Forbidden si no lo es. La entrada es un JSON y el endpoint es /mutant
- Persistir los resultados en una base de datos y exponer en el endpoint /stats el resultado en formato JSON con el siguiente formato {"count_mutant_dna":40, "count_human_dna":100, "ratio":0.4}
- Implementar la solución en un server público

## Requerimientos para implementación con docker
- Docker Engine
- docker-compose

### Instalacion de Docker Engine
Instalar Docker Engine y docker-compose en Linux
- descargar y ejecutar script desde https://gist.github.com/Zalitoar/ef1577acad9c3a78461954e080dc8576

#### Como ejecutarlo con Docker
Instanciar los contenedores docker

## Requerimientos para implementación sobre el Host
- Python3.6
- flask
- 
### Como ejecutarlo sobre el Host
teniendo instalado flask globalmente o iniciando un ambiente virtual con flask instalado
``` 
pyhton3 /app/main.py
``` 

Abrir el navegador e ingresar a la direccion 0.0.0.0:8090
