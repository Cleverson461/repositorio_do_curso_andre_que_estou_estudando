# Desafio 18

""" 
    Para este desafio, imagine que voce tem uma loja de carros. Crie uma lista com os carros que voce tem em estoque:  Peça ao usuario para que ele insira o nome do carro que deseja comprar. Se o carro estiver em estoque, imprima "Este carro está disponível". Se o carro não estiver em estoque, imprima "Desculpe, este carro não está disponível". 
"""
pesquisa_carro = input('Digite o nome ou numero do carro desejado: \nBMW X6 \nBMW i5 \nBMW i8 \n' )

loja_de_carros = ['BMW X6', 'BMW i5', 'BMW i8']

if pesquisa_carro in loja_de_carros:
    print(f'Este carro está disponível')
else:
    print(f'Desculpe, este carro não está disponível')