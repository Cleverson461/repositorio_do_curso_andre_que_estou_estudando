# Desafio 32

""" 
    Para este desafio, crie um funcao lambda que eleve um numero ao quadrado. Em seguida, use essa funcao para calcular o quadrado de todos os numeros em uma lista usando um loop for.
"""

numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda num: num ** 2

quadrados = []

for numero in numeros:
    quadrados.append(quadrado(numero))

print(f'Os quadrados dos numeros {numeros} são {quadrados}')