exp = str(input('Digite uma expressão: '))

print('A expressão é válida!' if exp.count('(') == exp.count(')') else 'A expressão é inválida!')
