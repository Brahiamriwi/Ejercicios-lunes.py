#pide edad y determina si es niño, adoles, adulto, anciano

edad = 0
edad = int(input("Ingresa tu edad: "))

if edad >= 1 and edad <= 12:
    print("eres un niño")
    
elif edad > 12 and edad <=17:
    print("Eres un adolescente") 
    
elif edad > 17 and edad <=35:
    print("Eres un joven")       
    
elif edad > 35 and edad >= 60:
    print("Eres un adulto")
    
elif edad > 60:
    print("Eres un anciano")
    
else: 
    print("Edad inválida")   
    