"Es un proyecto de simulacion de la maquina de Galton

#Cree dos funciones..
1 def simulacion_de_canicas , para simular la caida de las canicas
donde ocupe el bucle for , pero lo ocupaba como normalmente lo conocemos como (for i in) pero no hacia lo que queria
entonces estube investigando , leyendo hay otra forma de ocupar for la cual es for _ in en donde el _ se usa cuando no interesa la variable del ciclo , es decir cuando 
queremos repetir algo varias veces 

2 def graficar_histograma, hace la funcion para graficar el histograma 
Aqui ocupamos matplotlib  que es una libreria que permite crear graficas  y visualizaciones de manera sencilla 
entonces se ocupa plt. y lo que se decea hacer 
como por ejemplo plt.title que es para poner el titulo 
plt.xlabel es para definir el eje x 


De principio se me dificulto muchisimo ya que aun no tenia el conocimiento adecuado para poder crear una grafica o mas bien una simulacion de la maquina de galton
pero con el conocimiento adquirido y la practica en definir funciones me ayudo muchisimo y me abrio un poco mas las ideas.

Una funcion para esto y otra funcion para lo otro, en donde se me complico fue en como haré la grafica, entonces se instala la libreria matplotlib para poder 
hacer la visualizacion, y ya con sus alias plt. llamemoslo asi tube que investigar como se utilizaba 

por ejemplo:
plt.bar() → gráficos de barras

plt.hist() → histogramas

plt.scatter() → diagramas de dispersión

plt.pie() → gráficos de pastel

y asi mismo ya tenia una idea

entonces se definio las lineas X y Y, el titulo , la grafica en pantalla 

y el resultado de la simulacion de canicas  en este caso 3000 canicas , con 12 obstaculos , y aqui simula la caida de las canicas
y al final grafica la distribucion final en los contenedores.
