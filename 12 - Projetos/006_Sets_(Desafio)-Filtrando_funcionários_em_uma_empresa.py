# Desaafio com 'Sets'

""" 
Criar um programa que gera 3 listas de acordo com a nessicidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
"""

funcinarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Lista1: Funcionários que tem carro e trabalham a noite
lista1 = set(tem_carro).intersection(turno_noite)
print(f"Funcionários que tem carro e trabalham a noite: {lista1}")

# Lista2: Funcionários que tem carro e trabalham durante o dia
lista2 = set(tem_carro).intersection(turno_dia)
print(f"Funcionários que tem carro e trabalham durante o dia: {lista2}")

# Lista3: Funcionários que não tem carro
lista3 = set(funcinarios).difference(tem_carro)
print(f"Funcionários que não tem carro: {lista3}")