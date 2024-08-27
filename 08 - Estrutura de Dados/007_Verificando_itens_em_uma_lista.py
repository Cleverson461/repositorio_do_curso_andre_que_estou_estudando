# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável
    # Permite adicionar, remover e alterar dados
    # Indexação: Utilizar números para acessar os dados
    # Listas podem conter diferentes tipos de dados (heterogêneos)
    # Listas são mutáveis (podem ser alteradas após criação)
    # Listas em Python são implementadas como vetores dinâmicos
    # Listas podem ser criadas usando colchetes []
    # Listas podem ser vazias []
    # Listas podem conter outras listas como elementos
    # Listas podem ser concatenadas com o operador +
    # Listas podem ser repetidas com o operador *
    # Listas podem ser ordenadas com a função sorted()
    # Listas podem ser invertidas com a função reverse()
    # Listas podem ser buscadas com a função index()
    # Listas podem ser filtradas com a função filter()

cor_cliente = input('Digite a cor desejada: ').strip().lower()
cores = ['amarelo', 'verde', 'vermelho', 'preto', 'azul']

if cor_cliente in cores:
    print(f'{cor_cliente} tem em estoque!')
else:
    print(f'{cor_cliente} não temos está cor em estoque disponivel!')