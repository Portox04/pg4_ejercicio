#Practica #4

#Ejercicio 2


pasajeros = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],]

def intro_passanger():
    for x in range(len(pasajeros)):
        y = len(pasajeros[x])
        for z in range(y):
            print(f"Coloque la cantidad de Pasajeros de dia {x+1} en el servicio {z+1}: ")
            pasajeros[x][z] = int(input())
            while True:
                if pasajeros[x][z] > 60:
                    pasajeros[x][z] = int(input(f"La capacidad maxima del bus es de 60 por favor coloca un dato valido: \n"))
                else:
                    break

def prom_all():
    viaje = []
    viaje_all = 0
    for viaje_actual in pasajeros:
        suma_pasajeros = sum(viaje_actual)
        viaje.append(suma_pasajeros)
        viaje_all += suma_pasajeros  
    viaje_prom = viaje_all / len(pasajeros)  
    print(f"El promedio de pasajeros por dia es de: {viaje_prom}")

def prom():
    viaje = []
    for viaje_actual in pasajeros:
        suma_pasajeros = sum(viaje_actual)
        viaje.append(suma_pasajeros)
    for i in range(len(viaje)):
        pasajeros_prom = viaje[i] / len(pasajeros[i])
        print(f"La cantidad de pasajeros promedio en el viaje {i+1} es de: {pasajeros_prom}")
        
def best_travel_day():
    for dia in range(len(pasajeros)):
        max_pasajeros = 0
        mejor_viaje = 0
        for viaje in range(len(pasajeros[dia])):
            cantidad_pasajeros = pasajeros[dia][viaje]
            if cantidad_pasajeros > max_pasajeros:
                max_pasajeros = cantidad_pasajeros
                mejor_viaje = viaje + 1
        print(f"El dia {dia+1}, el mejor servicio es el {mejor_viaje} con {max_pasajeros} pasajeros.")

def bad_day():
    min_pasajeros_total = 999999  
    dia_menos_pasajeros = 0
    for dia in range(len(pasajeros)):
        total_pasajeros_dia = sum(pasajeros[dia])
        if total_pasajeros_dia < min_pasajeros_total:
            min_pasajeros_total = total_pasajeros_dia
            dia_menos_pasajeros = dia + 1
    if min_pasajeros_total == 0:
        print("Ningún pasajero se montó en ningún viaje.")
    else:
        print(f"El día con menos pasajeros fue el día {dia_menos_pasajeros} con un total de {min_pasajeros_total} pasajeros.")


    

intro_passanger()
prom_all()
prom()
best_travel_day()
bad_day()
