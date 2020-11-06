with open('SP.pto', 'r') as file:
    latitudes = file.readline().split()
    longitudes = file.readline().split()
    dimensões = file.readline().split()

    pontos_str = file.read().strip().split()

pontos = []
for ponto in pontos_str:
    pontos.append(int(ponto))

p_max = max(pontos)

x_max = int(dimensões[0])
y_max = int(dimensões[1])

i = 0
coordenadas = []
for yi in range(y_max):
    for xi in range(x_max):
        x = xi
        y = yi

        if x <= x_max/2:
            x = -x_max/2 + x
        else:
            x = x - x_max/2

        if y <= y_max/2:
            y = -y_max/2 + y
        else:
            y = y - y_max/2

        coordenadas.append(int(x))
        coordenadas.append(int(y))
        coordenadas.append(round(pontos[i]/p_max * 10, 2))
        i += 1

#print(coordenadas)

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

#print(indices)

n_t = (x_max-1)*2 * (y_max-1)
#print(n_t)

colors = []

for altitude in pontos:


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

#print(colors)

with open('SP.ctr', 'r') as file:
    qtd_pontos_ = file.readline()
    pontos_str = file.read().strip().split()

qtd_pontos = int(qtd_pontos_)

pontos_ = []
for ponto in pontos_str:
    pontos_.append(float(ponto))

#print(qtd_pontos, pontos_)

import numpy as np

latitude = list(np.linspace(float(latitudes[0]), float(latitudes[1]), int(dimensões[1])))
longitude = list(np.linspace(float(longitudes[0]), float(longitudes[1]), int(dimensões[0])))

#print(len(latitude), len(longitude))


# par = longitude
# impar = latitude

idx = []

for e in range(len(pontos_)):
    ponto = pontos_[e]

    if e % 2 == 0:
        #ponto = pontos_[e+1]
        mais_prox = min(longitude, key=lambda x: abs(x - ponto))
        x = longitude.index(mais_prox)

        xi = x

        if x <= x_max/2:
            x = -x_max/2 + x
        else:
            x = x - x_max/2

        idx.append(-x)
        
    else:
        #ponto = pontos_[e-1]
        mais_prox = min(latitude, key=lambda x: abs(x - ponto))
        y = latitude.index(mais_prox)

        yi = y

        if y <= y_max/2:
            y = -y_max/2 + y
        else:
            y = y - y_max/2

        idx.append(-y)

        #idx.append(12)
        idx.append(round(pontos[-(yi * 66 + xi)]/p_max * 10 + 0.5, 2))

    #print(xi, yi)

print(idx)

idx_idx = []

for e in range(79):
    idx_idx.append(e)

#print(idx_idx)