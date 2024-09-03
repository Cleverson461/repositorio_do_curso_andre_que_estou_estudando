# Python Object-Oriented Programming
    # Classes
        # Utilizadas para criar Objetos (instances)
        # Objetos são partes dentro de um Class (instancias)
        # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
        # ======================================
        # Class: Frutas
        # Objects: Abacate, Banana...

# criar a Classe
class Funcionarios:
    
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# Criando Objetos
    # Instânciando uma Classe
    # A função __init__ é chamada automaticamente quando um novo objeto é criado
    # A função __init__ recebe os argumentos passados durante a criação do objeto
    # ======================================
    # Funcionario 1: John Doe
    # Funcionario 2: Jane Smith
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Fernada', 'Silva', '15/10/2005')
usuario3 = Funcionarios('Cléverson', 'Santana', '22/11/1988')

# print
print(usuario1.nome)
print(usuario2.nome, usuario2.data_nascimento)
print(usuario3.sobrenome)