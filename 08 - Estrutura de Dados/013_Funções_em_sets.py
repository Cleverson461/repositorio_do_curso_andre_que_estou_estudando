
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
    
list1 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6}
#s1.add(7)
s1.update([6, 7, 8, 9, 10])
s1.remove(10)
s1.discard(9)

print(list1)
print(type(list1))
print()
print(s1)
print(type(s1))