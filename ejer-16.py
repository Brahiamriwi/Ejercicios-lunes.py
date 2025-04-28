#buscar si un número existe en una lista y
#encontrar su posición.


lista = [1,2,3,4,5,6,7,7,8,9]

buscado = int(input("Ingrese el numero a buscar: "))

if buscado in lista:
    posicion = lista.index(buscado)
    print(f"El numero {buscado}, esta en la posicion {posicion}")
    
else:
    print(f"El numero {buscado}, no se encuentra en la lista")