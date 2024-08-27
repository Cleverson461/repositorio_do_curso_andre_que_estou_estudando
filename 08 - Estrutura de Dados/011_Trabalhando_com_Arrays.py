
# Array (Matriz)
    # Similar as listas
    # Melhor perfome
    # Contém outros arrays como elementos
    # Arrays podem ser concatenados com o operador +
    # Arrays podem ser repetidos com o operador *
    # Arrays podem ser ordenados com a função sorted()
    # Arrays podem ser invertidos com a função reverse()
    # Arrays podem ser buscados com a função index()
    # Arrays podem ser filtrados com a função filter()
    # Arrays podem ser transformados em strings com a função str()
    # Arrays podem ser transformados em tuplas com a função tuple()
    # Arrays podem ser transformados em dicionários com a função dict()
    # Arrays podem ser transformados em conjuntos com a função set()
    # Arrays podem ser transformados em bytes com a função bytes()
    
""" https://docs.python.org/pt-br/3/library/array.html """

from array import array

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numeros_i)
print(numeros_f)