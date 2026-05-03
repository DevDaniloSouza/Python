valores = []

for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'O menor valor digitado foi {min(valores)} na posição ', end='')

for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
print()

print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print()
