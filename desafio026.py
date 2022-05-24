frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A apareceu {} vezes.'.format(frase.count('a')))
print('A letra A apareceu pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra A apareceu pela primeira vez na posição {}'.format(frase.rfind('a')+1))