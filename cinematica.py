#biblioteca com tres funcoes

#funcao menu
def mostrar_menu():
    print('_____________________')
    print('1 - Calcular Energia Potencial.')
    print('2 - Calcular Energia Cinetica.')
    print('4 - Sair do Programa.')
    print('_____________________')

#funcao calcular energia potencial
def calcular_ep(m, h):
    ep = m*9,8*h
    return ep

#funcao calcular energia cinetica
def calcular_ec(m, v):
    ec = (m*(v**2))/2 #massa * velocidade ao quadrado / por 2
    return ec

