"""Conversor de radianos para graus"""

radiano = float(input("Digite um valor em radianos: "))
grau = float(radiano * 180 / 3.14)

printf(f'{radiano:.2f} radianos equivale a {grau:.2f} graus')
