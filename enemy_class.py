#!/usr/bin/python3

import random

class Enemy:

	def __init__(self, nombre, vida, fuerza, descripcion):
		self.name = nombre
		self.hp = vida
		self.damage = fuerza
		self.description = descripcion

	def info (self):
		print ("NAME: "+self.name)
		print ("HP: "+str(self.hp))
		print ("DAMAGE: "+str(self.damage))

		if self.description != "":
			print ("DESCRIPTION: "+self.description)

	def attack (self):
		return random.randint(0, self.damage)

	def hurt (self, damage):
		self.hp -= damage

		if self.hp > 0:
			return False
	
		return True

if __name__ == "__main__":

	orc = Enemy("Orc", 10, 25, "Es un orco feo, que te esperas")
	orc.info()

#	enemies = [Enemy("Troll",14,7,"Es un troll tonto"),Enemy("Slime",0,1,"Slime de color verde que es mas inutil que yo que se")]
#	for enemy in enemies:
#		enemy.info()

	print("El orco acaba de pegar un puño en el saco de entrenamiento y ha hecho " + str(orc.attack()) + " de daño")

#	print(orc.hurt(orc.attack())
