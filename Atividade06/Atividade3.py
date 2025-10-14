# Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import requests


def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # gera exceção se a resposta não for 200
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado ❌")
        else:
            logradouro = dados.get("logradouro", "")
            bairro = dados.get("bairro", "")
            cidade = dados.get("localidade", "")
            estado = dados.get("uf", "")

            print(f"\nLogradouro: {logradouro}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")

    except requests.exceptions.RequestException:
        print(
            "Falha ao acessar a API. Verifique sua conexão ou tente novamente mais tarde.")


# Solicita o CEP ao usuário
cep_digitado = input("Digite o CEP (somente números): ")
consultar_cep(cep_digitado)
