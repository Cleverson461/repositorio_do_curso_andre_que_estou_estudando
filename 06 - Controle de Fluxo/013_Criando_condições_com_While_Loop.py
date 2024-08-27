# == while Loops ===
# Excelente para loops dependentes de uma condição

# Publicar um produto com comissão de 10% se for acima de R$20

preco_produto = int(input('Digite o valor do seu Produto em R$:'))

while preco_produto > 20:
    preco_produto = (preco_produto * 0.10) + preco_produto
    print(f'O valor final do seu produto será de R${preco_produto}')
    break