# Functions (Funções)
 # DRY - Don't repeat yourself.
 # Parametro --> Argumento
""" def boas_vindas_Marcos():
    print('Olá Marcos')
    print('Temos 5 laptops em estoque')

def boas_vindas_Ronaldo():
    print('Olá Ronaldo')
    print('Temos 4 laptops em estoque')
    
def boas_vindas_Linda():
    print('Olá Linda')
    print('Temos 2 laptops em estoque')


# Chamando a função
boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Linda() """

def boas_vindas(nome, quantidade):
    print(f'Olá, {nome} seja bem-vindo(a) ao nossa loja!')
    print(f'Temos {str(quantidade)} laptops em estoque.')

boas_vindas('Marcos', 5)
print(' ')
boas_vindas('Ronaldo', 10)
print(' ')
boas_vindas('Linda', 10)