""" Desafio com If, Elif, Else """

""" Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. O usuario deverá fornecer a temperatura. 

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o mal)
160°F ou 71°C - Well done (Bem passada)

"""

temperatura_da_carne = int(input('Qual é a temperatura da carne? '))
conversao = (temperatura_da_carne * 9/5) + 32

if conversao >= 160:
    print(f'A temperatura da carne está {conversao}°F então o ponto está: Well done (Bem passada)')
elif  conversao >= 150:
    print(f'A temperatura da carne está {conversao}°F então o ponto está: Medium well (Ao ponto para o mal)')
elif conversao >= 140:
    print(f'A temperatura da carne está {conversao}°F então o ponto está: Medium (Ao ponto)')
elif conversao >= 130:
    print(f'A temperatura da carne está {conversao}°F então o ponto está: Medium rare (Ao ponto para o mal)')
elif conversao < 120 and conversao >= 114:
    print(f'A temperatura da carne está {conversao}°F então o ponto está: Rare (Selada)')
else:
    print('Cozinhar por mais alguns minutos')