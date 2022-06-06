import calendar
ano = int(input('Digite o Ano:'))
if calendar.isleap(ano):
    print('BISSEXTO')
else:
    print('Não Bissexto')