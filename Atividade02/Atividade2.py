# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


# Dados de entrada
produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# Cálculos
desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - desconto

# Exibição dos resultados
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto ({percentual_desconto}%): R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
