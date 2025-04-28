#Pregunta si una persona tiene licencia
#y si lleva casco. Si no tiene licencia o
#no lleva casco, no puede conducir.

licencia=0
casco=0

licencia = str(input("tiene licencia? si/no: "))
casco= str(input("tiene casco? si/no : "))

if licencia == "si" and casco == "si":
    print("Puede conducir")
    
elif licencia == "si" and casco == "no":
    print("No puede conducir")    
    
elif licencia == "no" and casco == "si":
    print("No puede conducir")    
    
elif licencia == "no" and casco == "no":
    print("No puede conducir")   
     
else:
    ("valores inválidos")    
