#!/usr/bin/python3

import random

class Enemy:
	def __init__(self, name, health, strength, description = ""):
		self.name = name
		self.health = int(health)
		self.strength = int(strength)
		self.description = description

		print(self.name+": "+self.description)


	def attack (self):
		return random.randint(0, self.strength)


	def hurt (self, damage):
		self.health -= damage

		if self.health > 0:
			return False
		
		return True

	def show_info (self):
		print("Name: "+self.name)
		print("Health: "+str(self.health))
		print("Strength: "+str(self.strength))

		if self.description != "":
			print("Description: "+self.description)




if __name__ == "__main__":
	enemigo = Enemy("Orc", 10, 25, "Es un orco feo, que te esperas")

	enemigo.show_info()

	print(enemigo.hurt(enemigo.attack()))

	enemigo.show_info()
