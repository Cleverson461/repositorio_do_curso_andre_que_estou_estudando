# Functions (Funções)
 # DRY - Don't repeat yourself.
 # Realizam uma tarefa
 # Calcula e retorna um Valor
 

def cliente1(nome):
    print(f'Olá, {nome} seja bem-vindo(a) ao nossa loja!')
    

def cliente2(nome):
    return f'Olá, {nome} seja bem-vindo(a).'


x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)