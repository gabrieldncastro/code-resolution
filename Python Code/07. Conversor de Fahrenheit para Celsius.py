"""Conversão de Fahrenheit para Celsius"""

fahrenheit = float(input("Digite um valor em Fahrenheit: "))
celsius = float(5 * (fahrenheit - 32.0) / 9.0)

print(f'A temperatura é {celsius:.1f}ºC')