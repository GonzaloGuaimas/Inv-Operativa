from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable
import numpy as np

# FUENTE PARA EL USO DE LA LIBRERÍA PULP
# https://realpython.com/linear-programming-python/
# https://pypi.org/project/PuLP/

def cargarPagos(c_estrategiasJ1, c_estrategiasJ2):
  matriz_pago = np.zeros((5, 5)) #| Lo único malo de esta librería es que tengo que limitar el número de estrategias
  for i in range (c_estrategiasJ1):
    for j in range (c_estrategiasJ2):
        matriz_pago[i][j] = int(input('Ingresar Pago posicion: ('+str(i)+","+str(j)+")"))
  return matriz_pago

def resolverPL(matriz_pagos, nombre_variable, tipo_solución, c_estrategiasJ1, c_estrategiasJ2, jugador):
    #inicializo el modelo
    model = LpProblem(name="small-problem", sense=tipo_solución)
    #variables de decisión | Estrategias Lo único malo de esta librería es que tengo que limitar el número de estrategias
    x1 = LpVariable(name=nombre_variable+"1", lowBound=0)
    x2 = LpVariable(name=nombre_variable+"2", lowBound=0)
    x3 = LpVariable(name=nombre_variable+"3", lowBound=0)
    x4 = LpVariable(name=nombre_variable+"4", lowBound=0)
    x5 = LpVariable(name=nombre_variable+"5", lowBound=0)
    v = LpVariable(name="v", lowBound=0)

    obj_func = v
    #funcion objetivo
    if(jugador == 'J2'): obj_func = -v
    model += obj_func

    #restricciones | cargadas según el recorrido para J1 (col) y J2 (rows)
    numero_res = 1
    if(jugador == 'J1'):
        for j in range(c_estrategiasJ2):
            model += (obj_func - (matriz_pagos[0][j]*x1) - (matriz_pagos[1][j]*x2) - (matriz_pagos[2][j]*x3) - (matriz_pagos[3][j]*x4) - (matriz_pagos[4][j]*x5) <=0  , "res "+str(numero_res))
            numero_res +=1
    else:
         for i in range(c_estrategiasJ1):
            model += (obj_func - (matriz_pagos[i][0]*x1) - (matriz_pagos[i][1]*x2) - (matriz_pagos[i][2]*x3) - (matriz_pagos[i][3]*x4) - (matriz_pagos[i][4]*x5) >=0  , "res "+str(numero_res))
            numero_res +=1
    # usando esta librería tenemos que resolver nuestro pequeño problema de la siguiente forma
    # para que nos de el resultado correctamente : 
    if(jugador == 'J1'):
        if(c_estrategiasJ1 == 1):
            model += ( x1 == 1 , "res 11")
        elif(c_estrategiasJ1 == 2):
            model += ( x1 + x2  == 1 , "res 11")
        elif(c_estrategiasJ1 == 3):
            model += ( x1 + x2 + x3  == 1 , "res 11")
        elif(c_estrategiasJ1 == 4):
            model += ( x1 + x2 + x3 + x4  == 1 , "res 11")
        elif(c_estrategiasJ1 == 5):
            model += ( x1 + x2 + x3 + x4 + x5 == 1 , "res 11")
    else:
        if(c_estrategiasJ2 == 1):
            model += ( x1  == 1 , "res 11")
        elif(c_estrategiasJ2 == 2):
            model += ( x1 + x2  == 1 , "res 11")
        elif(c_estrategiasJ2 == 3):
            model += ( x1 + x2 + x3  == 1 , "res 11")
        elif(c_estrategiasJ2 == 4):
            model += ( x1 + x2 + x3 + x4 == 1 , "res 11")
        elif(c_estrategiasJ2 == 5):
            model += ( x1 + x2 + x3 + x4 + x5 == 1 , "res 11")
            
    model += ( x1 >= 0 , "res 12")
    model += ( x2 >= 0 , "res 13")
    model += ( x3 >= 0 , "res 14")
    model += ( x4 >= 0 , "res 15")
    model += ( x5 >= 0 , "res 16")

    # Solve the problem
    status = model.solve()

    print(f"Objetivo | v: {model.objective.value()}")
    for var in model.variables():
        print(f"{var.name}: {var.value()}")

def main():
    c_estrategiasJ1 = int(input('Ingresar Cantidad de Estrategias J1:  '))
    c_estrategiasJ2 = int(input('Ingresar Cantidad de Estrategias J2:  '))
    matriz_pagos = cargarPagos(c_estrategiasJ1, c_estrategiasJ2)
    print('\n')
    print(matriz_pagos)
    print('#--------------------------------------------------------------#\n')
    resolverPL(matriz_pagos, "x", LpMaximize, c_estrategiasJ1, c_estrategiasJ2, 'J1')
    print('#--------------------------------------------------------------#\n')
    resolverPL(matriz_pagos, "y", LpMinimize, c_estrategiasJ1, c_estrategiasJ2, 'J2')

main()



