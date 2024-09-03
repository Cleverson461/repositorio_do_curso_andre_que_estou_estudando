""" Calculo de IMC - Indice de Massa Corporal """
altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print('Você está MAGREZA.')
    print(f'Seu IMC é: {IMC:.2f}')
elif IMC >= 18.5 and IMC < 24.9:
    print('Você está no peso ideal.')
    print(f'Seu IMC é: {IMC:.2f}')
elif IMC >= 25.0 and IMC < 29.9:
    print('Você está SOBREPESO.')
    print(f'Seu IMC é: {IMC:.2f}')
elif IMC >= 30 and IMC < 39.9:
    print('Você está com OBESIDADE.')
    print(f'Seu IMC é: {IMC:.2f}')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
    print(f'Seu IMC é: {IMC:.2f}')
    print('Seu diagnóstico é: Obesidade mórbida severa.')