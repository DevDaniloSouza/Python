nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Média: {:.1f} - REPROVADO'.format(media))
elif 5.0 <= media < 7.0:
    print('Média: {:.1f} - RECUPERAÇÃO'.format(media))
else:
    print('Média: {:.1f} - APROVADO'.format(media))