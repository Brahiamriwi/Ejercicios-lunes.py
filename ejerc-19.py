#Pide 5 números y crea una lista solo con
#los pares.

lista_pares= []

for i in range(5):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        lista_pares.append(num)
        
    print("lista de numeros pares: ",lista_pares)      
      

