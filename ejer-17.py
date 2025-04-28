#Contar cuántas veces aparece un nombre
#en la lista.

lista = ["arroz","arroz","papa","papa"]

nombre = input("Ingrese el nombre que desea buscar: ")

cantidad = lista.count(nombre)

print(f"El nombre {nombre}, se encuentra {cantidad} veces")

