"""Aula 04 - Por que ordenar?

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Hoje voce NAO escreve algoritmo de ordenacao. Use sorted(lista), que
devolve uma lista nova e ordenada sem mexer na original. Evite lista.sort(),
que altera a lista de quem chamou a funcao.
"""


def custo_binaria(n):
    """PRONTA. Nao mexa.
    Pior caso da busca binaria numa lista de n elementos.
    E a quantas_divisoes da aula passada mais 1."""
    divisoes = 0
    while n > 1:
        n = n // 2
        divisoes = divisoes + 1
    return divisoes + 1


def tem_repetido_ordenando(lista):
    
    ordenada = sorted(lista)
    comparacoes = 0

    for i in range(len(ordenada) - 1):
        comparacoes += 1
        if ordenada[i] == ordenada[i + 1]:
            return True, comparacoes

    return False, comparacoes


def mediana(lista):
   
    if len(lista) == 0:
        return None

    ordenada = sorted(lista)
    meio = len(ordenada) // 2

    if len(ordenada) % 2 == 1:
        return ordenada[meio]

    return (ordenada[meio - 1] + ordenada[meio]) / 2


def buscas_para_compensar(n, custo_ordenar):
   
    custo_busca = custo_binaria(n)
    if custo_busca >= n:
        return -1
    k = 1

    while custo_ordenar + k * custo_busca >= k * n:
        k += 1

    return k

def menor_diferenca(lista):
  
    if len(lista) < 2:
        return None

    ordenada = sorted(lista)
    menor = abs(ordenada[1] - ordenada[0])

    for i in range(1, len(ordenada) - 1):
        diferenca = abs(ordenada[i + 1] - ordenada[i])

        if diferenca == 0:
            return 0
        if diferenca < menor:
            menor = diferenca

    return menor