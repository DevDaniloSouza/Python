import math

cat_oposto = float(input("Digite o valor do cateto oposto: "))
cat_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cat_oposto, cat_adjacente)
print("A hipotenusa é: {:.2f}".format(hipotenusa))