"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    soma = 0
  for n in lista:
    soma = soma + n
  return soma


def conta_pares(lista):
   def conta_pares(lista):
  contador = 0
  for n in lista:
    if n%2 == 0:
      contador = contador + 1
  return contador

def maior_valor(lista):
   def maior_valor(lista):
  maior = lista[0]
  for n in lista[i]:
    if n > maior:
      maior = n
  return maior
    

def existe(lista, alvo):
    for item in lista:
        if item == alvo:
            return true
        else:
          return false


def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    pass


def segundo_maior(lista):
    """(Desafio) Devolve o segundo maior, percorrendo a lista uma unica vez."""
    pass
