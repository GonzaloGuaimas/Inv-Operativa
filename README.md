# Investigación Operativa UCASAL - 2022

# Alumnos:
- Cordoba Thiago
- Guaimas Gonzalo

# UNIDAD 1 JUEGOS
## Eliminación dominadas
Para la elaboración de este algoritmo utilizamos la librería de nashpy para poder resolver el juego. 
Esta librería nos devuelve un array que nos señala con un 1 la fila o columna seleccionada por la librería
respectivamente para el J1 y J2
## Estrategias Mixtas
Usamos la librería PULP para la resolución del juego mediante Programación Lineal.
La limitación que tiene esta librería es que no es muy amigable a la hora de variar la cantidad de variables
## Minimax Maximin
Para resolvere este algoritmo utilizamos la librería de numpy para poder obtener el máximo y mínimo de un 
conjunto de datos de un array
#3 Nash
Utilizamos la librería de nashpy y numpy para resolver el algoritmo
# UNIDAD 2 GRAFOS
## Critical Path
Usamos la librería Node para poder calcular la ruta Crítica, esta libreria nos permite asignarle el nombre del proyecto, agregar las tareas y las dependencias de cada una de estas como array, al pasarle estos parámetros nos devuelve el resultado.
## Maximum Flow
Sólo usamos la librería de numpy para manejar los array, para ingresar nuestro grafo utilizamos una matriz de capacidad y mediante la misma realizamos los cálculos correspondientes
## Minimal Spanning Tree  MST
La resolución de este ejercicio se basa en agregar la cantidad de arcos que tenemos e ingresar el peso, el nodo de origen y destino de cada uno. De esta forma armamos nuestro grafo sobre el que trabajamos para encontrar nuestro resultado
## Shortest Path SPM
Usamos numpy para el manejo de arrays, a su vez cargamos la matriz de distancia para resolver el ejercicio
## Shortest Path SPM Floyd
Usamos numpy para el manejo de arrays y también usamos una matriz de distancia para la resolución, marcando como INF los nodos que no tienen conexión entre ellos.
# UNIDAD 3 COLAS
