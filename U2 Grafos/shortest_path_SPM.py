import numpy as np
# BASADO EN LA EXPLICACIÓN: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
def load_graph(q_node):
    graph = []
    for i in range(q_node):
        row = []
        for j in range(q_node):
            distance = int(input('Ingresar Distancia: '))
            row.append(distance)
        graph.append(row)
    return graph

def minimum_distance(distance, nodes_includes, q_node):
    #minimum value to compare
    aux_minimun_value = 1e7
    for i in range(q_node):
        # if the distance is minimal that aux and the node is not included
        if distance[i] < aux_minimun_value and nodes_includes[i] == False:
            aux_minimun_value = distance[i]
            node_index = i

    return node_index

def SPMDijkstra(graph, q_node, source_node):
    #We set an default larger number to compare the distance
    distance = np.full(q_node,1e7)
    #We set an array that contain nodes includes in result
    nodes_includes = np.full(q_node, False)
    #Now we asign 0 to the distance of source Node.
    distance[source_node] = 0

    for i in range(q_node):
        #Select the minimun distance
        node_index = minimum_distance(distance, nodes_includes, q_node)
        #Now we can include the node
        nodes_includes[node_index] = True
        #update values of adjacents vertices of the node picked
        #only if: distance is greater than new distance
        #and the node is not in the node_includes array
        for index in range(q_node):
            if (graph[node_index][index] > 0 and
                nodes_includes[index] == False and
                distance[index] > distance[node_index] + graph[node_index][index]):
                distance[index] = distance[node_index] + graph[node_index][index]
    return distance

def main():
    q_node = int(input('Ingresar Cantidad de Nodos: '))
    graph = load_graph(q_node)
    print('\nMatriz de Distancias:')
    print(graph)
    print('\n')
    source_node = int(input('Ingresar Nodo de Origen: '))
    print('\nResultado:')
    distance = SPMDijkstra(graph, q_node, source_node)
    print("Nodo \t Distancia desde el Nodo")
    for node in range(q_node):
        print(node, "\t", distance[node])

main()

#EXAMPLE
 # 1 2   3  4  5
#1 0 100 30 0  0
#2 0 0   20 0  0
#3 0 0   0  10 60
#4 0 15  0  0  50
#5 0 0   0  0  0
