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
    
set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'f'}
set3 = {'c', 'd', 'f'}

#set4 = set1.union(set2)
#set4 = set1.difference(set3)
# set4 = set1.intersection(set2)
set4 = set1.symmetric_difference(set2)

print(set4)