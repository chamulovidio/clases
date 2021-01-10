# Ej. de como definir una funcion
def mifuncion():
    print('Mi primera Funcion')

mifuncion()

# Utilizando argumentos dentro de las funciones
def imprimedato(argumentouno):
    print('Mi argumento es :', argumentouno)

imprimedato('parametro 1')

# usando varios argumentos en la funcion
def imprimedato(nombre, apllido):
    print('El nombre completo es :', nombre, apllido)

imprimedato('Ovidio', 'Chamul')

# Tambien podemos definir en nuestra funcion solo un agumento pero mandarle 
# varios parametro, y nos generara un tupla y no podremos modificar los datos
# solo tememos que ponerle un asterisco antes del argumento, Ej.
def imprimedato(*nombres):
    print('Los nombres son los siguientes: ', nombres)

imprimedato('juan', 'jaime', 'mario', 'daniel', 'orlando')

# Ej de como poder acceder a los datos generados por nuestra funcion
def imprimedato(*nombre):
    print('El nombre seleccionado es :', nombre[1])
imprimedato('juan', 'jaime', 'mario', 'daniel', 'orlando')

# Otra forma de poder acceder a los a los datos de la funcion seria
# utilizando el nombre de cada argumento sin importar el orden
# en que hayan sido definidos en la funcion, Ej.
def nombrecompleto(apellido, nombre):
    print('El nombre completo es :', nombre, apellido)
nombrecompleto(nombre = 'oscar', apellido = 'Galdamez')

# Como acceder a los datos de la funcion utilizando la sintaxis de Diccionario
def nombrecom(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombrecom(nombre = 'Oscar', apellido = 'Galdamez')

# Cuando a una funcion no se le define un argumento ella imprime el valor 
# que se le asigno, ej.
def mifuncion(argumento = 'Chanchito'):
    print(argumento)

mifuncion('Batman')
mifuncion()

# Tambien podemos acceder a los elementos cuando en la funcion hemos 
# definido una lista, Ej.
def mifuncionlista(lista):
    for el in lista:
        print(el)

mifuncionlista(['chanchito', 'feliz'])

# Tambien podemos crear variables en nuestra funcion, ej.
def concatenanombre(lista):
    i = ' '
    for el in lista:
        i = i + el + ' '
    return i

nombre = concatenanombre(['Ovidio', 'Mejia'])
print(nombre)

# Ej. de Recursividad
def Recursion(a):
    if(a - 1):
        return a
    print(a)
    Recursion(a - 1)

Recursion(6)