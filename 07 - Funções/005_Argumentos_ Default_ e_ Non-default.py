# Functions (Funções)
 # DRY - Don't repeat yourself.
 # Parametro --> Argumento
 # Parametro é o dado passado para a função
 # Argumento é o valor que será atribuído à variável definida pelo nome do parametro
 
 # Default = Aquele que você define o valor no parametro
 # Non-Default = Aquele que você não define o valor no parametro


def boas_vindas(quantidade, nome='Linda'):
    print(f'Olá, {nome} seja bem-vindo(a) ao nossa loja!')
    print(f'Temos {str(quantidade)} laptops em estoque.')

boas_vindas(9)