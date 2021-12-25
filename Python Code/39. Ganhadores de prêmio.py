""" Cálculo da divisão de um prêmio. O primeiro ganhador receberá 46% do total. O segundo 32% e o terceiro o resto."""

total = 780000.00
ganhador1 = float(total * 0.43) 
ganhador2 = float(total * 0.32)
ganhador3 = float(total - (ganhador1 + ganhador2))

print(f'Ganhador 1: {ganhador1:.2f} \nGanhador 2: {ganhador2:.2f} \nGanhador 3: {ganhador3:.2f}')
