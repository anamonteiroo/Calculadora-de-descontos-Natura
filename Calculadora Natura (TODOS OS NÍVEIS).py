print('='*80)
titulo = 'CALCULADORA NATURA'
print('{:^80}'.format(titulo))
print('='*80)
niveis = 'NÍVEIS: SEMENTE, BRONZE, PRATA, OURO E DIAMANTE'
print('{:^80}'.format(niveis))
nivel = str(input('Qual é o seu nível? ')).strip().upper()
if nivel == 'SEMENTE':
    produto = str(input('Qual é o produto? ')).strip().upper()
    valor = float(input('Qual o valor do produto? R$'))
    desconto = float(input('Quanto você quer dar de desconto no produto? Digite 0 para nenhum desconto '))
    pagar = valor * 0.80
    lucro1 = valor * 0.2
    lucro2 = lucro1 - (lucro1 * desconto / 100)
    venda = valor - (valor * desconto / 100)
    print('Você irá pagar R${:.2f} pelo produto {}.'.format(pagar,produto))
    print('Sem o desconto você lucrará R${:.2f}'.format(lucro1))
    if desconto > 0:
        print('Com o desconto você venderá o produto por R${:.2f} e lucrará R${:.2f}.'.format(venda, lucro2))
    else:
        fim = 'FIM'
        print('{:^80}'.format(fim))
if nivel == 'BRONZE' or 'PRATA':
    produto = str(input('Qual é o produto? ')).strip().upper()
    valor = float(input('Qual o valor do produto? R$'))
    desconto = float(input('Quanto você quer dar de desconto no produto? Digite 0 para nenhum desconto '))
    pagar = valor * 0.70
    lucro1 = valor * 0.3
    lucro2 = lucro1 - (lucro1 * desconto / 100)
    venda = valor - (valor * desconto / 100)
    print('Você irá pagar R${:.2f} pelo produto {}.'.format(pagar, produto))
    print('Sem o desconto você lucrará R${:.2f}'.format(lucro1))
    if desconto > 0:
        print('Com o desconto você venderá o produto por R${:.2f} e lucrará R${:.2f}.'.format(venda, lucro2))
    else:
        fim = 'FIM'
        print('{:^80}'.format(fim))
if nivel == 'OURO':
    produto = str(input('Qual é o produto? ')).strip().upper()
    valor = float(input('Qual o valor do produto? R$'))
    desconto = float(input('Quanto você quer dar de desconto no produto? Digite 0 para nenhum desconto '))
    pagar = valor * 0.68
    lucro1 = valor * 0.32
    lucro2 = lucro1 - (lucro1 * desconto / 100)
    venda = valor - (valor * desconto / 100)
    print('Você irá pagar R${:.2f} pelo produto {}.'.format(pagar, produto))
    print('Sem o desconto você lucrará R${:.2f}'.format(lucro1))
    if desconto > 0:
        print('Com o desconto você venderá o produto por R${:.2f} e lucrará R${:.2f}.'.format(venda, lucro2))
    else:
        fim = 'FIM'
        print('{:^80}'.format(fim))
if nivel == 'DIAMANTE':
    produto = str(input('Qual é o produto? ')).strip().upper()
    valor = float(input('Qual o valor do produto? R$'))
    desconto = float(input('Quanto você quer dar de desconto no produto? Digite 0 para nenhum desconto '))
    pagar = valor * 0.65
    lucro1 = valor * 0.35
    lucro2 = lucro1 - (lucro1 * desconto / 100)
    venda = valor - (valor * desconto / 100)
    print('Você irá pagar R${:.2f} pelo produto {}.'.format(pagar, produto))
    print('Sem o desconto você lucrará R${:.2f}'.format(lucro1))
    if desconto > 0:
        print('Com o desconto você venderá o produto por R${:.2f} e lucrará R${:.2f}.'.format(venda, lucro2))
    else:
        fim = 'FIM'
        print('{:^80}'.format(fim))
print('='*80)
fim = 'A NATURA AGRADECE SUA VISITA'
print('{:^80}'.format(fim))
s = input('='*80)

