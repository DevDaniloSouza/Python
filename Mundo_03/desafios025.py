text = str(input('Digite um texto: '))

def escreva(txt):
    print('=-' * len(txt))
    print(f'{txt:^{len(txt) * 2}}')
    print('=-' * len(txt))

escreva(text)