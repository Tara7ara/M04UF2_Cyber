#!/usr/bin/python3

import xmltodict
import os

aventurero = input("¿Quien eres bobo? Yo soy ")
title = "La gran aventura de "+str(aventurero)

print(title)
print("-"*len(title))

print("Antes de todo necesito tus datos")
player_health = int(input("Vida: "))
player_damage = int(input("Fuerza: "))
player = {
	"player" : {
		"name": aventurero,
		"damage": player_damage,
		"health": player_health
	}
}

player_stats_xml = xmltodict.unparse(player, pretty=True)
archivo = open("stats_player.xml", "w")
archivo.write(player_stats_xml)
archivo.close()
#Ya tenemos el nombre y los datos


enemy1= diccionario["enemys"]["enemy"]
("Nombre: "+enemy1["name"])
("Daño: "+enemy1["damage"])
("Vida: "+enemy1["health"])

vida_enemy= int((enemy1["health"]))
daño_enemy= int((enemy1["damage"]))
nombre_enemy= str((enemy1["name"]))

while True:

	teclado = input ("Introduce que quieres hacer, para ver tu vida escribe: vida, para atacar escirbe: ataca, para ver las stats de los enemigos escribe: stats y para salir escribe: salir\n")

	if teclado == "vida":		
		print ("Tu vida es: " + str(vida))
	
	elif teclado == "ataca":

		daño= int(random.randrange(5))
		daño_enemy1= int(random.randrange(daño_enemy))

		vida_enemy1= vida_enemy1 - daño
		vida= vida - daño_enemy1
		print ("Le has sacado " + str(daño) + " de vida, ahora el enemigo tiene: "+ str(vida_enemy1) + " de vida\n")
		print (str(nombre_enemy1) + " tambien te ha atacado, te ha sacado "+ str(daño_enemy1) + " de vida, ahora tienes " + str(vida) + " de vida\n")
	
	elif teclado == "stats":
		
		enemy1= diccionario["enemys"]["enemy"]
		print("Nombre: "+enemy["name"])
		print("Daño: "+enemy["damage"])
		print("Vida: "+enemy["health"])		
		print("Nivel: "+enemy["level"])

	elif teclado == "salir":
		break
	
	if vida <= 0:
		print("Moriste")
		break

	elif vida_enemy1 <= 0:
		print("Ganaste el combate")
		break

#os.system ("clear")
#print(title)
#print("-"*len(title))
#print("Iniciaste un combate con " + {name})
