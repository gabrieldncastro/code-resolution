""" """

total = 780000.00
ganhador1 = float(total * 0.43) 
ganhador2 = float(total * 0.32)
ganhador3 = float(total - (ganhador1 + ganhador2))

print(f'Ganhador 1: {ganhador1:.2f} \nGanhador 2: {ganhador2:.2f} \nGanhador 3: {ganhador3:.2f}')
