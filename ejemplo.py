#Script para aprender la basde de py

#definir una funcion, siempre arriba de todo
def suma_numeros (a, b):
	print(a + b)

#print de toda la vida
print("Hello world!")

#if y else de toda la vida
if 3 == 3:
	print("Es igual carajo")

if 3 > 8:
	print("Es mayor")
else:
	print("Es menor")

#variables
num1 = 8
num2 = 8

#elif es como el else if
if num1 > num2:
	print("Mayor")
elif num1 < num2:
	print("Menor")
else:
	print("Igual")
#Las separaciones no es con ; es con la tabulacion

#strings
frase = "Queréis correr y no sabéis ni la base xD "

#Aunque no definamos las variables, py ya lo detecta, por eso peta --> print(frase+num1)
print(frase)
print(frase+str(num1))

#bucles
contador = 10
while contador > 0:
	print(contador)
	contador -= 1
while contador < 10:
	print(contador)
	contador += 1

#input, salto de linea \n, recordatorio int, bool, float.
teclado = input("Introduce tu nombre: ")
print("Hola "+teclado)

#Lo transforma automaticamanete en un INT print(int(teclado)+7)

#arrays
lista = ["uno",2,"treH","catorce"]
print(lista[2])
print(len(lista)) #retornara el numero de la casilla que tiene el array
print(len(lista[3])) #mostrara la de characters que hay en x casilla

#uso/llamada de la funcion
suma_numeros(num1, num2)
