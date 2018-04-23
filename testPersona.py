#!/usr/bin/env python3

from persona import Persona
import csv
import sqlite3


conn = sqlite3.connect('personas.db')
c = conn.cursor()

listaPersonas = []

with open('datos.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        listaPersonas.append( Persona(row['id'], row['first_name'], row['last_name'], row['email'], row['gender'], row['date']))

for persona in listaPersonas:
    p = (int(persona.id), persona.firstName, persona.lastName, persona.email, persona.gender, persona.date)
    c.execute("INSERT INTO persona VALUES (?,?,?,?,?,?)", p)
    
conn.commit()
conn.close()
