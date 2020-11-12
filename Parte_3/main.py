import argparse
from part3_functions import *

# PROJETO 2 - PARTE 3

#dimensoes, latitude, longitude, altitude = get_data('SP.pto')

filepath = 'SP.ctr'
filepathPTO = 'SP.pto'

idx_coord = get_coord_line(filepath, filepathPTO)
indices_line = get_indices_line(filepath)

with open('outputs/idx_coord.txt', 'w') as file:
    file.write('idx_coord = [')
    for e in idx_coord:
        file.write(str(e))
        file.write(', ')
    file.write(']\n')

with open('outputs/indices_line.txt', 'w') as file:
    file.write('indices_line = [')
    for e in indices_line:
        file.write(str(e))
        file.write(', ')
    file.write(']\n')