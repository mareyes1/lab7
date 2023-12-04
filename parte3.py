"""
Script que crea una herramienta para monitorear automáticamente el consumo de CPU y memoria de un proceso
Recibe como parámetro un ejecutable y ejecuta el binario recibido
Periódicamente lee y registra el consumo de CPU y memoria y lo gráfica en el tiempo con matplotlib
"""

import os
import subprocess
import psutil
import time
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

def ejecutar_proceso(binario):
    # Ejecutar el binario
    proceso = subprocess.Popen(binario, shell=True)
    return proceso

def monitorear_proceso(proceso, intervalo, log_file):
    tiempos = []
    uso_cpu = []
    uso_memoria = []

    while proceso.poll() is None:
        # Obtener información del proceso
        info_proceso = psutil.Process(proceso.pid)
        
        # Registrar tiempo actual
        tiempo_actual = datetime.now()
        tiempos.append(tiempo_actual)
        
        # Registrar consumo de CPU y memoria
        uso_cpu.append(info_proceso.cpu_percent())
        uso_memoria.append(info_proceso.memory_info().rss)

        # Esperar intervalo especificado
        time.sleep(intervalo)

    # Escribir datos en archivo de registro
    with open(log_file, 'w') as f:
        f.write("Tiempo, Uso de CPU (%), Uso de Memoria (bytes)\n")
        for tiempo, cpu, memoria in zip(tiempos, uso_cpu, uso_memoria):
            f.write(f"{tiempo},{cpu},{memoria}\n")

def graficar_datos(log_file):
    # Leer datos de archivo de registro
    tiempos = []
    uso_cpu = []
    uso_memoria = []

    with open(log_file, 'r') as f:
        next(f)  # Saltar primera línea de encabezado
        for linea in f:
            #tiempo, cpu, memoria = map(float, linea.strip().split(','))
            tiempo, cpu, memoria = linea.strip().split(',')
            #tiempos.append(datetime.strptime(tiempo, "%Y-%m-%d %H:%M:%S.%f"))
            #tiempos.append(datetime.utcfromtimestamp(tiempo))
            tiempos.append(tiempo)
            #tiempo = datetime.strptime(tiempo, "%Y-%m-%d %H:%M:%S.%f")
            #tiempos.append((tiempo - datetime(1970, 1, 1)).total_seconds())
            uso_cpu.append(float(cpu))
            uso_memoria.append(float(memoria))

    # Convertir formato de tiempo a datetime
    tiempos = [datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f") for t in tiempos]

    # Graficar los datos
    #plt.figure(figsize=(10, 5))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(tiempos, uso_cpu, label='Uso de CPU (%)', marker='o')
    ax.plot(tiempos, uso_memoria, label='Uso de Memoria (bytes)', marker='o')
    ax.set_title('Monitoreo de CPU y Memoria')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Valor')
    ax.legend()
    ax.grid(True)

    ax.xaxis.set_major_locator(mdates.SecondLocator(interval=20))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    if len(os.sys.argv) != 3:
        print("Uso: python parte3.py <binario a ejecutar> <intervalo de monitoreo>")
        os.sys.exit(1)

    binario = os.sys.argv[1]
    intervalo = float(os.sys.argv[2])
    log_file = "registro_monitoreo.csv"

    # Ejecuta el proceso
    proceso = ejecutar_proceso(binario)

    try:
        # Monitorea el proceso y guarda los datos en un archivo
        monitorear_proceso(proceso, intervalo, log_file)
    except KeyboardInterrupt:
        print("Monitoreo del proceso detenido.")

    # Grafica los datos al finalizar el proceso
    graficar_datos(log_file)
