"""Programa para ler as dimensões de um terreno e dizer o preço do metro de tela """

c = float(input('Digite o comprimento do terreno (em metros): ')) #comprimento
l = float(input('Digite a largura do terreno(em metros): ')) #largura
p = float(input('Digite o valor da tela: ')) #preço da tela
d = (c * l) #dimensão
total = (d * p) #preço de cercar

print(f'O terreno tem {c}x{l} de comprimento, equivalente a {d} metros quadrados. O preço de cerca-lo é: {total:.2f} Reais')
