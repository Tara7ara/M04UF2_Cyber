#!/usr/bin/python3

from enemies_class import Enemies
from player_class import Player

player = Player()
enemies = Enemies()

def game ():
	salir = False
	while not salir:
		print("Me acabas de encontrar, soy un enemigo")

		enemies.show_info()

		opc = input("¿Quieres atacar o que bobo? atacar/mirar las musarañas")

		if opc == "atacar":
			damage = player.attack()
			dead = enemies.hurt(damage)
			if not dead:
				print("El enemeigo te atacka MONGOLO")
				damage = enemies.attack()
				player.hurt(damage)
		

if __name__ == "__main__":
	title = "Empiesa el juego"
	print(title)
	print("-"*len(title))


	opc = ""
	while opc != "s":
		print("1 --> JUEGO NUEVO")
		print("2 --> CARGAR JUEGO")
		print("3 --> SALIR")

		opc = input("Introduce una opción: ").lower()

		if opc == "1":
			player.input_info()
			player.write_info()
		elif opc == "2":
			player.read_info()
			player.show_info()
		
		game()


			

