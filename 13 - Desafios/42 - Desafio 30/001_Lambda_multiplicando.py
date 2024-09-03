# Desafio 30

""" 
    Para este desafio, crie uma funcao lambda que aceite dois numeros e retorne a multiplicacao desses numeros. 
"""

multiplicar = lambda num1, num2: num1 * num2

# Teste
num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print(f'A multiplicaçao entre {num} e {num2} {multiplicar(num, num2)}')
