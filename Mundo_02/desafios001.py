valorCasa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestação = valorCasa / (anos * 12)

if prestação <= salário * 0.30:
    print('Empréstimo pode ser CONCEDIDO. Sua prestação será de R$ {:.2f}.'.format(prestação))
else:
    print('Empréstimo NEGADO. Valor da parcela é muito alto: R$ {:.2f}.'.format(prestação))