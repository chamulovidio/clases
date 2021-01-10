# Aqui va un comentario
if 5 > 3:# Aqui va otro comentario, este es el ejemplo de escrivir comentarios en codigo del programaS
    print('5 es mayor 3')

if 3 > 5:
     print('Esto no se imprime porque no cumple la condicion, al correr el programa no mostrara nada')

# Definicion de Variables
x = 5
y = ('Ovidio')
print(x, y)

email = ('ovidio@gmail.com')
print(email)

# Definicion de multiples variables en una solo linea Ej.
a, b, c = 'La', 'Le', 3
print(a, b, c)

# Se pueden crear muchas o multiples variables que contenga el mismo valor Ej.
valor1 = valor2 = valor3 = valor4 = 'Ovidio'
print(valor1, valor2, valor3, valor4)

# Ejemplo de concatenacion de variables de tipo str o caracteres alfabeticos
inicio = 'Hola'
final = 'Mundo'
print(inicio + ' ' + final)

# Ejemplo para definir un String
# Un String: es una palabra o lo que conocemos como datos alfabeticos
palabra = 'Hola Mundo' # Este es un String
oracion = "Hola Mundo Comilla Doble" # Este es un String Comilla Doble

entero = 20         # Integer
condecimal = 20.2   # float
complejo = 1j       # complejo
print(palabra, oracion, entero, condecimal, complejo)

# Ejemplo para definicion de lista
lista = []      # Las listas se definen vacias
print(lista)

# Ejemplo para introducirle valores a la lista
lista = [1, 2, 3]
print(lista)

# Ejemplo de como manipular una lista ya sea agregandole o quintandole valores
lista = [1, 2, 3]
lista.append(4) # El metodo append permite aumentarle un valor a la lista
print(lista)

# Ejemplo de como eliminar los valores de una lista y dejarla vacia
lista = [1, 2, 3]
lista.clear()   # El metodo clear elimina los valores de la lista
print(lista)

# Ejemplo de como copiar una lista
lista = [1, 2, 3]
lista2 = lista.copy()   # El metodo copy realiza una copia de una lista
print(lista, lista2)

# Ej. de como copiar una lista y agregarle un valor adicional a lista del ejemplo anterior
lista = [1, 2, 3]
lista2 = lista.copy()
lista.append(4)
print(lista, lista2)

# Ej. de como acceder al primer valor de la lista
# Siempre el primer valor de la lista ocupara el lugar cero
print(lista[0])

# para Acceder al segundo valor de la lista, sera de la siguiente forma
print(lista[1])

# Para acceder al tercer valor de la lista, sera de la siguiente forma
print(lista[2])

# Para Acceder al primer valor de lista2, sera de la siguiente forma
print(lista2[0])

# Ejemplo de como acceder al cuarto valor de lista
print(lista[3])

# Una lista tambien puede contener texto o string, Ej.
lista = ['Hola', 'Mundo', 'chanchito']
print(lista)

# Si quiero acceder al primer valor de lista, seria de la siguiente forma
print(lista[0])

# Ej. de como podemos eliminar el ultimo Elemento de la lista
lista.pop() # El metodo pop() nos permite eliminar el ultimo elemento de la lista
print(lista)

lista = ['Hola', 'Mundo', 'Chanchito', 'Feliz']
print(lista)

# Ej. de como eliminar un elemento cualquiera de una lista
lista.remove('Chanchito')   # El metodo remove permite eliminar cualquier elemento de una lista
print(lista)

lista = ['Hola', 'Mundo', 'Chanchito', 'Feliz']
print(lista)

# Ej. de como poner al reves los elementos de una lista
lista.reverse() # El metodo reverse permite poner al reves los elementos de la lista
print(lista)

#Ej. de como ordenar los datos de una lista en orden alfabetichoppo
lista.sort()    # El metodo sort() nos permite ordenar los elementos de una lista
print(lista)

# Ejemplro de como crear una tupla, la tupla es similar a la lista 
# Con la diferencia que la tupla no se puede modificar
tupla = ('Hola', 'Mundo', 'Somos', 'tupla')
print(tupla)

# En la tupla tambien se puede utilizar el metodo count()
# Nos permite saber cuantas veces se repite un elemento en la tupla Ej.
print(tupla.count('Mundo'))

# En las tuplas tambien podemos utilizar el metodo index()
# Nos permite saber la posicion de un elemento dentro de la tupla Ej.
print(tupla.index('tupla'))

# Las tuplas no se pueden modificar y si queremos agregarle un elemento
# tenemos que convertirla en una lista Ej.
listadetupla = list(tupla)
listadetupla.append('Feliz')
print(listadetupla)

# Tambien podemos trabajar con los rangos Ej.
rango = range(6)    # el metodo range() es el que nos permite crear un rango
print(rango)

# Ejemplo de como crear los Diccionarios
diccionario = {
    "nombre": "chanchito Feliz",
    "raza": "persa",
    "edad": 5
}
print(diccionario)

# Otro Ej. de Diccionario
diccionario1 = {
"Nombre1": "Daniela",
"Nombre2": "Elizabeth",
"Apellido1": "Gutierrez",
"Apellido2": "Vasquez",
"Edad": 5,
"Año de Nacimiento": 2015
}
print(diccionario1)

# Ej. de como acceder a un valor del diccionario
print(diccionario1["Nombre1"])

# Tambien podemos acceder a un valor sin utilizar los corchetes, se puede untilizar un metodo Ej.
print(diccionario1.get('Nombre1'))

# Ej. de como puedo cambiar el valor a un elemento de un diccionario
diccionario["nombre"] = "chanchito triste"
print(diccionario)

