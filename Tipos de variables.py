
#Sting- cadena de texto (palabras)
nombre = "Elias 🤣" # Emoji con windows y un punto
print(nombre)       # Imprimimos lo que tiene la varaiable  

#Enteros - Números sin punto decimal
edad = 26     # Son números sin decimales para operaciónes matemáticas 
edads = "26"  # En este caso aunque es un número por estar entre comillas es una variable del tipo string 

   #ejemplo de diferencia entre 26 y "26"

print( edads + edads )  # "26" lo toma como una variable del tipo strin es decir un texto 
print( edad + edad )    # 26 lo toma como variable entera como numeros matemáticos
#print (edads + edad)   # Da error por que sería una suma de diferentes tipos de variable, una String mas una entero 
                        # Es decir sumar una palabra mas un número 

# Flotante - Números con punto decimal, por ejemplo el número pi
pi = 3.1416           # Es un número pero cn decimales 

# Casteo - Transforma de un tipo de variable a otro tipo de variable cierta variable 
edad = float (edad)   # En este caso transforma el numero de la edad que es del tipo entero a una edad Flotante  
                      # es decir numero con decimal, para hacer esto a la variable se le asigna "tipo de variable a convertir (Variable)""

print(pi)             # Imprime el número flotane Pi
print(edad)           # Imprime el numero flatante resultante del casteo de la variable edad 

print(type(nombre), type (edad))  #Usa type para saber de que tipo de variable es la variable 


# BOOL - Booleano - SI O NO 
tegusto = False       # A la variable se le asinan solo dos tipod de valores 
legustas = False

print(legustas)       # Imprime el valor booleano de la variable 


