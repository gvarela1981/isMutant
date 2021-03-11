# isMutant
API para encontrar ADN mutante

## Requerimientos
- Docker Engine
- docker-compose

## Instalacion
Instalar Docker Engine y docker-compose en Linux
- descargar y ejecutar script desde https://gist.github.com/Zalitoar/ef1577acad9c3a78461954e080dc8576

## Como ejecutarlo
Instanciar los contenedores docker
``` 
docker-compose up -d
``` 
Abrir el navegador e ingresar a la direccion 0.0.0.0:8090

#### To do
- Mejorar Dockerfile utilizando mutli-stage builds https://www.docker.com/blog/containerized-python-development-part-1/
- Recorrer la Matriz evaluando cada secuencia en 3 direcciones
- Crear API REST que devuelve http 200-OK si un humano es mutante y HTTP 403-Forbidden si no lo es. La entrada es un JSON y el endpoint es /mutant
- Persistir los resultados en una base de datos y exponer en el endpoint /stats el resultado en formato JSON con el siguiente formato {"count_mutant_dna":40, "count_human_dna":100, "ratio":0.4}