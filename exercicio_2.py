print()
print('-'*10, ' Exercicio 2.5.1', '-'*15)
print()
ano_nas = int(input(' Digite o ano do seu nascimento: '))
ano_atual = int(input(' Digite o ano atual: '))

idade = ano_atual - ano_nas
print(' Você tem {} anos de idade '.format(idade))
if (idade >= 18):
    print(" Você já é maior de idade. Já pode: \n - Morar sozinho \n - Tirar habilitação \n - Votar \n - Ser responsavel")
else:
    print(' Você é menor de idade:')