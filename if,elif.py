edad = int(input("Escribe tu edad "))
if edad >= 0 and edad <= 11:
    print("Niño/a")
elif edad > 11 and edad <= 17:
    print("Adolescente")
elif edad > 17 and edad <= 29:
    print("Joven")
elif edad > 29 and edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")
   
