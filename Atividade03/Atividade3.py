# 3- Conversor de Temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# Conversor de Temperatura


temperatura = float(input("Informe a temperatura: "))
origem = input("Informe a unidade de origem (C, F ou K): ").upper()
destino = input("Informe a unidade de destino (C, F ou K): ").upper()

# Converte a temperatura para Celsius como base
if origem == "C":
    temp_celsius = temperatura
elif origem == "F":
    temp_celsius = (temperatura - 32) * 5 / 9
elif origem == "K":
    temp_celsius = temperatura - 273.15
else:
    print("Unidade de origem inválida.")
    exit()

# Converte de Celsius para a unidade de destino
if destino == "C":
    temperatura_convertida = temp_celsius
elif destino == "F":
    temperatura_convertida = (temp_celsius * 9 / 5) + 32
elif destino == "K":
    temperatura_convertida = temp_celsius + 273.15
else:
    print("Unidade de destino inválida.")
    exit()

# Exibe o resultado formatado
print(f"\n{temperatura:.2f}°{origem} equivale a {temperatura_convertida:.2f}°{destino}")
