
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