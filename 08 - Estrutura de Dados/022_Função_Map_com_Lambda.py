""" https://docs.python.org/3/library/functions.html """

# Map Function
    # Muito utilizado com listas
    # Aplicar um função a um Iterable, por item. (list, tuple, dic etc.)
    # Aplica uma função a cada elemento de uma lista

numeros = [6, 7, 8, 9, 10]

print(list(map(lambda x: x * 2, numeros)))