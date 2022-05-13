import math
op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente'))
hip = math.hypot(op,ad)
print('O valor da hipotenusa de acordo com os valore inseridos é: {:.3f}'.format(hip))