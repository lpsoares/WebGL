
with open('SP.pto', 'r') as file:
    latitudes = file.readline().split()
    longitudes = file.readline().split()
    dimensões = file.readline().split()

    pontos = file.read().strip().split()

x_max = int(dimensões[0])
y_max = int(dimensões[1])

i = 0
coordenadas = []
for y in range(y_max):
    for x in range(x_max):
        coordenadas.append(x)
        coordenadas.append(y)
        coordenadas.append(int(pontos[i]))
        i += 1

#print(coordenadas)

indices = []

for linha in range(y_max-1):
    for coluna in range(x_max):
        if coluna > 0:
            indices.append(coluna + linha*x_max)
            indices.append(x_max + coluna + linha*x_max)
            indices.append(x_max + coluna + 1 + linha*x_max)

        if coluna < x_max - 1:
            indices.append(coluna + 1 + linha*x_max)
            indices.append(coluna + linha*x_max)
            indices.append(x_max + coluna + linha*x_max)

print(indices)

n_t = (x_max-1)*2 * (y_max-1)
#print(n_t)

colors = []

for altitude in pontos:
    altitude = int(altitude)

    if altitude <= 0:
        colors.append(0)
        colors.append(0)
        colors.append(255)
        colors.append(1)

    elif 0 > altitude and altitude <= 100:
        colors.append(0)
        colors.append(119)
        colors.append(0)
        colors.append(1)
    
    elif 100 > altitude and altitude <= 200:
        colors.append(108)
        colors.append(226)
        colors.append(0)
        colors.append(1)

    elif 200 > altitude and altitude <= 300:
        colors.append(254)
        colors.append(254)
        colors.append(128)
        colors.append(1)

    elif 300 > altitude and altitude <= 400:
        colors.append(233)
        colors.append(175)
        colors.append(58)
        colors.append(1)

    elif 400 > altitude and altitude <= 500:
        colors.append(230)
        colors.append(116)
        colors.append(4)
        colors.append(1)

    elif 500 > altitude and altitude <= 600:
        colors.append(182)
        colors.append(19)
        colors.append(0)
        colors.append(1)

    elif 600 > altitude and altitude <= 700:
        colors.append(128)
        colors.append(0)
        colors.append(0)
        colors.append(1)
    
    else:
        colors.append(255)
        colors.append(0)
        colors.append(0)
        colors.append(1)

colors_out = []

for cor in colors:
    if cor != 1:
        colors_out.append(round(cor/255, 2))
    else:
        colors_out.append(cor)

#print(colors_out)