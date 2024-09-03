# Desafio 27

""" 
    As funcoes recursivas sao funcoes que se chamam dentro do seu proprio bloco de codigo. Elas sao uteis para resolver problemas que podem ser divididos em problemas menores de natureza semelhante. 
    
    Um exemplo classico de onde a recursao é usada e o calculo do fatorial de um numero. O fatorial de um numero n é o produto de todos os numeros inteiros positivos de n ate 1.
"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
# Testando a função
user_number = int(input('Digite um número: '))

print(f'O fatorial de {user_number} é {fatorial(user_number)}')