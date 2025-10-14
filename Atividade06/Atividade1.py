# Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.

import random
import string

# Solicita o tamanho da senha ao usuário
tamanho = int(input("Digite o tamanho da senha desejada: "))

# Conjunto de caracteres: letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

# Exibe a senha gerada
print(f"\nSenha gerada: {senha}")
