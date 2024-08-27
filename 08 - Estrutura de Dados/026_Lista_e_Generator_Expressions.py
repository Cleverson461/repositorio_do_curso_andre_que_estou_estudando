
# Generator Expressions
    # Uma forma mais rápida para Listas, dicionários e etc. 
    # Menos memória alocada
    # Valores em bytes
    # Utiliza parênteses () ao invés de colchetes []
    # São mais eficientes para loops
    # Generator expressions não podem ser alterados após sua criação
    # Generator expressions não podem ser iterados duas vezes
    # Generator expressions podem ser usadas em expressões lambda
    # Generator expressions podem ser usadas em funções map(), filter(), reduce()
    # Generator expressions não podem ser usadas em funções zip()
    
# Exemplos de Generator Expressions
from sys import getsizeof

numeros = [x * 10 for x in range(1000000)]
print(type(numeros))
#print(numeros)
print(getsizeof(numeros))

print('======================')

numeros2 = (x * 10 for x in range(1000000))
print(type(numeros2))
#print(list(numeros2))
print(getsizeof(numeros2))