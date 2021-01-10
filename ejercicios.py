# En este ejemplo se solicitara la introduccion de datos
dato = input('Digite su Nombre: ')
dato1 = input('Diguite su apellido: ')
print(dato, dato1)

# Crear una variable, una lista, luego digitar un dato, verificar si
# en la lista y mostrar el dato introducido
var = input('Ingrese un Dato: ')
lista = ["Hola", "Mundo", "Chanchito", "Feliz", "Dragones"]
if lista.count(var) > 0:
    print('El dato existe :', var)
else:
    print('El dato no existe :', var)

# Ejercisio, definir una variable, solicitar la introduccion de un dato
# definir una lista y evaluar si el dato digitado existe en la lista creada,
# luego imprimir un mensaje diciendo si existe el dato o si no existe
nombre = input('Digite su Nombre : ')
listnombre = ["Daniela", "Ovidio", "Silvia", "Daniel", "Dayana"]
if listnombre.count(nombre) > 0:
    print('Si existe este nombre :' , nombre)
else:
    print('Este nombre no existe :' , nombre)

# Ej. de Sumas, primero se crean las variables se convierten a numeros enteros
primero = input('Ingrese el Primer Numero :')
segundo = input('Ingrese el segundo Numero :')
pnumero = int(primero)
snumero = int(segundo)
print(pnumero+snumero)

# Otra forma seria evaluando el valor digitado, si no es numero tratar de
# convertirlo a numero y si no se puede mandar un mensaje de que no se 
# digitaron numeros
numero = input('Ingrese el Primer Numero :')
try:
    numero = int(numero)
except:
    numero = 'Chanchito Feliz'

numero1 = input('Ingrese el Segundo Numero :')
try:
    numero1 = int(numero1)
except:
    numero1 = 'Chanchito Feliz'

if numero == 'Chanchito Feliz' or numero1 == 'Chanchito Feliz':
    print('Los datos digitados no son numeros, intente digitando numero')
else:
    print(numero+numero1)

# Otra forma seria la siguiente
numero = input('Digite el primer numero :')
try:
    numero = int(numero)
    numero1 = input('Digite el segundo numero :')
    try:
        numero1 = int(numero1)
        print(numero+numero1)
    except:
        print('Los datos digitados no son numero, intente digitando numeros')
except:
    print('Los datos digitados no son numero, intente digitando numeros')

# Ej. de como detener la ejecucion al momento de digitar mal el dato
numero = input('Ingrese el Primer Numero :')
try:
    numero = int(numero)
except:
    numero = 'chanchito feliz'

if numero == 'chanchito feliz':
    print('Los datos digitados no son numero')
    exit()

numero1 = input('Ingrese el Segundo Numero :')
try:
    numero1 = int(numero1)
except:
    numero1 = 'Chanchito Feliz'

if numero1 == 'Chanchito Feliz':
    print('Los datos digitados no son numeros')
    exit()

print(numero+numero1)

# Agregando mas operaciones a la calculadora
numero = input('Digite el primer Numero: ')
try:
    numero = int(numero)
except:
    numero = ('No es numero')

if numero == ('No es numero'):
    print('El dato digitado no es un numero, intente digitando un numero entero')
    exit()

numero1 = input('Digite el segundo numero: ')
try:
    numero1 = int(numero1)
except:
    numero1 = ('No es numero')

if numero1 == ('No es numero'):
    print('El dato digitado no es un numero, intente digitando un numero entero')
    exit()

operador = input('Digite el tipo de Operacion: ')

if operador == '+':
    print('Suma: ', numero + numero1)
elif operador == '-':
    print('Resta: ', numero - numero1)
elif operador == '*':
    print('Multiplicacion: ', numero * numero1)
elif operador == '/':
    print('Divicion: ', numero / numero1)
else:
    print('El simbolo ingresado no es Valido')