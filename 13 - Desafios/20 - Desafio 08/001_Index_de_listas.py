# Desafio 08
""" 
    Para este desafio, comece com a lista "frutas" do desafio anterior.
    Primeiro, seu desafio é alterar o segundo elemento da lista (índice 1) de 'banana'para 'morango'.
    Depois disso, adicione a fruta 'abacaxi'ao final da lista. Por fim, imprima a lista modificada na tela.
"""

frutas = ['abacate', 'maça', 'banana', 'manga', 'uva']

# frutas[0:5] = ['morango', 'abacaxi']
# frutas[2] =  "morango"
# frutas.append('abacaxi')
frutas.insert(2, 'abacaxi')
print(frutas)
