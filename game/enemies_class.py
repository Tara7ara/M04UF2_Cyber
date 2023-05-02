#!/usr/bin/python3

import xmltodict

from enemy_class import Enemy

class Enemies:

	def __init__(self):
		xml_file = open ("enemys.xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())

		enemies_list = enemies_tmp['enemies']['enemY']

		self.enemies = []

		for e in enemies_list:
			self.enemies.append(Enemy(e["name"],e["damage"],e["health"],"Descripcion nula ;)"))

