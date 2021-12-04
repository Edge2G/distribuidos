## Tarea 3: Balanceadores de Carga
---

### 1 - Instalacion: Docker compose<br><br>

En este caso se utilizo **docker-compose** para la ejecucion de el microservicio de inventario, con **flask**, y **nginx**.

Para ejecutar el contenedor, asumiendo que ya se encuentra en un sistema con **docker** y **docker-compose**, simplemente se invocan los siguientes comandos:

```sh
docker-compose build
```

```sh
docker-compose up
```

Luego, las peticiones se escuchan en localhost.