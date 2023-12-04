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

Se debe ejecutar de la siguiente forma:

`>>> python3 ./parte2.py <nombre del proceso> <comando para ejecutarlo>`

A continuación se muestra como se visualiza en la terminal la ejecución del script, donde se vuelve a abrir el proceso y finalmente se detiene el monitoreo al interrumpir la ejecución del script.

![resultados2](https://raw.githubusercontent.com/mareyes1/Lab2/main/parte2_lab7.png)

## 3 Log de consumo y gráfica de uso de recursos
Archivo `parte3.py`: El script ejecuta un proceso especificado y periódicamente lee y registra el consumo de CPU y de memoria en un archivo, almacenando la información con timestamps.

Se utiliza la biblioteca `matplotlib` para graficar los resultados.

En este punto es importante reconocer que para una aplicación y utilidad más reales de este script, incluso para la misma prueba a nivel didáctico de este laboratorio, hubiese sido más interesante hacer mayores pruebas con otro tipo de procesos que tuviesen un comportamiento más dinámico e idealmente de relevancia real. También es cierto que la configuración de la gráfica, en conjunto con la elección adecuada del proceso a monitorear, permitirían un mayor aprovechamiento del ejercicio de scripting. No obstante, se presentan los resultados de probar el script con un proceso cualquiera, como se muestra a continuación.

![resultados3](https://raw.githubusercontent.com/mareyes1/Lab2/main/parte3_lab7.png)

Se muestra como se logra graficar con `matplotlib` la información del proceso, aunque como se mencionó anteriormente, el ejemplo utilizado no es el más apropiado.

Los resultados mostrados surgen de ejecutar el siguiente comando, donde el segundo argumento corresponde al tiempo de espera:

`>>> python3 ./parte3.py calc.exe 5`

Nota: Como se ha podido ver, en gran parte se ha hecho uso de la plataforma Windows, la cual aunque es más incómoda para trabajar en comparación la terminal de Linux, era la única que estaba disponible debido al agotamiento de la memoria de almacenamiento de la máquina virtual de Linux que se venía utilizando. Sin embargo en el caso de los primeros scripts sí fue posible verificar su funcionamiento y portabilidad en ambas plataformas.
