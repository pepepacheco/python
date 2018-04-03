import json
import pymongo
from pymongo import MongoClient


class Geografia:
    def __init__(self, ciudad, pais, latitud, longitud):
        self.ciudad   = ciudad
        self.pais     = pais
        self.latitud  = latitud
        self.longitud = longitud

    def toString(self):
        return self.ciudad + ", " + self.pais + ", " + self.latitud + ", " + self.longitud

datos = json.loads(open('datos.json').read())

client = MongoClient('localhost', 27017)
db = client.nuevaBD
collection = db.nuevaColeccion
listaObjetos = []

for x in (datos):
    collection.insert_one(x)
    objetoGeografia = Geografia(x['city'], x['country'], str(x['latitude']), str(x['longitude']))
    listaObjetos.append(objetoGeografia)



for i in listaObjetos:
    print(i.toString())
