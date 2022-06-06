n = float(input('Digite quantos KMs tem sua viagem: '))
if n <= 200:
    print('O valor da viagem será {}'.format(n*0.50))
else:
    print('O valor da viagem será {}'.format(n*0.45))

print('FIM')
