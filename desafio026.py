n = str(input('Digite uma frase: ')).lower().strip()
print('A letra A apareceu {} vezes.'.format(n.count('a')))
print('A letra A apareceu pela primeira vez na posição {}'.format(n.find('a')+1))
print('A letra A apareceu pela primeira vez na posição {}'.format(n.rfind('a')+1))