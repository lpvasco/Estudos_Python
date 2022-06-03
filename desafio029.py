velo = int(input('Digite a sua velocidade: '))
multa = (velo-80)*7
if velo > 80:
    print('Você excedeu o limite de 80km/h, deverá pagar uma multa de {} reais'.format(multa))
else:
    print("Ok, tenha um bom dia.")
