#Agregar un número en una posición
#específica.

lista = [2,3,4,5,6]

numero_ingresar = int(input("Ingrese el numero: "))
posicion = int(input("Ingrese la posicion de 1 a 10: "))

lista.insert(posicion, numero_ingresar)
print("la lista actualizada es:", lista)
