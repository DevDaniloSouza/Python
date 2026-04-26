import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
num4 = random.randint(1, 10)
num5 = random.randint(1, 10)

tupla = (num1, num2, num3, num4, num5)

print(f'Os números sorteados foram: {tupla}')
print(f'O maior número sorteado foi: {max(tupla)}')
print(f'O menor número sorteado foi: {min(tupla)}')