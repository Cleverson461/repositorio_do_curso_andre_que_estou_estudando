def somar():
    print('Esta funçao vai somar valores')
    
def multi():
    print('Esta funcao via multiplicar valores')
    
def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return -1