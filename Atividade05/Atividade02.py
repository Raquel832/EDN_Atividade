# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”
# Exercício 2 — Verificador de Palíndromos (interativo e funcional)
# Regra: Enter vazio encerra o programa.

import string


def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo.
    Ignora espaços, pontuação e diferenças de maiúsculas/minúsculas.

    Parâmetros:
    texto (str): palavra ou frase a ser verificada

    Retorna:
    str: "Sim" se for palíndromo, "Não" caso contrário
    """
    # Remove espaços e pontuação, e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    # Verifica se é igual de trás para frente
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# Exemplo de uso
entrada = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(entrada)
print(resultado)
