
# Erros 
    # Excelente para testes 
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

""" try: 
    valor = int(input('Digite o valor do seu produto: '))
    # print(type(valor))
    print(valor)
except ValueError:
    print('Você digitou um valor inválido.')
else:
    print('Operação realizada com sucesso')
    resultado = valor * 0.5
    print(f'O resultado da porcentagem do {valor} é: {resultado}')

print('Este código nunca será executado') # Não realiza o 'stop' no programa """

try: 
    valor = int(input('Digite o valor do seu produto: '))
    # print(type(valor))
    print(valor)
except ValueError:
    print('Você digitou um valor inválido.')
finally:
    print('Este código sempre será executado') # Realiza o 'stop' no programa