# En los diccionarios tambien se puede utilizar len() para poder conocer
# el numero de elemento que tiene un diccionario Ej.
print(len(diccionario))

print(len(diccionario1))

# Ej. de como agregar otro valor al diccionario
diccionario1["Mes Nac"] = "Enero"
print(diccionario1)

# Ej. de como eliminar un valor o elemento de la lista
diccionario1.pop("Mes Nac")
print(diccionario1)

# Ej. de como eliminar el ultimo valor o elelemento de la lista
diccionario1.popitem()
print(diccionario1)

# Otro Ej. de como eliminar un valor o elemento de un diccionario
del diccionario1["Edad"]
print(diccionario1)

# Ejemplo de como copiar un diccionario 
diccionario2 = diccionario1.copy()
print(diccionario1, diccionario2)

# Ejemplo de como copiar un diccionario y a la vez agregarle un valor 
# al diccionario copiado
diccionario2 = diccionario1.copy()
diccionario2["Edad"] = 5
print(diccionario1, diccionario2)

# Ej. de como eliminar todos los valores o elementos de la lista
diccionario2.clear()
print(diccionario2)

# Otro Ej. de como copiar un diccionario es el siguiente
copiadiccionario = dict(diccionario1)
print(copiadiccionario)

# Ej. de como crear diccionarios anidados
hijos = {
    "hijo1" : {
        "nombre" : "juan",
        "apellido" : "rivas"
    },
    "Hijo2" : {
        "nombre": "mario",
        "Apellido": "aguilar"
    }
}
print(hijos)

# Otra forma de como podemos crear los diccionario anidados es 
# creando variables
hijo1 = {
    "nombre" : "julio",
    "apellido" : "campos"
}

hijo2 = {
    "nombre" : "jorge",
    "apellido" : "servellon"
}
familia = (hijo1, hijo2)
print(familia)

# Otra forma de como crear un diccionario es con el metodo dict()
# Para eso hay que crear una variable
perrito = dict(nombre = "chester")
print(perrito)

# Ej. de si queremos agregarle mas elementos o datos al diccionario
perrito = dict(nombre = "chester", edad = 2)
print(perrito)

# los datos booleanos solo pueden terner dos valores que son
# verdadero o falso
booleanoVerdadero = True
booleanoFalso = False
print(booleanoVerdadero, booleanoFalso)

# Utilizacion de la instruccion if
if 3 < 5:
    print("tres es menor que cinco")

if 2 == 2:
    print(" dos es igual a dos")

if 2 == 3:
    print("dos es igual a tres")    # en esta evaluacion no imprime nada porque no se cumple la condicion

if 2 > 5:
    print(" dos es mayor a cinco")  # en esta evaluacion no imprime nada porque no se cumple la condicion

if 5 > 2:
    print("cinco es mayor que dos") # esta evaluacion si se cumple por lo que imprimira el resultado

if 2 != 2:
    print("dos es distinto a dos")  # Esta evaluacion no imprime nada porque no se cumple la condicion

if 3 != 2:
    print("tres es distinto a dos") # Esta evaluacion si se cumple por lo que imprimira el resultado

if 6 >= 3:
    print("seis es mayor o igual que tres") 

if 3 >= 3:
    print("tres es mayor o igual que tres")

if 2 < 5:
    print("dos es menor o igual que cinco")

if 2 <= 2:
    print("dos es menor o igual que dos")

# Ejemplo del uso de la funcion elif
if 2 < 5:
    print("dos es menor que cinco")
elif 2 > 5:
    print("dos es mayor que cinco") # Esta evaluacion no se cumple por lo que no imprimira nada

if 3 > 6:
    print("tres es mayor que seis") # no imprime nada porque no se cumple la condicion
elif 3 < 6:
    print("tres es menor que seis")

# Ejemplo del uso de la funcion else
if 2 > 4:
    print("dos es mayor que cuatro") # no imprime nada porque no cumple la condicion
elif 3 > 8:
    print("tres es mayor que ocho") # no imprime nada porque no cumple la condicion
else:
    print("niguna de las anteriores se cumple")

# Ej. del udo de if solamente con un else 
if 8 < 3:
    print("ocho es mayor que tres")
else:
    print("no se cumple la evaluacion anterior")

# Ej. de uso de if cortos y ternarios
if 8 > 3: print("if de una sola linea")

# Ej. del uso de if y else en una sola linea
print("Se ejecuta cuando devuelve verdadero") if 3 < 5 else print("se ejecutna cuando debuelve falso")

# Ej. del uso de los operadores and y or
# si utilizamos el operador and se tienen que cumplir las dos evalucaiones 
# para que se ejecute la isntruccion
if 2 < 5 and 3 > 2:
    print("ambas evaluaciones devuelven verdadero")

# Si una de las evaluaciones no se cumple no se ejecutara la isntruccion
if 2 < 5 and 3 < 2:
    print("hay una evaluacion que es falsa por lo que no imprime nada")

# Ej. del operador or, aqui se ejecuta la instruccion si una de las
# Evaluaciones se cumple
if 1 < 0 or 1 > 0:
    print("una de las evaluaciones devuelve verdadero")

# Si las dos evaluaciones se cumplen o devuelven verdadero se ejecuta la instruccion
if 1 > 0 or 2 > 1:
    print("las dos evaluaciones se cumplen")

# Si las dos evaluaciones no se cumplen o devuelven falso no se
#ejecuta la instruccion Ej.
if 2 < 1 or 5 < 3:
    prin("las dos evalucaniones no se cumplen o devuelven falso")
