# Desafio 14
""" 
    Para este desafio, quero que voce crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando o comando "break". Em seguida, crie um segundo loop que imprima os números de 1 a 10, mas pule a impressão do número 5 usando o comando "continue".
"""

print('Loop com o break: ')
for numero in range(1, 11):
    if numero > 5:
        break
    print(f'Número: {numero}')

print('  ')
print('------------------------')
print('  ')

print('Loop com o continue: ')
for num in range(1, 11):
    if num == 5:
        continue
    print(f'Número: {num}')