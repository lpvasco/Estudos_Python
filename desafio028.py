import random
rand = random.randint(0,5)

n = int(input('Eu pensei em um número de 0 a 5, tente adivinhar: '))

if n == rand:
    print('Parabéns você acertou, o número foi {}'.format(rand))
else:
    print('Você errou, o número foi {}'.format(rand))

print('FIM')
