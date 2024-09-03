# Python Object-Oriented Programming
    # Classes
        # Utilizadas para criar Objetos (instances)
        # Objetos são partes dentro de um Class (instancias)
        # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
        # ======================================
        # Class: Frutas
        # Objects: Abacate, Banana...

class Funcionarios:
    # Atributos (variáveis)
        # O nome e o salário são atributos da classe Funcionarios
        # Atributos são dados que um objeto possui
        # Um objeto pode ter vários atributos diferentes, mas todos compartilham os mesmos valores
    nome = "Elena"
    sobrenome = "Cabral"
    data_nascimento = "12/01/2009"

usuario1 = Funcionarios()
print(usuario1.nome)
print(usuario1.sobrenome)
print(usuario1.data_nascimento)