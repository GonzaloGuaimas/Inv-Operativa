import numpy as np
INF = 99999 #largest num aux to compare

def load_distance_matrix(q_nodes):
    #complete the matrix with INF value
    distance_matrix = np.full((q_nodes, q_nodes),INF)  
    for i in range (q_nodes):
        for j in range (q_nodes):
            try:
                #Enter is equal to INF
                distance_matrix[i][j] = int(input('Ingresar Distancia, posición: ('+str(i)+","+str(j)+")"))
            except:
                j+=1
    return distance_matrix

def SPMFloyd(distance_matrix, q_nodes): 
    distance_matrix = list(map(lambda i: list(map(lambda j: j, i)), distance_matrix))
    for k in range(q_nodes):    # node 1
        for i in range(q_nodes):    # node 2
            for j in range(q_nodes):    # node 3
                # floyd equation
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    return distance_matrix
 
def main():
    graph = [[0, 3, 10, INF,INF],
            [3, 0, INF, 5, INF],
            [10, INF, 0, 6, 15],
            [INF, 5, 6, 0, 4],
            [INF, INF, INF, 4, 0]]
    q_nodes = int(input('Ingresar Cantidad de Nodos: '))
    matrix = load_distance_matrix(q_nodes)
    print('\nMatriz de distancia: ')
    print(matrix)
    distance_matrix = SPMFloyd(matrix, q_nodes)
    print("\nMatriz de las distancias más cortas para cada par de Nodos")
    for i in range(q_nodes):
        for j in range(q_nodes):
            if(distance_matrix[i][j] == INF):
                print("%7s" % ("INF"), end=' ')
            else:
                print("%7d\t" % (distance_matrix[i][j]), end=' ')
            if j == q_nodes-1:
                print()
main()