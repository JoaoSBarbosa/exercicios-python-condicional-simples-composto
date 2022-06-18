print()
print('-' * 10, 'Exercício 2.5.2', '-' * 14)
print()

# Entrada de dados

salario = float(input(' Digite o seu salário atualmente: '))
data_reg = int(input(' Digite o seu ano de registro na empresa: '))
data_atual = int(input(' Digite o ano atual: '))

# pré-processamentos

tempo = data_atual - data_reg

# Condições

if tempo > 10:
    bonus = salario * 0.3
else:
    if tempo > 5:
        bonus = salario * 0.2
    else:
        bonus = salario * 0.1

# Resultado

print()
print(' ► Você tem {} ano(s) nesta empresa \n ► Seu salário atualmente é R$ {} '
      '\n ► Sua bonificação será R$ {} \n ► Seu novo salário será de R$ {}'
      .format(tempo, salario, bonus, salario + bonus))
print()
print('Fim')
