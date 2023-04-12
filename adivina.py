import random
import math

DEBUG = False #True

num_max = 100

print("Adivina un número del 1 al "+str(num_max))

azar = math.floor(random.random()*num_max)+1

if DEBUG:
	print(azar)

salir = False

while not salir:

	numero = int(input("Introduce un numero del 1 al "+str(num_max)+": "))

	if numero < azar:
		print("El numero es MAYOR")
		salir = False
	elif numero > azar:
		print("El numero es MENOR")
		salir = False
	else:
		print("CORRECTO, el numero es "+str(azar))
		salir = True
