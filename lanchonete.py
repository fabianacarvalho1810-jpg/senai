print("=== Lá no Charuri ===")
print(" "*4, "Lanchonete" )

nome_cliente = input("Por favor, gigite o seu nome ")
print(f"Olá, {nome_cliente}")

print("=== Nosso cardapio ===")
print("1. Hambúrguer Matador  - R$ 30.00")
print("2. Pizza   - R$ 10.00")
print("3. Sanduiche  - R$ 25.00")
# Recebendo dados do pedido
print("\n Faça o seu pedido" )
qtd_hamburguer = int(input("Quantos hamburgures voce deseja "))
qtd_pizza = int(input("Quantas pizzas voce deseja "))
qtd_sanduiche = int(input("Quantos sanduiche voce deseja "))
#Fechando a conta
total_pedido = qtd_hamburguer + qtd_pizza + qtd_sanduiche



# Exibindo o cupon fiscal
print("\n" + "="*30)
print(" " * 8 + "CUPOM FISCAL" + " " * 8)
print("=" * 30)
print(f"Cliente: {nome_cliente}")
print(f"Hamburguer Matador: {total_hamburguer} ")
print(f"pizza: {total_pizza} ")

print(f"Total do pedido: {valor_total} ")









