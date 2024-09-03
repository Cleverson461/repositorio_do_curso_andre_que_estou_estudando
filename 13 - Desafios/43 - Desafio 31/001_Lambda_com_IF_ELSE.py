# Desafio 31

""" 
    Para este desafio, crie uma funcao lambda que aceite um numero e retorne "Par" se o numero for par e "impar" se o numero for impar. 
"""

par_impar = lambda x: 'Par' if x % 2 == 0 else 'Impar'

user_number = int(input('Digite um numero: '))
print(f'O número {user_number} é {par_impar(user_number)}')