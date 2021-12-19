"""Conversão de Celsius para Fahrenheit"""

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = float(celsius * (9.0 / 5.0) + 32)

print(f'A temperatura é {fahrenheit:.1f} graus Fahrenheit.')
