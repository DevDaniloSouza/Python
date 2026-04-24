preco = float(input('Digite o preço do produto: R$ '))
print('''Formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Escolha a forma de pagamento: '))

if opcao == 1:
    desconto = preco * 0.10
    total = preco - desconto
    print('Pagamento à vista no dinheiro/cheque. Desconto de 10%: R$ {:.2f}. Total a pagar: R$ {:.2f}.'.format(desconto, total))
elif opcao == 2:
    desconto = preco * 0.05
    total = preco - desconto
    print('Pagamento à vista no cartão. Desconto de 5%: R$ {:.2f}. Total a pagar: R$ {:.2f}.'.format(desconto, total))
elif opcao == 3:
    total = preco
    print('Pagamento em 2x no cartão. Preço final: R$ {:.2f}.'.format(total))
elif opcao == 4:
    parcelas = int(input('Digite o número de parcelas: '))
    juros = preco * 0.20
    total = preco + juros
    print('Pagamento em {}x no cartão. Juros de 20%: R$ {:.2f}. Total a pagar: R$ {:.2f}.'.format(parcelas, juros, total))