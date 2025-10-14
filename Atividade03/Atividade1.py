# 1- Classificador de Idade

# Crie um programa que solicite a idade do usuário e classifique-o
# em uma das seguintes categorias:

# *Criança (0-12 anos),
# *Adolescente (13-17 anos),
# *Adulto (18-59 anos) ou
# *Idoso (60 anos ou mais).


# Classificador de Idade

idade = int(input("Informe a sua idade: "))

# Verifica e classifica a idade
if idade < 0:
    classificacao = "Idade inválida"
elif idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"\nClassificação: {classificacao}")
