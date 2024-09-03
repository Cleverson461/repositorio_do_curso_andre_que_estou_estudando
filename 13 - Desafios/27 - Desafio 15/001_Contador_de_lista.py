# Desafio 15

""" 
    Para este desafio, crie uma lista de frutas que inclui "maça" tres vezes e outras frutas de sua escolha. Use um loop for para contar quantas vezes 'maça' aparece na lista e imprima o resultado. 
"""

frutas = ['laranja', 'maça', 'acerola', 'maça', 'banana', 'maça', 'manga']

contador = 0
for fruta in frutas:
    if fruta == 'maça':
        contador += 1
        
print(f'Numeros de maças na lista: {contador} - {fruta}.')