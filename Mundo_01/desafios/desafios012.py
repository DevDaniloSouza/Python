dist = float(input('Digite a distância da viagem em km: '))

if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45

print('O preço da passagem é R$ {:.2f}.'.format(preço))