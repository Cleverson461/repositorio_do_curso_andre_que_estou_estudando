# Desafio 24

""" 
    Crie uma função que aceita um número como entrada e retorna o quadrado desse número.
"""

def quadrado(numero):
    return numero ** 2

num = int(input('Digite um numero: '))

# Teste
print(f'O quadrado de {num} é {quadrado(num)}' )  # Saída: 25
#print(f'O quadrado de {num} é {quadrado(num)}')  # Saída: 100
#print(f'O quadrado de {num} é {quadrado(num)}')  # Saída: 9