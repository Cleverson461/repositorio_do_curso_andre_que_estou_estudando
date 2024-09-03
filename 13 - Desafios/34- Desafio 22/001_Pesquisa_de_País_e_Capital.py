# Desafio 21

""" 
    Para este desafio, crie uma lista com 5 nomes de paises e as capitais desses paises. Peca ao usuario para digitar o nome de um pais. Se o pais estiver na lista, imprima "A capital de [pais] e [capital]". Se o pais nao estiver na lista, imprima "Desculpe, nao temos informacoes sobre a capital desse pais".
    
"""
paises_capitais = {
    'Brasil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
    
}

pais = input('Digite o nome de um pais: ')

if pais in paises_capitais:
    resultado = f'A capital de {pais} e {paises_capitais[pais]}'
else:
    resultado = 'Desculpe, nao temos informacoes sobre a capital desse pais'

print(resultado)