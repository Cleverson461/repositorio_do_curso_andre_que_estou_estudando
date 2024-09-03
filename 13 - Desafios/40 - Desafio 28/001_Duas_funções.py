# Desafio 28

""" 
    Para este desafio, crie duas funcoes. A primeira funcao deve aceitar um numero e retornar o dobro desse numero. A segunda funcao deve aceitar um numero e retornar o quadrado desse numero. Em seguida, chame a primeria funcao dentro da segunda para retornar o quadrado do dobro de um numero.
"""

def dobrar(numero):
    return numero * 2

def quadrado(numero):
    return dobrar(numero) ** 2

user_numero = int(input('Digite um numero: '))

print(f'O quadrado do dobro numero {user_numero} é {quadrado(user_numero)}')