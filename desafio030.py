from cmath import inf


n = int(input('Digite um valor: '))
n1 = n % 2
if n1 == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é impar'.format(n))