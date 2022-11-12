import numpy as np

def factorial(num): 
    if num < 0: 
        print('Número negativo')
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


def load_data():
    lamda = int(input('Ingresar Tasa de Llegada Lamda: '))
    mu = int(input('Ingresar Tasa de Servicio Mu: '))
    q_server = int(input('Ingresar Cantidad de Servidores c: '))
    return lamda, mu, q_server

def MMS(lamda, mu, q_server):
    P = []
    C = []

    rho = lamda/mu
    P0 = 1-rho
    Lq = (P0*((lamda/mu)**q_server)*rho/(factorial(q_server)*((P0)**2)))  
    Wq = Lq / lamda
    W = Wq + (1/mu)
    L = Lq + (lamda/mu)

    P.append(P0)
    pacum = []
    for i in range(1, 40):
        Pn = P[-1]
        if(i<=0 and i<=q_server):
            Pi = (((lamda/mu)**i)/factorial(i))*Pn
        else:
            Pi = (((lamda/mu)**i)/(factorial(q_server)*(q_server**(i-q_server))))*Pn
        P.append(Pi)
        pacum.append(sum(P))

    print(f'lambda: {lamda}')
    print(f'Mu: {mu}')
    print(f'c: {q_server}')
    print(f'Wq: {Wq}')
    print(f'Lq: {Lq}')
    print(f'L: {L}')
    print(f'W: {W}')
    print('Pn | Ac Pn | Prob Pn | Ac Pn')
    print(np.array(P))

def main():
    lamda, mu, q_server = load_data()
    MMS(lamda, mu, q_server)

main()