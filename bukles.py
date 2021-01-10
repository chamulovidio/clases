# Uilizacion de while
i = 0
while i < 5:
    print(i)
    i += 1

# Ejemplo de como poder detener el bokle
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

# Ej. del uso de continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# uso for y loop, el uso de estos se utiliza en listas, tuplas y diccionarios
# crear una lista que se llame usuarios, crear una variable que se llame 
# usuario y aplicar el for y loop, luego imprimie el contenido de la lista
usuarios = ['cesar', 'felipe', 'roberto', 'nicolas']
for usuario in usuarios:
    print(usuario)

# Este es otra forma de usuar el for
usuario = ['chanchito feliz']
for c in usuario:
    print(c)

# Tambien podemos acceder a un string o cadena de caractereres ej.
# crear una variable y asignarle un strig luego imprimir el contenido
# de la variable
usuario = 'chanchito feliz'
for c in usuario:
    print(c)

# En for tambien se puede usar el break, Ej.
usuarios = ['cesar', 'felipe', 'roberto', 'nicolas']
for usuario in usuarios:
    if usuario == 'roberto':
        break  
    print(usuario)

# En for tambien se puede utilizar continue
usuarios = ['cesar', 'felipe', 'roberto', 'nicolas']
for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario)

# Utilizacion del range
for x in range(6):
    print(x)

# Otro ejemplo de rango o range es el siguiente
for a in range(2, 6):
    print(a)

# En el rango si le agragamos un tercer numero separado por coma
# le estamos indicando que se aumente de acuerdo al tercer numero
# Ej. si el tercer numero es 5, se aumentara de 5 en 5
for b in range(5, 30, 5):
    print(b)

# Tambien podemos aplicar un else en el rango y este se ejecutara hasta
# que haya completado todos los datos del rango Ej.
for b in range(10, 50, 10):
    print(b)
else:
    print('Hemos terminado el proceso')

# Utilizando un for dentro de otro for Ej.
usuarios = ['cesar', 'felipe', 'roberto', 'nicolas']
edades = [24, 25, 26, 27]
for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)
