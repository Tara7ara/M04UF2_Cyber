#!/usr/bin/python3

import xmltodict
import random

print("Crea un enemigo")
print("---------------")

name = input("Nombre: ")
health = input("Vida: ")
damage = input("Fuerza: ")


enemy = {
	"enemy": {
		"name": name,
		"damage": damage,
		"health": health
	}
}

enemy_xml = xmltodict.unparse(enemy, pretty=True)
#el prety es para hacerlo bonito

print(enemy_xml)
#USAMOS LAS TUPLAS no diccionario

archivo = open("enemy.xml", "w")

archivo.write(enemy_xml)

archivo.close()
