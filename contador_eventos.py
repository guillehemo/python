# a tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado,
# expresándolo en horas y minutos. 
# Las horas van de 0 a 23 y los minutos de 0 a 59. 
# El resultado debe ser mostrado en la consola.

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

total_minutos = (mins + dura)%60

total_horas = (hour + round(dura/60))%24

print(total_horas,":",total_minutos)