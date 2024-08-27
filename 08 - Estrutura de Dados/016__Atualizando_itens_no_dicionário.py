
# Dicionarios
    # Utiliza index no formato de Keys e Values
    # Aceita string, integer, float, boolean...
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável
    # Permite adicionar, remover e alterar dados
    # Indexação: Utilizar números para acessar os dados
    # Dicionários são mutáveis (podem ser alteradas após criação)
    # Dicionários em Python são implementados como hash tables
    # Dicionários podem ser criados usando chaves {}
    # Dicionários podem ser vazios {}
    # Dicionários podem conter diferentes tipos de dados (heterogêneos)
    # Dicionários podem ser utilizados para mapear chaves a valores
    # Dicionários não possuem ordem de inserção
    # Dicionários não podem conter listas como valores
    # Dicionários não podem conter outros dicionários como valores
    # Dicionários podem ser concatenados com o operador +
    # Dicionários podem ser repetidos com o operador *
    # Dicionários podem ser ordenados com a função sorted()
    # Dicionários podem ser invertidos com a função reverse()
    # Dicionários podem ser buscados com a função get()
    # Dicionários podem ser filtrados com a função filter()

aluno = {
#    key    Value    
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'aprovado': True,
}

del aluno['idade']
# aluno['nome'] = 'Jose'
# aluno.update({'nome': 'Maria', 'nota_final': 'B'})
aluno.update({'endereco': 'Rua dos Bobos'})

print(aluno.get('endereco', 'Não existe'))
print(aluno)