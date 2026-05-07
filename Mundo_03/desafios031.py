def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()

if g.isnumeric():
    g = int(g)
else:
    g = 0

if not n:
    n = '<desconhecido>'

ficha(n, g)
ficha()