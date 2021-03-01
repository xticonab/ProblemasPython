print('Problema 1')

n = int(input('Introduce un número entero entre 1 y 10: '))

file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')

for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()


print('Problema 2')

n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'

try: 
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())


print('Problema 3')
n = int(input('Introduce un número entero entre 1 y 10: '))
m = int(input('Introduce otro número entero entre 1 y 10: '))
nombre = 'tabla-' + str(n) + '.txt'
try: 
    f = open(nombre, 'r')
except:
    print('No existe el fichero con la tabla del ', n)
else:
    lineas = f.readlines()
    print(lineas[m - 1])

