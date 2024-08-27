""" https://docs.python.org/3/library/functions.html#filter """

# Filter Function
    # Muito utilizado com listas
    # Aplicar um função a um Iterable, filtrando os items. (list, tuple, dic etc.)
    # Recebe uma função e uma lista como argumentos
    # Retorna uma nova lista com todos os elementos que satisfazem a função
    
valores = [10, 12, 34, 44, 57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

# Usando lambda function para filtrar valores maiores que 20
print(list(filter(lambda x: x > 20, valores)))