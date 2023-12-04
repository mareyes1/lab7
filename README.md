# Laboratorio 7 Python Scripting
## Obtener información relevante de un proceso
Se utiliza además del módulo `os` se utiliza también el módulo `psutil`, el cual se debe instalar previamente por medio de `pip install psutil`.

Se crea una función denominada `obtener_informacion_proceso` la cual recibe el ID del proceso (o PID) y crea un objeto `proceso` mediante una instancia con `psutil.Process(pid)`. A partir de ahí, por medio de los atributos de proceso obtenidos utlizando el módulo de `psutil`, se almacena en variables la información requerida del proceso, como su nombre, ID, parent process ID, usuario, uso de recursos, estado y ruta al ejecutable.

Debido al uso de módulos estándar de Python, el script corre indistintamente en diferentes plataformas.

A continuación se muestra la salida del programa.

![resultados1](https://raw.githubusercontent.com/mareyes1/Lab2/main/parte1_lab7.png)
