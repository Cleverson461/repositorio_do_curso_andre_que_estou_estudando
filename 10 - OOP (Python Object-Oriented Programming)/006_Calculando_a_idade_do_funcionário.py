# Python Object-Oriented Programming
    # Classes
        # Utilizadas para criar Objetos (instances)
        # Objetos são partes dentro de um Class (instancias)
        # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
        # ======================================
        # Class: Frutas
        # Objects: Abacate, Banana...

from datetime import datetime

# criar a Classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

# Criando Objetos
    # Instânciando uma Classe
    # A função __init__ é chamada automaticamente quando um novo objeto é criado
    # A função __init__ recebe os argumentos passados durante a criação do objeto
    # ======================================
    # Funcionario 1: John Doe
    # Funcionario 2: Jane Smith
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Fernada', 'Silva', 2005)
usuario3 = Funcionarios('Cléverson', 'Santana', 2003)

# print
# #print(usuario1.nome, usuario1.sobrenome)
# #print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario3))
print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))
print(Funcionarios.idade_funcionario(usuario3))