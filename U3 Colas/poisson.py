# Trabajo Final de la Unidad de Colas:
# Implementar un software que permita obtener las siguientes medidas de rendimiento
# 	- Cantidad promedio en el sistema
# 	- Cantidad promedio en cola
# 	- Tiempo promedio en el sistema
# 	- Tiempo promedio en cola
# 	- Factor de utilizacion del/los servidores
# Para los siguientes modelos:
# 	- M/M/1
# 	- M/G/1
# 	- M/D/1
# 	- M/M/s
# 	- M/G/s
# 	- M/D/s
# 	- H/M/s
INF = 999999999

def load_data():
    lamda = int(input('Ingresar Tasa de Llegada Lamda: '))
    mu = int(input('Ingresar Tasa de Servicio Mu: '))
    q_server = int(input('Ingresar Cantidad de Servidores c: '))
    try:
        q_system_lim = int(input('Ingresar Límite Sistema: '))
    except:
        q_system_lim = INF
    try:
        q_source_lim = int(input('Ingresar Límite Fuente: '))
    except:
        q_source_lim = INF
    return lamda, mu, q_server, q_system_lim, q_source_lim
def main():
    lamda, mu, q_server, q_system_lim, q_source_lim = load_data()

    
def MM1(lamda, mu, q_server, q_system_lim, q_source_lim):
    roh = lamda / mu 
    Ls = roh / (1 - roh)
    Lq = (roh * roh) / (1 - roh)
    Ws = 1 / (mu - lamda)
    Wq = roh / (mu (1 - roh))
    c = roh
def MMs(lamda, mu, q_server, q_system_lim, q_source_lim):
    roh = lamda / mu 
    Ls = lamda / (mu - lamda)
    Lq = (lamda * lamda) / (mu * (mu - lamda))
    Wq = Lq / lamda  # ????
    Ws = Wq + (1 / mu) # ????


