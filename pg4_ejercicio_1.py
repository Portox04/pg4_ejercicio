#Practica #4

#Ejercicio 1

nota =[[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],]

def colocacion_notas(notas):
    numero_fila = len(notas)
    for filas in range(numero_fila):
        numero_columna = len(notas[filas])
        for columnas in range(numero_columna):
            print(f"Coloque la nota del estudiante {columnas+1} del curso {filas+1}: ")
            notas[filas][columnas] = int(input())

def nota_final():
    notas_finales = []
    notas_promedio = []
    notas_all = 0
    for fila in nota:
        suma_notas = sum(fila)
        notas_finales.append(suma_notas)
        promedio = suma_notas/len(fila)
        notas_promedio.append(promedio)
    for i in range(len(notas_finales)):
        print(f"La nota promedio del curso {i + 1} es de: {notas_promedio[i]}")

def nota_prom():
    notas_finales = []
    notas_all = 0
    for fila in nota:
        suma_notas = sum(fila)
        notas_finales.append(suma_notas)
    for i in range(len(notas_finales)):
        notas_all+=notas_finales[i]
    notas_prom = notas_all/15
    print(f"El promedio de las notas es de: {notas_prom}")

def aprobados():
    aprobados_1 = 0
    aprobados_2 = 0
    aprobados_3 = 0
    for columna in range(len(nota[0])):
        if nota[0][columna] >= 70:
            aprobados_1 +=1
    for columna in range(len(nota[1])):
        if nota[1][columna] >= 70:
            aprobados_2 +=1
    for columna in range(len(nota[2])):
        if nota[2][columna] >= 70:
            aprobados_3 +=1
            
    prom_aprobados_1 =(aprobados_1*100)/5
    prom_aprobados_2 =(aprobados_2*100)/5
    prom_aprobados_3 =(aprobados_3*100)/5
    print(f"El promedio de aprobado en el curso 1 es de {prom_aprobados_1}")
    print(f"El promedio de aprobado en el curso 2 es de {prom_aprobados_2}")                    
    print(f"El promedio de aprobado en el curso 3 es de {prom_aprobados_3}")

def notas_max_min():
    nota_menor = [100,100,100]
    nota_mayor = [0,0,0]
    for fila in range(len(nota)):
        num_colunm = len(nota)
        for columna in range(num_colunm):
            if nota[fila][columna] > nota_mayor[fila]:
                nota_mayor[fila]=nota[fila][columna]
            if nota[fila][columna] < nota_menor[fila]:
                nota_menor[fila]=nota[fila][columna]
    for x in range (len(nota_menor)):
        print(f"Del curso {x+1} la nota mayor es {nota_mayor[x]} y la menor es {nota_menor[x]}")


colocacion_notas(nota)
nota_final()
nota_prom()
aprobados()
notas_max_min()

