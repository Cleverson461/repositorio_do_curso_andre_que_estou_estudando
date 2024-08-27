
# Erros 
    # Excelente para testes 
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try: 
    valor = int(input('Digite o valor do seu produto: '))
    # print(type(valor))
    print(valor)
except ValueError:
    print('Você digitou um valor inválido. Favor digitar um valor em numeros')

print('Este código nunca será executado') # Não realiza o 'stop' no programa