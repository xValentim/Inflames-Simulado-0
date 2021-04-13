'''
-Pizzaria
Uma pizzaria está se modernizando e contratou você para desenvolver um mecanismo que 
os ajude na contabilidade das pizzas.

O mecanismo precisa identificar as pizzas como listas de 3 valores: 
quantidade em gramas da massa da pizza (sem contar o recheio), quantidade em gramas de recheio
e raio da pizza em cm, respectivamente

Por exemplo, [600, 300, 35], representa uma pizza de 900 gramas no total,
600 gramas de massa sem contar o recheio, 300 gramas de recheio e 35 cm de raio.

Por critérios econômicos e do chef, as pizzas precisam passar por um padrão de qualidade:

1) A pizza deve ter uma densidade superficial de recheio (massa de recheio por unidade de área)
entre 0.07 g/cm^2 e 0.09 g/cm^2 (não inclui eles).

2) A pizza deve ter uma densidade superficial de massa total (massa total por unidade de área)
entre 0.18 g/cm^2 e 0.25g/cm^2 (não inclui eles).

A pizza pode ser classificada como: 'baixa qualidade', 'media qualidade' e 'alta qualidade'.

Critério de alta qualidade: passar nos padrões 1) e 2).
Critério de média qualidade: passar em um dos padrões.
Critério de baixa qualidade: passar em nenhum dos padrões.

Dessa forma, faça uma função que recebe uma lista preenchida por várias listas que representam pizzas
e retorne uma lista com as strings 'baixa qualidade', se a pizza daquela posição for de baixa qualidade,
'media qualidade', se for de média qualidade e 'alta qualidade', se for de alta qualidade.

Sua função deve se chamar classifica_pizza.

Exemplos,

Entrada: [[600, 300, 35], [650, 250, 35], [1000, 100, 35]]
Saída: ['alta qualidade', 'media qualidade', 'baixa qualidade']

Entrada: [[100, 50, 15], [300, 150, 25], [650, 250, 15], [750, 50, 35]]
Saída: ['alta qualidade', 'alta qualidade', 'baixa qualidade', 'media qualidade']

'''


'''lista = [[600, 300, 35],
         [650, 250, 35],
         [1000, 100, 35]]
i = 0
while i < len(x):
    j = 0
    while j < len(y):
        lista[i][j]





        j += 1
    i += 1'''


def calcula_densidades(pizza):
    qtde_de_massa = pizza[0]
    qtde_de_recheio = pizza[1]
    qtde_total = qtde_de_massa + qtde_de_recheio
    raio = pizza[2]
    area_da_pizza = math.pi * raio * raio
    densidade_superficial_de_recheio = qtde_de_recheio / area_da_pizza
    densidade_superficial_total = qtde_total / area_da_pizza
    return densidade_superficial_de_recheio, densidade_superficial_total

import math
def classifica_pizza(lista_de_pizzas):
    aux = []
    qualidades = ['baixa qualidade', 'media qualidade', 'alta qualidade']
    for pizza in lista_de_pizzas:
        densidade_superficial_de_recheio, densidade_superficial_total = calcula_densidades(pizza)
        indice = 0
        if densidade_superficial_de_recheio > 0.07 and densidade_superficial_de_recheio < 0.09:
            # Passou no padrão 1
            indice += 1
        if densidade_superficial_total > 0.18 and densidade_superficial_total < 0.25:
            # Passou no padrão 2
            indice += 1
        qualidade_da_pizza = qualidades[indice]
        aux.append(qualidade_da_pizza)
    return aux

#Testes 
print(classifica_pizza([[600, 300, 35], [650, 250, 35], [1000, 100, 35]]))
print(classifica_pizza([[100, 50, 15], [300, 150, 25], [650, 250, 15], [750, 50, 35]]))


