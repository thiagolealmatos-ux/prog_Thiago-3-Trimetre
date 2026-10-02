"""Aula 03 - Construa e diga o custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

ATENCAO: quase todas as funcoes desta aula devolvem DUAS coisas,
o resultado e a contagem de operacoes:

    return soma, operacoes

Quem devolve so o resultado nao passa nos testes.
"""


def soma_contando(lista):

  soma = 0
  operacoes = 0

  for numero in lista:
    soma += numero
    operacoes += 1

  return soma, operacoes


def busca_linear_contando(lista, alvo):
    
    comparacoes = 0
    
    for i in range(len(lista)):
        comparacoes += 1
        
        if lista[i] == alvo:
            return i, comparacoes
    
    return -1, comparacoes        


def busca_binaria_contando(lista, alvo):
    
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    
    while inicio <= fim:
        meio = (inicio + fim) //2
        comparacoes += 1
        
        if lista[meio] == alvo:
            return meio, comparacoes
            
        elif lista[meio] < alvo:
            inicio = meio + 1
        
        else:
            fim = meio - 1
     
    return -1, comparacoes   
    


def tem_repetido_contando(lista):
    
    comparacoes = 0
    
    for i in range (len(lista)):
        for j in range (+ 1, len(lista)):
            comparacoes += 1
            
            if lista[i] == lista[j]:
                return True, comparacoes
                
    return False, comparacoes


def quantas_divisoes(n):
    """Quantas vezes da para dividir n por 2 ate sobrar 1.
    Use divisao inteira. Devolve so o numero, sem contagem.
    quantas_divisoes(8) -> 3"""
    pass


def mais_frequente_contando(lista):
    """(Desafio) Devolve (valor, comparacoes).
    O valor que mais aparece na lista. Em caso de empate, o que aparece
    primeiro. Conte 1 comparacao cada vez que comparar dois elementos."""
    pass
