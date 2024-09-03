# Desafio 23

""" 
    Para este desafio, crie dois conjuntos, cada um contendo 5 nomes de seus amigos. Alguns nomes devem estar presentes em ambos os conjuntos. Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado.
"""

nomes_de_amigos = {'Davi', 'Nicolas', 'Bruno', 'Bryan', 'Alisson'}
nomes_de_amigos2 = {'Marcileia', 'Neide', 'Davi', 'Nicolas', 'Bryan'}

# amigos = nomes_de_amigos.intersection(nomes_de_amigos2)
# amigos = nomes_de_amigos.union(nomes_de_amigos2)
amigos = nomes_de_amigos.difference(nomes_de_amigos2)

print(amigos)