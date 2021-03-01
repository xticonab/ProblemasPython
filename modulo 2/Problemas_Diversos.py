print('Problema 1')

def listar_alumnos(cantidad_alumnos):
    lista_alumnos = [] 
    for i in range(cantidad_alumnos):
        alumno = {}
        alumno['nombre'] = input('Ingrese el nombre del alumno {}: '.format(i+1))
    
        alumno['nota1'] = float(input('Ingrese una nota entre 0 y 10: '))
        alumno['nota2'] = float(input('Ingrese una nota entre 0 y 10: '))
        alumno['nota3'] = float(input('Ingrese una nota entre 0 y 10: '))
        lista_alumnos.append(alumno)
        
    return lista_alumnos
print()

n = int(input('Cantidad de alumnos a ingresar: '))
print(n)


lista_alumnos = listar_alumnos(n)
print(lista_alumnos)

while True:
    try:
        nota = float(input('Introduce la nota(0-10): '))
        
        if nota >=0 and nota <= 10:
            break
        else:
            print('nota fuera del rango')
    except:
        print('Ha ocurrido un error, introduce bien la nota')

