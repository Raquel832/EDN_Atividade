# 1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
# gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

# Função para calcular gorjeta

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    valor_conta (float): valor total da conta
    porcentagem_gorjeta (float): porcentagem da gorjeta (ex: 10 para 10%)

    Retorna:
    float: valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso
total_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem = float(input("Digite a porcentagem de gorjeta desejada: "))

valor_gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
