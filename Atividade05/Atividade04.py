# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

# Exercício 4 — Calculadora de Dias de Vida (interativa)

from datetime import datetime

# Solicita a data de nascimento do usuário
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string para objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Obtém a data atual
data_atual = datetime.now()

# Calcula a diferença em dias
dias_vividos = (data_atual - data_nascimento).days

# Exibe o resultado
print(f"\nVocê está vivo há aproximadamente {dias_vividos} dias!")
