
# Erros 
    # Excelente para testes 
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro
    # A função 'get_data' não verifica se o arquivo existe antes de tentar ler os dados
    # A função 'get_data' não verifica se o arquivo é um arquivo Excel
    # A função 'get_data' não trata casos de erros durante a leitura dos dados
    # A função 'get_data' não trata casos de erros durante a escrita dos dados
    # A função 'get_data' não trata casos de erros durante a conversão dos dados
    # A função 'get_data' não trata casos de erros durante a criação do gráfico
    # A função 'get_data' não trata casos de erros durante a exportação do gráfico
    # A função 'get_data' não trata casos de erros durante a validação dos dados


try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')