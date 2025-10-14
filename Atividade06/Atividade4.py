# Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests
from datetime import datetime


def consultar_brl():
    url = "https://economia.awesomeapi.com.br/json/last/BRL-USD"  # Cotação BRL para USD

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # lança erro se a resposta não for 200
        dados = resposta.json()

        if "BRLUSD" in dados:
            cotacao = dados["BRLUSD"]
            valor_atual = cotacao["bid"]
            valor_max = cotacao["high"]
            valor_min = cotacao["low"]
            data_hora = datetime.fromtimestamp(
                int(cotacao["timestamp"])).strftime("%d/%m/%Y %H:%M:%S")

            print(f"\nValor atual (BRL → USD): US$ {valor_atual}")
            print(f"Máxima do dia: US$ {valor_max}")
            print(f"Mínima do dia: US$ {valor_min}")
            print(f"Última atualização: {data_hora}")
        else:
            print("Moeda não encontrada ❌")

    except requests.exceptions.RequestException:
        print(
            "Falha ao acessar a API. Verifique sua conexão ou tente novamente mais tarde.")


# Executa a função
consultar_brl()
