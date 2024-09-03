# Desafio com funcoes

""" 
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuario deverá fornecer as seguintes informações: Rendimento, altura e largura. O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'.
"""

rendimento = int(input('Qual o rendimento da lata de tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))


def calcular_tinta():
    area = altura * largura
    latas = area / rendimento

    print(f'Você necessita de {latas} latas de tinta.')

calcular_tinta()