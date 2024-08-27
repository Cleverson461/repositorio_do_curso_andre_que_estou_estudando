
# Lambda Function
    # É um função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'
    # Pode receber 0 ou mais argumentos
    # Pode ter um ou mais retornos
    # Pode ser atribuída a uma variável
    # Pode ser usada como argumento de outras funções
    # Pode ser usada como valor de retorno de outras funções
    # Funções anônimas
    # Não possuem nome
    # Utilizam a palavra reservada lambda
    # São usadas para expressões simples
    # São chamadas quando são necessárias
    # São úteis quando você precisa de uma função em uma única expressão
    
# Criando uma lambda function simples

def somar(x):
    return x + 10
print(somar(2))


soma = lambda b, c: b + c + 10
print(soma(2, 4))