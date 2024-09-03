# Desafio 29

""" 
    Para este desafio, crie uma funcao lambda que aceite um numero e retorne o cubo desse numero. 
"""

cubo = lambda num: num ** 3

# Teste
num = int(input('Digite um numero: '))

print(f'O cubo de {num} e {cubo(num)}')
