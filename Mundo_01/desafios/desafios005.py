dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))

preco = (dias * 60) + (km * 0.15)

print("O preço a pagar é R$ {:.2f}".format(preco))