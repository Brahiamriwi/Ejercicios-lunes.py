#Pide dos números. Si ambos son
#mayores que 0, muestra "Ambos son
#positivos"

num=0
mum2=0

numero_usuario1 = int(input("Ingresa un numero: "))
numero_usuario2 = int(input("Ingresa un numero: "))

if numero_usuario1 > 0 and numero_usuario2 > 0:
    print("ambos son positivos")
    
elif numero_usuario1 < 0 and numero_usuario2 <0:
    print("numeros negativos")
    
else: 
    print("caracteres inválidos")
    