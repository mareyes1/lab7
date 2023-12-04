# Laboratorio 7 Python Scripting
## 1 Obtener información relevante de un proceso
Archivo `parte1.py`: Se utiliza además del módulo `os` se utiliza también el módulo `psutil`, el cual se debe instalar previamente por medio de `pip install psutil`.

Se crea una función denominada `obtener_informacion_proceso` la cual recibe el ID del proceso (o PID) y crea un objeto `proceso` mediante una instancia con `psutil.Process(pid)`. A partir de ahí, por medio de los atributos de proceso obtenidos utlizando el módulo de `psutil`, se almacena en variables la información requerida del proceso, como su nombre, ID, parent process ID, usuario, uso de recursos, estado y ruta al ejecutable.

Debido al uso de módulos estándar de Python, el script corre indistintamente en diferentes plataformas.

A continuación se muestra la salida del programa.

La forma de ejecutarlo es:

`>>> python3 ./parte1.py <pid>`

![resultados1](https://raw.githubusercontent.com/mareyes1/Lab2/main/parte1_lab7.png)

Como se puede observar, la salida es conforme a lo esperado. De acuerdo con estos resultados, se puede afirmar que por medio de Python se puede realizar con los mismos resultados la resolución de problemas de scripting que había sido inicialmente abordada en el curso con bash. Se puede concluir que Python es más intuitivo a la hora de escribir código debido a su sintaxis, así como más poderoso debido a las bibliotecas estándar con las que cuenta, como por ejemplo `subprocess`, `psutil` u `os`, que al mimsmo tiempo permiten su portabilidad en múltiples plataformas dado no que requieren en su implementación particularidades en relación con el sistema operativo sino que esto es transparente para el programador en cuanto a la implementación de estos módulos "por debajo".

## 2 Automatizar monitoreo de un proceso
Archivo `parte2.py`: En el script se utiliza un bucle infinito para monitorear continuamente el estado del proceso. Se hace uso de la bliblioteca `psutil` para obtener información del proceso en ejecución.

Se verifica si el proceso está en ejecución comparando el ID del proceso con la lista de procesos activos. Si se detecta que el proceso se ha cerrado, se utiliza `subprocess.Popen` para reiniciarlo. Se deja un tiempo de espera de 5 segundos para las verificaciones de estado periódicas.

A continuación se muestra como se visualiza en la terminal la ejecución del script, donde se vuelve a abrir el proceso y finalmente se detiene el monitoreo al interrumpir la ejecución del script.

![resultados2](https://raw.githubusercontent.com/mareyes1/Lab2/main/parte2_lab7.png)
