from Python.Mundo_03.Módulos.desafios035.functions import numeros

num = int(input('Digite um número inteiro: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
