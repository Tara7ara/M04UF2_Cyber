#!/usr/bin/python3

import xmltodict

import random

class Player:

	def __init__(self, nombre, hp=100, damage=10, level=1, xp=0):
		self.name = nombre
		self.hp = hp
		self.damage = damage
		self.level = level
		self.xp = xp
	
		xml_file = open("level.xml", "r")
		levels =  xmltodict.parse(xml_file.read())
		xml_file.close()

		tmp = levels["levels"]["level"]

		print(tmp)

		self.levels = {}

		for level in tmp:
			self.levels[ int(level["@num"]) ] = int(level["@xp"])

		print(self.levels)

	def set_hp (self, hp):
		self.hp = hp

	def set_damage (self, damage):
		self.damage = damage
	
	def set_level (self, level):
		self.level = level

	def set_xp (self, xp):
		self.xp = xp

	def info (self):
		print ("NAME: "+self.name)
		print ("HP: "+str(self.hp))
		print ("DAMAGE: "+str(self.damage))
		print ("LEVEL: "+str(self.level))
		print ("XP: "+str(self.xp))

	def get_level (self, xp = -1):	
		if xp == -1:
			return self.level

		level_cur = self.level

		for level in self.levels:
			if self.levels[level] <= xp:
				level_cur = level

		return level_cur

	def hurt (self):
		self.hp -= damage

		if self.hp > 0:
			return False

		return True
	
	def attack (self):
		return random.randint(0, self.damage)

if __name__ == "__main__":
	player = Player("TU")

	print(player.get_level(100))
