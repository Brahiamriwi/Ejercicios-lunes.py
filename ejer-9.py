#Pide una nota (0-10). Muestra si
#perdio, aprobado o sobresaliente


nota = float(input("ingresa tu nota: "))

if nota <= 5:
    print("perdio")
    
elif nota > 5 and nota <8:
    print("gano")
    
elif nota >= 8 and nota <10:
    print("sobresaliente")
    
else: 
    print("nota invalida")