nome = input('Digite um nome: ')

print('O nome tem Silva? {}'.format(nome.lower().find('silva') != -1))