# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/)

# Função para encapsular a lógica da calculadora.

def adicionar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"


# Menu principal
print("=== Calculadora Básica ===")
print("Operações disponíveis:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Solicita a escolha do usuário
operacao = input("Escolha a operação (1/2/3/4): ")

# Solicita os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executa a operação escolhida
if operacao == "1":
    resultado = adicionar(num1, num2)
    simbolo = "+"
elif operacao == "2":
    resultado = subtrair(num1, num2)
    simbolo = "-"
elif operacao == "3":
    resultado = multiplicar(num1, num2)
    simbolo = "*"
elif operacao == "4":
    resultado = dividir(num1, num2)
    simbolo = "/"
else:
    resultado = "Operação inválida"
    simbolo = "?"

# Exibe o resultado
print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")
