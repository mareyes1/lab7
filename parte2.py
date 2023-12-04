"""
Script para monitorear un proceso de forma automática.
Revisa periódicamente el estado del proceso. Si se cierra se vuelve a abrir.
"""
import os
import subprocess
import time
import sys
import psutil

def iniciar_proceso(nombre_proceso, comando):
    try:
        # Iniciar proceso
        subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Proceso '{nombre_proceso}' iniciado.")
    except Exception as e:
        print(f"No se pudo iniciar el proceso '{nombre_proceso}': {e}")

def monitorear_proceso(nombre_proceso, comando):
    while True:
        # Comprobar si proceso está en ejecución, utilizando psutil
        proceso_en_ejecucion = any(
            psutil.Process(pid).name() == nombre_proceso
            for pid in psutil.pids()
        )

        if not proceso_en_ejecucion:
            # Si proceso se cierra volver a iniciarlo
            print(f"El proceso '{nombre_proceso}' se ha cerrado. Reiniciando...")
            iniciar_proceso(nombre_proceso, comando)

        # Esperar intervalo de tiempo para verificar
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_proceso> <comando>")
        sys.exit(1)

    nombre_proceso = sys.argv[1]
    comando = sys.argv[2]

    # Iniciar proceso
    iniciar_proceso(nombre_proceso, comando)

    try:
        # Monitorear proceso
        monitorear_proceso(nombre_proceso, comando)
    except KeyboardInterrupt:
        print("Monitoreo del proceso detenido.")
