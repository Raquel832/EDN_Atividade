# Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.

import requests


def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # gera exceção se a resposta não for 200
        dados = resposta.json()

        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"\nNome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException:
        print(
            "Falha ao acessar a API. Verifique sua conexão ou tente novamente mais tarde.")


# Executa a função
buscar_usuario()
