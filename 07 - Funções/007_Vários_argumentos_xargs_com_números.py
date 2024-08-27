# Functions (Funções)
 # DRY - Don't repeat yourself.
 # Vários Argumentos (xargs)
 
# Criar um função que soma vários números.

def soma(*numeros):
    resultado = 0
    for number in numeros:
        resultado += number
    return resultado

# Testar a função
print(soma(2, 3, 4, 7, 4)) # Deve imprimir: 20
x = soma(2, 3, 4, 7)
print(x)