#rea una lista vacía y permite al usuario
#ñadir 3 nombres.

lista_nombres = []

for i in range(3):
    pide_nombres = input("Ingrese el nombre: ")
    lista_nombres.append(pide_nombres)

    
print("Nombres registrados:",lista_nombres)


