import numpy as np
from Parte_2.part2_functions import get_data


def get_data_line(filepath):
    """
        Lê o arquivo com os dados e devolve uma lista com as coordenadas
    """

    with open('SP.ctr', 'r') as file:
        qtd_pontos_ = file.readline()
        coordenadas_ = file.read().strip().split()

    qtd_pontos = int(qtd_pontos_)

    coordenadas = []
    for co in coordenadas_:
        coordenadas.append(float(co))

    return coordenadas, qtd_pontos

def get_coord_line(filepath, filepathPTO):
    """
        Retorna as coordenadas da linha na escala utilizada
    """

    # Pega as informações do arquivo .PTO
    dimensoes, latitudes, longitudes, altitudes = get_data(filepathPTO)

    coordenadas, qtd_pontos = get_data_line(filepath)

    latitude = list(np.linspace(float(latitudes[0]), float(latitudes[1]), int(dimensoes[1])))
    longitude = list(np.linspace(float(longitudes[0]), float(longitudes[1]), int(dimensoes[0])))

    # par = longitude
    # impar = latitude

    x_max = latitudes[1]
    y_max = longitudes[1]

    altitude_maxima = max(altitudes)

    idx_coord = []

    for e in range(len(coordenadas)):
        ponto = coordenadas[e]

        if e % 2 == 0:
            mais_prox = min(longitude, key=lambda x: abs(x - ponto))
            x = longitude.index(mais_prox)

            xi = x

            if x <= x_max/2:
                x = -x_max/2 + x
            else:
                x = x - x_max/2

            idx_coord.append(-x)
            
        else:
            mais_prox = min(latitude, key=lambda x: abs(x - ponto))
            y = latitude.index(mais_prox)

            yi = y

            if y <= y_max/2:
                y = -y_max/2 + y
            else:
                y = y - y_max/2

            idx_coord.append(-y)

            idx_coord.append(round(altitudes[-(yi * 66 + xi)]/altitude_maxima * 10 + 0.5, 2))

    return idx_coord

def get_indices_line(filepath):
    """
        Retorna lista de indices da linha
    """

    coordenadas, qtd_pontos = get_data_line(filepath)

    idx_line = []

    for e in range(qtd_pontos):
        idx_line.append(e)

    return idx_line