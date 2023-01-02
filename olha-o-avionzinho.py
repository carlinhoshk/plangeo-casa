import requests
import time

# Coordenadas da localização geográfica (latitude e longitude)
latitude = -23.205034
longitude = -46.775237


# URL da API OpenSky Network
api_url = "https://opensky-network.org/api/states/all"

while True:
    # Envia uma solicitação GET à API
    response = requests.get(api_url)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Extrai os dados da resposta
        data = response.json()

        # Inicializa o contador de aviões
        plane_count = 0

        # Itera pelos dados de estado de cada avião
        for state in data['states']:
            # Extrai as coordenadas de latitude e longitude do avião
            plane_latitude = state[6]
            plane_longitude = state[5]

            # Verifica se as coordenadas do avião estão dentro do raio de 2 km da localização geográfica
            if plane_latitude is not None and plane_longitude is not None:
                if (latitude - plane_latitude)**1 + (longitude - plane_longitude)**1 <= 4:
                    # Incrementa o contador de aviões
                    plane_count += 1

        # Exibe o número de aviões que passaram pela localização geográfica
        print(f"{plane_count} aviões passaram por essa localização.")
    else:
        # Exibe uma mensagem de erro
        print("Ocorreu um erro ao obter os dados da API.")

    # Pausa o loop por 1 minuto antes de enviar a próxima solicitação
    time.sleep(60)
