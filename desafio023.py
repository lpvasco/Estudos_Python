n = str(input('Digite um valor entre 0 e 9999: '))
mil = n[:1]
cen = n[:2]
dez = n[:3]
uni = n[:4]

print('No valor {} existem {} milhares'.format(n,mil))
print('No valor {} existem {} centenas'.format(n,cen))
print('No valor {} existem {} dezenas'.format(n,dez))
print('No valor {} existem {} unidades'.format(n,uni))

