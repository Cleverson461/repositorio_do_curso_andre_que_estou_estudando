# Functions (Funções)
 # DRY - Don't repeat yourself.
 # Vários Argumentos (xargs)
 
# Criar um função que armazena numeros e strings (dados)


def agencia(**carro):
    return carro

print(agencia(modulo='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(modulo='Gol', cor='Azul', motor=1.0))
print(agencia(modulo='Gol', cor='Preto', motor=1.8, placa=1444))
print(agencia(modulo='Gol', cor='Amarelo'))