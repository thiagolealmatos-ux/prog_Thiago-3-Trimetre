"""Aula 02 - Listas em Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def remove_negativos(lista):
  
    nova_lista = []
    for numero in lista:
        if numero >= 0:
            nova_lista.append(numero)

    return nova_lista


def inverte(lista):
    
    nova_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nova_lista.append(lista[i])

    return nova_lista


def busca_binaria(lista, alvo):
  
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def intercala(lista_a, lista_b):

    nova_lista = []
    for i in range(len(lista_a)):
        nova_lista.append(lista_a[i])
        nova_lista.append(lista_b[i])

    return nova_lista


def remove_repetidos(lista):

    nova_lista = []
    for numero in lista:
        if numero not in nova_lista:
            nova_lista.append(numero)

    return nova_lista
