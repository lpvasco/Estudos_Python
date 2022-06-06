n1 = int(input('Diite um valor: '))
n2 = int(input('Diite um valor: '))
n3 = int(input('Diite um valor: '))

if n1 > n2 and n1 > n3:
    print('O maior valor é {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O maior valor é {}'.format(n2))
else:
    print('O maior valor é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor valor é {}'.format(n1))
elif n2 < n2 and n2 < n3:
    print('O menor valor é {}'.format(n2))
else:
    print('O menor valor é {}'.format(n3))
