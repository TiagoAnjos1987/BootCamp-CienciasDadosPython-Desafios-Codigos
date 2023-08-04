valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

#//TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

#//TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

#//TODO: Imprimir a saída no formato especificado neste desafio.

valor_total_dos_hamburgueres = valorHamburguer * quantidadeHamburguer

valor_total_da_bebida = valorBebida * quantidadeBebida

preco_total_do_pedido = valor_total_dos_hamburgueres + valor_total_da_bebida

troco = valorPago - preco_total_do_pedido

print(f'O preço final do pedido é R$ {preco_total_do_pedido: .2f}. Seu troco é R$ {troco: .2f}.')