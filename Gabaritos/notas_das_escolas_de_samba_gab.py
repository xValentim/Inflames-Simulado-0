#Questão 3
#PI 2020.2

#Solução 1
def calcula_escola(lista):
    soma = 0
    for quesito in lista:
        quesito.remove(min(quesito))
        for nota in quesito:
            soma += nota
    return soma

#Solução 2
def calcula_escola(lista):
    soma = 0
    for quesito in lista:
        quesito.remove(min(quesito))
        soma += sum(quesito)
    return soma


#Teste - Academia python