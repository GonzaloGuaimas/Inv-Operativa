import nashpy as nash
import numpy as np

def cargarPagos(c_estrategiasJ1, c_estrategiasJ2, jugador):
  matriz_pago = np.zeros((c_estrategiasJ1, c_estrategiasJ2))
  for i in range (c_estrategiasJ1):
    for j in range (c_estrategiasJ2):
        matriz_pago[i][j] = int(input('Ingresar Pago '+jugador+' posicion: ('+str(i)+","+str(j)+")"))
  return matriz_pago

def mostrarResultado(arreglo, jugador, tipo):
    for index in range(len(arreglo)):
        print(arreglo[index])
        if (arreglo[index] == 1): print(jugador+' ELIJE '+tipo+' '+str(index+1))
        break
def main():
    c_estrategiasJ1 = int(input('Ingresar Cantidad de Estrategias J1:  '))
    c_estrategiasJ2 = int(input('Ingresar Cantidad de Estrategias J2:  '))
    matriz_pagosJ1 = cargarPagos(c_estrategiasJ1, c_estrategiasJ2, 'J1')
    matriz_pagosJ2 = cargarPagos(c_estrategiasJ1, c_estrategiasJ2, 'J2')
    print('\n')
    print('MATRIZ PAGOS J1')
    print(matriz_pagosJ1)
    print('\n')
    print('MATRIZ PAGOS J2')
    print(matriz_pagosJ2)

    print('\n')
    print('RESOLUCIÓN')

    resultado_dominadas = nash.Game(matriz_pagosJ1,matriz_pagosJ2).support_enumeration()
    for resultado in resultado_dominadas:
        print('J1 ELIGE FILA') # se marca con 1 la fila seleccionada
        print(resultado[0])
        print('J2 ELIGE COLUMNA') # se marca con 1 la columna seleccionada
        print(resultado[1])
        print(resultado)
main()