# Escreva um algortimo que leia dois valores numéricos e que pergunte
# ao usuario qual operação ele deseja realizar: Adição, subtração,
# multiplicação ou divisão. Exiba na tela o resultado da operação desejada

print()
print('-' * 10, ' Exercicio 5.1.1', '-' * 15)
print()
print(' Calculadora Online')
print()
print(' Qual operação deseja realizar ?')
op = int(input(
    ' ► 1) Adição \n ► 2) Subtração \n ► 3) Multiplicação \n ► 4) Divisão \n Digite o numero da opção desejada: '))
print()

# Verificar uma opção inválida e sair sem pedir os números

if (op == 1 or op == 2 or op == 3 or op == 4):
    x = float(input(' Digite o primeiro valor: '))
    y = float(input(' Digite o segundo valor: '))

if op == 1:
    res = x + y
    print(' Resultado: {} + {} = {}'.format(x, y, res))
elif op == 2:
    res = x - y
    print(' Resultado: {} - {} = {} '.format(x, y, res))
elif op == 3:
    res = x * y
    print(' Resultado: {} * {} = {}'.format(x, y, res))
elif op == 4:
    res = x / y
    print(' Resultado: {} / {} = {}'.format(x, y, res))
else:
    print(' Opção inválida')
print(' \n \n Encerrando...')
