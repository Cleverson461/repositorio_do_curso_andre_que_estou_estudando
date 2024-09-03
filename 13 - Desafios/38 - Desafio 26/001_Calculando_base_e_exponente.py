# Desafio 26

""" 
    Para este desafio, crie uma função que calcule a pontência de um número. A funçao deve aceitar dois argumentos: a base e o expoente. No entendo, se o expoente não for fornecido ao chamar a funcao, ele deve assumir o valor padrao de 2. 
"""

def potencia(base, expoente=2):
    return base ** expoente

num1 = int(input('Digite o numero base: '))
num2 = input('Digite o numero expoente (default 2): ')

if num2:
    print(f'O valor de {num1} elevado á {num2} é: {potencia(num1, int(num2))}')
else:
    print(f'O valor de {num1} elevado á {num2} é: {potencia(num1)}')
    
    
