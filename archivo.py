#!/usr/bin/python3

#abrir un archivo (es un objeto que contiene lo de dentro)
#r=lectura w=editar
try:
	archivo = open("numeritos.txt", "r")
#leer el archivo
#print(archivo.read())
#devuelve las x primeros characters
#print(archivo.read(8))
#devuelve el archivo linea a linea
#print(archivo.readline())

	linea = archivo.readline()
#split --> divide en un array la string que pasemos, por el character que hemos dicho
	lista = linea.split(";") 

	print(lista[3])

#para cerrar el archivo
	archivo.close()

except:
	print("ERROR al abrir el archivo")

archivo = open("textitos.txt", "w")

#para escribir un archivo
archivo.write("ola k ase")

archivo.close()

#en py los arrays no se llama array, se llama lista de elementos o diccionarios
diccionario = {
	"nombre": "Guillem",
	"apellido": "Granjero",
	"altura": 1.1
}
#el dicionario no hace falta que se llame asi
print(diccionario["altura"])

