#Declaramos una variable
calificacion = input("introduce tu calificación del AZ-900: ")

calificacion = int(calificacion) # las variables provenientes del teclado se convierten de tipo de variable a string

#Preguntamos si la calificación es menor a 700
if calificacion < 700:
    print("Ves por no estudiar") #Si es menor a 700 muestra esto
elif calificacion  > 1000:
    print("MIENTESSS")
else: #si no se cumple el if pasa al else 
    print("Felicidade pasa por tu certificado")




edad = input("Introduce tu edad ")
edad = int(edad) # hay que castearlo

if edad > 18 and edad < 100:
    print("Bienvenido al mamitassssss ")
elif edad > 0 and edad < 18:
         print("no puedes comprar cigarros ")
elif edad > 0 and edad < 100:
    print("si vienes acompañado de tus abuelitos si te podemos fiar")
elif edad < 0:
    print("ni que fueras viajero del tiempo")
else:
    print("Ya deberías estar empujando margaritas")


# en paython no existe el switch case 
# el elif lleva una condición para probar tambien, en cambio en el else se va ejecuatar si o si sin comprobar otra 