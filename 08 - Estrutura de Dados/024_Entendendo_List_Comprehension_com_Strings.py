""" https://docs.python.org/3/tutorial/datastructures.html """

# List Comprehension
    # Mais simples de se escrever
    # Utilizando quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for iten in itens]
    # Permite usar operadores matemáticos, lógicos, condicionais, e funções
    # Permite usar funções built-in do Python
    # Permite usar funções customizadas
    # Permite usar list comprehension em qualquer estrutura de dados (listas, tuplas, dicionários)
    # É mais eficiente que loops normais
    # Permite fazer loops sem precisar de variáveis auxiliares
    # Permite transformar listas em outras listas
    # Permite usar expressões para gerar novos elementos
    
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
""" frutas2 = []

for iten in frutas1:
    if 'n' in iten:
        frutas2.append(iten) """

frutas2 = [iten for iten in frutas1 if 'k' in iten]

print(frutas2)

