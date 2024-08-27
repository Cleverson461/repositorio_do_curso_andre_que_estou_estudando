""" https://docs.python.org/3/library/functions.html """

# Map Function
    # Muito utilizado com listas
    # Aplicar um função a um Iterable, por item. (list, tuple, dic etc.)
    # Aplica uma função a cada elemento de uma lista

numeros = [1, 2, 3, 4, 5]
def multi(x):
    return x * 2

lista2 = map(multi, numeros)
print(list(lista2))