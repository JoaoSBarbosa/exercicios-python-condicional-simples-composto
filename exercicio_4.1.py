# Escreva um algortimo em Python em que o usuário escolhe se ele quer comprar
# maçãs, Laranjas ou bananas. Deverá ser apresentado na tela um menu com opções
# 1 para maçã, 2 para laranja e 3 para banana. Após escolhido a fruta, deve-se
# digitar quantas unidades se quer comprar. O algortimo deve calcular o preço total
# a pagar do produto escolhido e mostrá-lo na tela. Considere que uma maçã custa R$ 2,30,
# uma laranja R$ 3,60 e uma Banana R$ 1,85

print()
print('-' * 10, ' Exercício 4.1', '-' * 14)
print()
print(' Escolha o produto: \n \n ► 1- Maçã \n ► 2- Laranja \n ► 3- Banana')
produto = int(input(' \n Qual a sua escolha ? '))
qtd = int(input(' \n Qual a quantidade ? '))

if produto == 1:
    preco = qtd * 2.35
    print('\n Você comprou {} maçã(s). Total á pagar: R$ {}'.format(qtd, preco))
else:
    if produto == 2:
        preco = qtd * 3.60
        print(' \n Você comprou {} Laranja(s). Total à pagar: R$ {}'.format(qtd, preco))
    else:
        if produto == 3:
            preco = qtd * 1.85
            print(' \n Você comprou {} Bananas. Total a pagar R$ {}'.format(qtd, preco))
        else:
            print(' ERRO')
