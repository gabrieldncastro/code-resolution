"""Conversão de km/h para m/s"""

quilometros = float(input("Valor em km/h: "))
metros = float(quilometros / 3.6)

print(f'{quilometros:.1f} Quilômetros por hora equivale a {metros:.1f} metros por segundo.')
