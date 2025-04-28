#Pide la hora. Si es menor que 12 o
#mayor que 18, muestra "No es hora de
#trabajar".

hora = float(input("Ingresa la hora: "))

if hora < 12 or hora > 18:
    print("No es hora de trabajar")
    
else:
    print("Ya es hora de trabajar")    