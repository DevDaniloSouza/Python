import math

angulo = float(input("Digite o valor do ângulo em graus: "))
angulo_rad = math.radians(angulo)
seno = math.sin(angulo_rad)
coseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print("O seno do ângulo é: {:.2f}".format(seno))
print("O coseno do ângulo é: {:.2f}".format(coseno))
print("A tangente do ângulo é: {:.2f}".format(tangente))