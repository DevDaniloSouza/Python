velocidade = float(input('Em que velocidade você está dirigindo? '))

if velocidade > 80:
    print('Você foi multado! A velocidade máxima é de 80 km/h.')
    multa = (velocidade - 80) * 7
    print('O valor da multa é R$ {:.2f}.'.format(multa))
else:
    print('Parabéns! Você está dentro do limite de velocidade.')