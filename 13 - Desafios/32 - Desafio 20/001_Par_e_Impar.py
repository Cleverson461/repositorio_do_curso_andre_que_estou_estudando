# Desafio 20

""" 
    Para este desafio, crie uma lista de numeros de 1 a 10. Use um "for loop" para iterar sobre a lista. Se o numero atual da iteracao for par, imprima "O numero[numero] é par". Se o numero for impar, imprima "O número[numero] é impar.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 34, 45, 56, 21]
numeros = list(range(1, 11))

for interecao in numeros:
    if interecao % 2 == 0:
        print(f'O número {interecao} é par')
    else:
        print(f'O número {interecao} é impar')