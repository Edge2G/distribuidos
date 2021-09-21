import redis
r = redis.Redis(host="localhost", port=6379, db=0)

r.set('hello','world') #llave=hello valor=world
value = r.get('hello')
print(value)

# Comandos para la terminal:
# redis-cli : ingresa a redis
# config get maxmemory-policy : te permite saber la politica de tu cache.
# config set maxmemory-policy volatile-lru : cambia las politicas del cache a lru.
# config get maxmemory : obtienes el maximo de la memoria cache -----> si sale 0 es xq tienen memoria infinita.
# config set maxmemory 20M: modifica el maximo de la memoria cache 20MB.

