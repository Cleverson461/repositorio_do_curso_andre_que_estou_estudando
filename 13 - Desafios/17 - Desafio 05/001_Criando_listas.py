# Desafio 05

""" 
    Neste desafio, quero que você crie um script que solicite ao usuário dois números. Em seguida, seu script deve imprimir a soma, a subtração, a multiplicação, a divisão(resultado decimal) e a exponenciação(primeiro número elevado ao segundo número) desses dois números.
"""

# Lose when user enters two numbers
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

# Perform mathematical calculations
sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
exponentiation = num1 ** num2

# Printing the results to the console
print(f'Soma: {sum}')
print(f'Subtracao: {subtraction}')
print(f'Multiplicacao: {multiplication}')
print(f'Divisao: {division:.2f}')
print(f'Exponenciacao: {exponentiation:.2f}')