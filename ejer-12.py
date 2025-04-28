#dada una lista de frutas, pide al usuario una fruta que desee eliminar


frutas =["banano", "manzana","pera"]


print("lista de frutas: ", frutas)
for i in frutas:
    eliminar = input("Que fruta desea eliminar? : ")
    frutas.remove(eliminar)
    print("fruta eliminada")
    print("las frutas disponibles son",frutas)

    


   