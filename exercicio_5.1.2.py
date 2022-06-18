# Uma loja de departamentos está oferecendo diferentes formas de pagamento,
# conforme opção a seguir. Faça um algoritmo que leia o valor total de uma
# compra e calcule o valor de pagamento final de acordo com a opção escolhida.
# Se a escolha for pagamento parcelado, calcule também o valor de cada parcela.
# A o final, apresente o valor total da compra e o valor das parcelas:
# ► Pagamentos á vista- Conceder desconto de 5%
# ► Pagamentos em 3x- O valor não sofre alterações;
# ► Pagamento em 5x- Acréscimo de 2%
# ► Pagamento em 10x- Acréscimo 8%

print()
print('-'*15, ' Exercicício 5.1.2','-'*20)
print()
print(' Lojas Barbosa')
print()
valor = float(input(' Digite o valor da compra: '))
print(' Escolha a forma de pagamento \n '
      '► A) Pagamentos á vista- Desconto de 5% \n '
      '► B) Pagamentos em 3x sem juros; \n '
      '► C) Pagamento em 5x- Acréscimo de 2% \n '
      '► D) Pagamento em 10x- Acréscimo 8% ')
op = input('\n Digite a letra da opção desejada: → ')

if op == 'a':
      desc = valor * 0.05
      valorF = (valor-desc)
      print(' \n Desconto recebido → R$ {:.2f} \n Valor a final à pagar R$ {:.2f}'.format(desc, valorF))

elif op == 'b':
      parc = valor / 3
      print(' \n Valor das compras R$ {} \n Quantidades de parcela 3x \n Valor de cada parcela R$ {:.2f}'.format(valor, parc))
elif op == 'c':

      valorF = valor * 1.02
      parc = valorF / 5
      print(' \n Produto parcelado em 5x. \n Total à pagar R$ {:.2f} \n Valor de cada parcela R$ {} '.format(valorF, parc))
elif op == 'd':
      valorF = valor * 1.08
      parc = valorF / 10
      print(' \n Produto parcelado em 10x. \n Total a pagar {:.2f} \n Valor de cada parcela R$ {:.2f}'.format(valorF, parc))
else:
      print(' Opção inválida')



