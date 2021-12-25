"""Coversor de real para dólar"""

real = float(input("Coloque um valor em reais "))
cota = 5.67
dolar = float(real * cota)

print(f'{real:.2f} Reais equivalem a {dolar:.2f} dólares')
