import argparse
from part2_functions import *

# PROJETO 2 - PARTE 2

#dimensoes, latitude, longitude, altitude = get_data('SP.pto')

filepath = 'SP.pto'

positions = get_positions(filepath)

indices = get_indices(filepath)

vC = get_vertexCount(filepath)

colors = get_colors(filepath)

with open('outputs/positions.txt', 'w') as file:
    file.write('positions = [')
    for e in positions:
        file.write(str(e))
        file.write(', ')
    file.write(']\n')

with open('outputs/indices.txt', 'w') as file:
    file.write('indices = [')
    for e in indices:
        file.write(str(e))
        file.write(', ')
    file.write(']\n')

with open('outputs/vC.txt', 'w') as file:
    file.write('vC = ')
    file.write(str(vC))
    file.write('\n')
    
with open('outputs/colors.txt', 'w') as file:
    file.write('colors = [')
    for e in colors:
        file.write(str(e))
        file.write(', ')
    file.write(']\n')


