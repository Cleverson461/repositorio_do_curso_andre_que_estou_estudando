
# Python Object-Oriented Programming
    # Classes
        # Utilizadas para criar Objetos (instances)
        # Objetos são partes dentro de um Class (instancias)
        # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
        # =====================================
        # Classes podem ter atributos (dados) e métodos (funções)
        # Atributos são variáveis que são definidas dentro de uma classe
        # Métodos são funções que são definidas dentro de uma classe
        # Os métodos podem acessar e modificar os atributos da classe
        # ======================================
        # Class: Frutas
        # Objects: Abacate, Banana...
        # Atributos: nome, cor, peso
        # Métodos: comer(), dormir(), crescer()
        # =====================================
        # Instanciar uma Classe:
        # fruta = Frutas('Laranja', 'laranja', 'Terra')
        # fruta.comer()
        # fruta.dormir()
        # fruta.crescer()
        # =====================================
        # Herança:
        # A herança é uma forma de reaproveitar código entre classes
        # Uma Classe é chamada de Superclasse (pai) e a outra Classe é chamada de Subclasse (filha)
        # A Subclasse herda todos os atributos e métodos da Superclasse
        # A Subclasse pode modificar ou adicionar novos atributos e métodos
        # Superclasse: Animal
        # Subclasse
class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat
        
nome = 'Cléverson'
nome_lower = nome.upper()
print(nome_lower)