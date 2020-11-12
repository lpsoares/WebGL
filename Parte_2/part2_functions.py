def get_data(filepath):
    """ 
        Lê os dados do arquivo passado, organiza os dados e retorna:

        latitudes_ = latitudes máxima e mínima
        longitudes_ = longitude máxima e mínima
        dimensoes_ = 
            0 - quantidade de amostras no intervalo da latitude,
            1 - quantidade de amostras no intervalo da longitude, 
            2 - quantidade de valores de altitude 
        altitudes_ = valores de altitudes para cada nó gerado da malha construída 
                        com os valores de latitude e longitude
    """

    
    with open('SP.pto', 'r') as file:
        latitudes_ = file.readline().split()
        longitudes_ = file.readline().split()
        dimensoes_ = file.readline().split()

        altitudes_ = file.read().strip().split()

    altitudes = []
    latitudes = []
    dimensoes = []
    longitudes = []

    for latitude in latitudes_: latitudes.append(float(latitude))
    for longitude in longitudes_: longitudes.append(float(longitude))
    for dimensao in dimensoes_: dimensoes.append(int(dimensao))
    for altitude in altitudes_: altitudes.append(int(altitude))

    dimensoes.append(len(altitudes))

    return dimensoes, latitudes, longitudes, altitudes

def get_positions(filepath):
    """
        As coordenadas são os valores no intervalo 
        das amostras de latitude e longitude,
        ou seja, valores numa malha 66 x 48. Entretanto
        os valores são redimensionados para o centro
        ser a coordenada (0,0).

        Logo, x (latitude) está no intervalo de -33 a 33, 
        enquanto y (longitude) está no intervalo de -24 a 24.
        
        As altitudes estão numa escala de 0 a 10, 
        sendo 10 a altitude máxima.
    """

    dimensoes, latitudes, longitudes, altitudes = get_data(filepath)

    altitude_maxima = max(altitudes)

    x_max = dimensoes[0] # = 66
    y_max = dimensoes[1] # = 48

    i = 0
    positions = []
    for yi in range(y_max):
        for xi in range(x_max):
            x = xi
            y = yi

            # Essa parte realiza o redimensionamento das coordenadas
            if x <= x_max/2:
                x = -x_max/2 + x
            else:
                x = x - x_max/2

            if y <= y_max/2:
                y = -y_max/2 + y
            else:
                y = y - y_max/2

            positions.append(x)
            positions.append(y)
            positions.append(round(altitudes[i]/altitude_maxima * 10, 2))
            i += 1

    return positions

def get_indices(filepath):
    
    dimensoes, latitudes, longitudes, altitudes = get_data(filepath)

    x_max = dimensoes[0] # = 66
    y_max = dimensoes[1] # = 48

    indices = []

    for linha in range(y_max-1):
        for coluna in range(x_max):
            if coluna < x_max - 1:
                indices.append(coluna + 1 + linha*x_max)
                indices.append(coluna + linha*x_max)
                indices.append(x_max + coluna + linha*x_max)

                indices.append(coluna + 1 + linha*x_max)
                indices.append(x_max + coluna + linha*x_max)
                indices.append(x_max + coluna + 1 + linha*x_max)

    return indices

def get_vertexCount(filepath):
    """
        Pega o número de vertex
    """
    
    dimensoes, latitudes, longitudes, altitudes = get_data(filepath)

    x_max = dimensoes[0] # = 66
    y_max = dimensoes[1] # = 48

    n_t = (x_max-1)*2 * (y_max-1) * 3

    return n_t

def get_colors(filepath):
    """
        Devolve a lista de cor por triangulo
        A cor é definida pela altitude
    """

    dimensoes, latitudes, longitudes, altitudes = get_data(filepath)

    colors = []

    for altitude in altitudes:

        if altitude <= 0:
            colors.append(0)
            colors.append(0.2)
            colors.append(1)
            colors.append(1)
        
        elif 0 < altitude and altitude < 800:

            k = altitude/800

            colors.append(round(0.3*k + 0.1, 2))
            colors.append(round(0.7*k + 0.1, 2))
            colors.append(0)
            colors.append(1)

        elif 800 < altitude and altitude < 1300:

            k = (altitude-800)/500

            colors.append(round(0.6*k + 0.4,2))
            colors.append(round(0.6*k + 0.4,2))
            colors.append(0.1)
            colors.append(1)
        
        else:

            k = (altitude-1300)/500

            colors.append(round(0.2*k + 0.8))
            colors.append(round(0.2*k + 0.8))
            colors.append(round(0.2*k + 0.8))
            colors.append(1)

    return colors

