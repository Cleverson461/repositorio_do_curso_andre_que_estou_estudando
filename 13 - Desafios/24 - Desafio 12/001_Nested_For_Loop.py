# Desafio 12

""" 
    Para este desafio, crie uma lista de frutas ou vegetais. Use um 'for loop' aninhado (nested for loop) para imprimir todas as combinações possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo.
    
"""

frutas = ["Acerola", "Banana", "Abacaxi"]
vegetais = ["Alface", "Couve", "Brócolis"]

# Imprimindo as combinacoes
for fruta in frutas:
    print("---", fruta)
    for vegetal in vegetais:
        print(f'{fruta} - {vegetal}')