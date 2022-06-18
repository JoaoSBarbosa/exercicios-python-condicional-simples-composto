print()
print('-'*10, "Exercicíos Elif", '-'*15)
print()
print(' Escolha o produto \n ► 1) Maçã \n ► 2) Laranja \n ► 3) Banana')
prod = int(input(' Qual a sua escolha: '))
qtd = int(input(' Qual a quantidade ? '))

if prod == 1:
    preco = qtd * 0.50
    print(' Você comprou {} Maçâ(s). Preço total: R$ {}'.format(qtd, preco))

elif prod == 2:
    preco = qtd * 0.25
    print(' Você comprou {} Laranjas.  Preço total: R$ {}'.format(qtd, preco))
elif prod == 3:
    preco = qtd * 0.75
    print(' Você comprou {} Banana(s) . Preço total R$ {}'.format(qtd, preco))
else:
    print(' Opção Invalida')
