# Desafio 19

""" 
    Para este desafio, crie um loop que peça ao usuário para digitar o nome de uma fruta. Se a fruta digita não for 'abacate', o loop deve continuar pedindo ao usuario para digitar o nome de uma fruta. Se a fruta for 'abacate', o loop deve terminar e o programa deve imprimir "Parabéns, voce acertou a fruta!". 
"""

digite_fruta = input('Adivinhe qual fruta estou pensando: ')

while True:
    if digite_fruta.lower() == 'abacate':
        print('Parabéns, voce acertou a fruta!')
        break
    else:
        digite_fruta = input('Adivinhe qual fruta estou pensando: ')
  
