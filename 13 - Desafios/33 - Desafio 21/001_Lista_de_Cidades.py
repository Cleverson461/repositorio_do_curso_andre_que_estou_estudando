# Desafio 21

""" 
    Para este desafio, crie uma lista com os nomes de tres cidades. Peca ao usuario para digitar o nome de uma cidade. Se a cidade estiver na lista, imprima "A cidade esta na lista de cidades". Se a cidade nao estiver na tupla, imprima "A cidade nao esta na lista de cidades" . 
    
"""
# Obs.: Voce nao pode utilizar list[]
cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador', 'Belo Horizonte')

while True:
    cidade_usuario = input('Adivinhe o nome da cidade: ')
    if cidade_usuario.strip() in cidades:
        print('A cidade esta na lista de cidades.')
        break
    else:
        print('A cidade nao esta na lista de cidades.')