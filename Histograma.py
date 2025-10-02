#Será la simulación de una máquina de Galton de 3000 canicas. 
#En total tendrá 12 niveles de obstáculos 
#El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, como el siguiente -Se coloca nombre a los ejes y un título al gráfico.
#Deberás emplear dos funciones, una para calcular los resultados de las canicas y la segunda para la graficación del histograma. 

import matplotlib.pyplot as plt  #Aquí se importa la librería matplotlib para graficar
import numpy as np #Aquí se importa la librería numpy para trabajar con arreglos
import random #Aquí se importa la librería random para generar números aleatorios


#Hacemos la funcion para simular la caida de las canicas

def simulacion_de_canicas(numero_canicas, numero_niveles):
    '''
    Simula la caida de canicas en una maquina de Galton
    '''
    contenedores = [0] * (numero_niveles + 1) #Creamos una lista para contar cuantas canicas caen en cada contador  #Se repite la simulacion para cada canica
    for _ in range(numero_canicas): #Se usa cuando no te interesa la variable del ciclo, solo quieres repetir algo N veces.
        posicion = 0   #Empezamos cada canica en la posicion inicial en este caso izquierda 
        for _ in range(numero_niveles):   #Cada canica pasa por numero_niveles de obsatculos , como se ve en el video 
            if random.choice([True, False]):  #Forma aleatoria True= Derecha False = Izquierda 
                posicion += 1 # Si cae a la derecha , s eaumenta la posicion 
   
        contenedores[posicion] += 1 #Cuando la canica termina los niveles , la contamos en su contenedor final 
    return contenedores  #Regresamos a la lista con la cantidad de canicas por contendor 


#Aqui hacemos la funcion  para graficar el histograma

def graficar_histograma(contenedores):
    '''
    Grafica un histograma con los resultados de la simulación de canicas en cada contenedor
    '''
    plt.bar(range(len(contenedores)), contenedores, color = 'blue', width=1.0) #Grafico de barras en color azul 
    plt.xlabel('Posicion final') #Llamamos el eje de x 
    plt.ylabel('Cantidad de canicas') #Llamamos el eje y
    plt.title('Simulacion de la maquina de Galton') #Titulo del grafico 
    plt.grid(True) #Se hace en cuadricula para mayor entendimiento 
    plt.show() #Se muestra la grafica en pantalla

#Ejecutamos la simulacion

resultado = simulacion_de_canicas(3000, 12) #3000 numero de canicas #12 numero de obstaculos de la maquina #Simula la caida de las canicas 
graficar_histograma(resultado) #Grafica la distribucion final en los contenedores
