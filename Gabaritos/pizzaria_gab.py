#Questão 3
#Simulado Inflames
#Gabarito

import math
def classifica_pizza(lista_de_pizzas):
    aux = []
    qualidades = ['baixa qualidade', 'media qualidade', 'alta qualidade']
    for pizza in lista_de_pizzas:
        quantidade_de_massa = pizza[0]
        quantidade_de_recheio = pizza[1]
        raio = pizza[2]
        total = quantidade_de_massa + quantidade_de_recheio
        area_da_pizza = math.pi * raio * raio
        densidade_superficial_de_recheio = quantidade_de_recheio / area_da_pizza
        densidade_superficial_massa_total = total / area_da_pizza
        indice = 0
        if densidade_superficial_de_recheio > 0.07 and densidade_superficial_de_recheio < 0.09:
            indice += 1
        if densidade_superficial_massa_total > 0.18 and densidade_superficial_massa_total < 0.25:
            indice += 1
        aux.append(qualidades[indice])
        indice = 0
    return aux


pizzas_0 = [[600, 300, 35], [650, 250, 35], [1000, 100, 35]]
pizzas_1 = [[100, 50, 15], [300, 150, 25], [650, 250, 15], [750, 50, 35]]

#Testes
print(classifica_pizza(pizzas_0)) #Saída: ['alta qualidade', 'media qualidade', 'baixa qualidade']
print(classifica_pizza(pizzas_1)) #Saída: ['alta qualidade', 'alta qualidade', 'baixa qualidade', 'media qualidade']

