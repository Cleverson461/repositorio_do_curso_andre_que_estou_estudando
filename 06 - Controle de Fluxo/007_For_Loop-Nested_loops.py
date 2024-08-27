# == For Loop Nested Loops ==
    # Outer loop
    # Inner loop
    
for numero1 in range(1, 6):
    print(f'Dentro do Outer Loop: {numero1}')
    for numero2 in range(6):
        print(f'Inner Loop: {numero1} {numero2}')