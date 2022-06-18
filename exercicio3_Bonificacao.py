print()
print('-'*10, ' Exercícios 2.5.2', '-'*15)
print()
salario = float(input(' Digite o seu sálario atual: '))
ano_reg = int(input(' Digite o seu ano de registro na empresa: '))
ano_atual = int(input(' Digite o ano atual: '))

tempo = ano_atual - ano_reg

if (tempo > 5):
    bonus = salario * 0.2
else:
    bonus = salario * 0.1
print()
print(' Você tem {} ano(s) dentro desta empresa'.format(tempo))
print(' Seu salário é de R$ {} reais por mês '.format(salario))
print(' Sua bonificação será de R$ {} reais'.format(bonus))
print(' Seu novo salário será R$ {} reais por mês'.format(salario + bonus))
print()
print('-'*10, 'FIM','-'*15)