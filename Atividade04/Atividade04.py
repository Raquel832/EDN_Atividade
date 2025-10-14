# Analisador de números: pares e ímpares

pares = 0
impares = 0

print("=== Analisador de Números ===")
print("Digite números inteiros. Para sair, digite 'sair'.")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == "sair":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par ✅")
            pares += 1
        else:
            print(f"{numero} é ímpar ✅")
            impares += 1
    except ValueError:
        print("Entrada inválida! Digite um número inteiro ou 'sair'.")

# Exibe o resultado final
print("\n=== Resultado Final ===")
print(f"Números pares digitados: {pares}")
print(f"Números ímpares digitados: {impares}")
