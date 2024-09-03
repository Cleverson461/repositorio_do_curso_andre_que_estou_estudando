# Python Object-Oriented Programming
    # Classes
        # Utilizadas para criar Objetos (instances)
        # Objetos são partes dentro de um Class (instancias)
        # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
        # ======================================
        # Class: Frutas
        # Objects: Abacate, Banana...

# criar a classe        
class Funcionarios:
    pass

# criar o objeto
usuario1 = Funcionarios()

# criar os parametros
    # Atributos: dados que caracterizam um objeto
usuario1.nome = "Elena"
usuario1.sobrenome = "Cabral"
usuario1.data_nascimento = "12/01/2009"
usuario1.idade = 15
usuario1.cargo = "Estudante"

# criar os parametros do usuario2
    # Métodos: funções que manipulam os objetos
usuario2 = Funcionarios()
usuario2.nome = "João"
usuario2.sobrenome = "Silva"
usuario2.data_nascimento = "05/10/2005"
usuario2.idade = 19

print(usuario1.nome)
print(usuario2.nome)
print(usuario2.data_nascimento)

# Criar os métodos