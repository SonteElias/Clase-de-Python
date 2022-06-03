# En esta parte vamos a ver la estructura if elif else

# Ejemplo 1 Con las calificacciónes del examen

#Declaramos una variable
calificacion = input("introduce tu calificación del AZ-900: ")#Con input hacemos que nuestro programa reciba información por medio de los perifericos 
                                                              # Toda la información de los perifericos es del tipo String
calificacion = int(calificacion) # las variables provenientes del teclado se convierten de tipo string a variable tipo entero 

#Estructura IF 
if calificacion < 700:               # Preguntamos si la calificación es menor a 700
    print("Ves por no estudiar")     # Si es menor a 700 muestra esto
elif calificacion == 700:             # Preguntamos si la calificación es igual a 700
    print("Panzazoooo we")           # Si la calificacción es igual a 700 entonces pasó pero de panzazo
elif calificacion  > 1000:           # Compara si la calificación es mallor a 1000 que es el máximo puntaje del examen
    print("MIENTESSS")               # Si dIce que es mallor al maximo puntaje está mintiendo
else:                                # Si no se cumple ninguno de los casos anteriores (el if y los elif) pasa al else 
    print("Felicidade pasa por tu certificado") # Es una accoón que se ejecuta por default aal no cumplir ninguna de las condiciones 


# Ejemplo 2 con edades

# Declaramos las variables

edad = input("Introduce tu edad ")                    # Introducimos la información desde el teclado
edad = int(edad)                                      # hay que castearlo de tipo string a tipo int (entero)

# Estructura IF
if edad > 18 and edad < 100:                          # Comprobamos la condición de que la edad proporcionada la cumpla
    print("Bienvenido al mamitassssss ")              # Si la cumple entonces ejecuntamos esto, si no pasamos al siguiente elif 
elif edad > 0 and edad < 18:                          # Volvemoa acomprobar que si la edad cumple la condición
         print("no puedes comprar cigarros ")         # Si la cumple entonces ejecuntamos esto, si no pasamos al siguiente elif
elif edad > 0 and edad < 100:                         # Volvemos a ver si sicumple la condicion 
    print("si vienes acompañado de tus abuelitos si te podemos fiar") # Si la cumple entonces ejecuntamos esto, si no pasamos al siguiente elif
elif edad < 0:                                        # Otra vez vemos si cumple esta otra condición 
    print("ni que fueras viajero del tiempo")         # Si la cumple entonces ejecuntamos esto, si no pasamos al else, que es la instrucción
else:                                                 # si no se cumplió ninguna de las condiciones anteriores 
    print("Ya deberías estar empujando margaritas")   # Dice esto


# En paython no existe el switch case, en su lugar se puede usar el ELIF 
# El elif lleva una condición para probar tambien, en cambio en el else se va ejecuatar si o si sin comprobar otra 