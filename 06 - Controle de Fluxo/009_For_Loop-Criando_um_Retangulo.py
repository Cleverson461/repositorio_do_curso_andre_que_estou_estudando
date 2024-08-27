# == For Loop Nested Loops ==
    # Outer loop
    # Inner loop
    
# Criar um retangulo de 6x6

linhas = 6
colunas = 6
simbolos = "|"
simbolos2 = "-"
simbolos3 = "|"

for l in range(linhas):
    for c in range(colunas):
        print(simbolos, end=" ")
        print(simbolos2, end=" ")
        print(simbolos3, end="")
    print()