velocidade = 39

if velocidade > 80:
    print("Você ultrapassou a velocidade máxima permitida.")
    print("Multado!")
    multa = (velocidade - 80) * 5
    print(f"Você deverá pagar uma multa de R${multa} .")
elif velocidade < 40:
    print("Favor dirigir acima de 80km/h.")
else:
    print("Você não ultrapassou a velocidade máxima permitida.")
    print("Sem multa.")