n = int(input('Diite o valo do seu salário: '))
if n > 1250:
    print('Seu salário agora será de {}'.format(n+(n*0.10)))
else:
    print('Seu salário agora será de {}'.format(n+(n*0.15)))