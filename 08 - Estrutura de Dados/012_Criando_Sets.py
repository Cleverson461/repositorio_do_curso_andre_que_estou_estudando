
# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index
    # Utiliza chaves {}
    # Não permite valores duplicados
    # São mutáveis
    # São indexados
    # Podem ser utilizados para armazenar dados relacionados
    # Podem ser utilizados para verificar a existência de valores
    # Podem ser utilizados para realizar operações de união, interseção, diferença e diferença simétrica
    # Podem ser utilizados para filtrar dados

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference
print(num1 & num2) # And

print()

print(len(num1))
print(len(num2))

print()


