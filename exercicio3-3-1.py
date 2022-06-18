print()
print('-'*10, 'Exercícios 3.3.1', '-'*15)
print()
nome=input(' Aluno, por favor digite seu nome: ')
ru=int(input(' Seja Bem-Vindo, {} ! \n Por favor, digite seu RU: → '.format(nome)))
print()

if(nome == 'João' and ru == 431559):
    print(' Acesso AUTORIZADO !')

    print()
    m1 = float(input(' Digite a sua média de Lógica de Programação: → '))
    m2 = float(input(' Digite sua média da disciplina de Matemática Computacional: → '))
    m3 = float(input(' Digite sua média da disciplina de Comunicação Empresarial: → '))
    print()
    if (m1 >= 7 and m2 >= 7 and m3 >= 7):
        print(" Parabéns, {} ! Você foi aprovado com as médias: {}, {}, {}".format(nome, m1, m2, m3))
    else:
        print(' Sinto muito, {} ! Você foi reprovado com as médias: {}, {}, {}'.format(nome, m1, m2, m3))

    print(' FIM')
else:
    print(' Acesso não autorizado')

