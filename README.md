# tomasteawita_Blog
---
## Ejecución
* Tener docker instalado
* Crear directorio `postgres_data` y el archivo .env con la siguiente información:
```python
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST_AUTH_METHOD=trust
POSTGRES_PORT=5432
POSTGRES_HOST=postgre_db
```
a la misma altura que el archivo docker-compose.yml
* Correr el siguiente comando en una terminal en la misma altura que el archivo docker-compose.yml:
```bash
docker-compose up --build
```
* Abrimos otra termina y ejecutamos los comandos
```bash
docker exec -it web-app sh
python manage.py runserver 0.0.0.0:8000
```
* Finalmente abrimos en el navegador con la dirección `127.0.0.1:8000`