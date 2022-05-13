import math
n = float(input('Digite o valor do ângulo: '))
n1 = math.radians(n) 
cos = math.cos(n1)
sin = math.sin(n1)
tan = math.tan(n1)
print('O cosseno é {:.2f}, seno é {:.2f} e a tangente é {:.2f}.'.format(cos,sin,tan))