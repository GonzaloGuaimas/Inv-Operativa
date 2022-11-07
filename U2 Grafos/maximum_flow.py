from collections import defaultdict
import numpy as np

def load_capacity_matrix(q_nodes):
    #complete the matrix with 0 values
    capacity_matrix = np.zeros((q_nodes, q_nodes))  
    for i in range (q_nodes):
        for j in range (q_nodes):
            try:
                #Enter is equal to 0
                capacity_matrix[i][j] = int(input('Ingresar Capacidad, posición: ('+str(i)+","+str(j)+")"))
            except:
                j+=1
    return capacity_matrix

#this func check if there a path from source to destiny and select the minimun path
def there_is_a_path(source, destiny, path, q_node, graph):
        visited = np.full((q_node),False)
        queue = []
        queue.append(source)
        visited[source] = True
        while queue:
            index = queue.pop(0)
            for i, val in enumerate(graph[index]):
                if visited[i] == False and val > 0:
                    queue.append(i)
                    visited[i] = True
                    path[i] = index
                    if i == destiny:
                        return True
        return False

def maximum_flow(q_nodes, graph, source, destiny):
    path = np.full((q_nodes),-1)
    max_flow = 0
    while there_is_a_path(source, destiny, path, q_nodes, graph) :
        path_flow = float("Inf")
        s = destiny
        while(s != source):
            path_flow = min (path_flow, graph[path[s]][s])
            s = path[s]
        max_flow += path_flow
        v = destiny
        while(v != source):
            u = path[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = path[v]
    return max_flow

def main():
    q_node = int(input('Ingresar cantidad de Nodos'))
    source = int(input('Ingresar nodo fuente'))
    destiny = int(input('Ingresar nodo Destino/Sumidero'))
    graph = load_capacity_matrix(q_node)
    print ("El flujo máximo es" + maximum_flow(q_node, graph, source, destiny))

main()