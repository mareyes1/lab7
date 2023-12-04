"""
Script para obtener información de un proceso con su ID
Se utiliza los módulos os y psutil
"""
import os
import psutil
import sys

def info_proceso(pid):
    try:
        proceso = psutil.Process(pid)

        # Obtener información del proceso
        nombre_proceso = proceso.name()
        pid_proceso = proceso.pid
        ppid_proceso = proceso.ppid()
        usuario_propietario = proceso.username()
        uso_cpu = proceso.cpu_percent(interval=1)
        consumo_memoria = proceso.memory_info().rss
        estado_proceso = proceso.status()
        path_ejecutable = proceso.exe()

        # Imprimir información del proceso
        print("========== Información del proceso ==========")
        print(f"Nombre del proceso: {nombre_proceso}")
        print(f"ID del proceso: {pid_proceso}")
        print(f"Parent process ID: {ppid_proceso}")
        print(f"Usuario propietario: {usuario_propietario}")
        print(f"Porcentaje de uso de CPU: {uso_cpu}%")
        print(f"Consumo de memoria: {consumo_memoria} bytes")
        print(f"Estado del proceso: {estado_proceso}")
        print(f"Path del ejecutable: {path_ejecutable}")

    except psutil.NoSuchProcess:
        print(f"Error: No se encontró proceso con el PID {pid}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: >>> python3 parte1.py <PID>")
        sys.exit(1)

    pid_proceso = int(sys.argv[1])
    info_proceso(pid_proceso)
