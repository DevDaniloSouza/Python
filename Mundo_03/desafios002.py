CampBras = ('Palmeras', 'Flamendo', 'Fluminense', 'São Paulo', 'Bahia', 'Atletico-PR', 'Coritiba', 'Bragantino', 'Bota Fogo', 'Vasco da Gama', 'Grêmio', 'Cruzeiro', 'EC-Vitória', 'Corinthians', 'Atlético-MG', 'Internacional', 'Santos', 'Mirassol', 'Remos', 'Chapecoense')

print(f'Os 5 primeiros colocados são: {CampBras[0:5]}')
print(f'Os 4 últimos colocados são: {CampBras[-4:]}')
print(f'Times em ordem alfabética: {sorted(CampBras)}')
print(f'O Chapecoense está na {CampBras.index("Chapecoense")+1}ª posição.')