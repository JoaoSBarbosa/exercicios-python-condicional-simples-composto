# Faça um algortimo que receba três valores representando os lados de um triangulo
# fornecido pelo usuário. Verifique se os valores formam um triângulo e classifique como:
# A) Equilátero ( três lados iguais)
# B) Isósceles ( Dois lados iguais);
# C) Escaleno ( Três lados diferentes)

print()
print('-'*10, 'Exercicíos 4.1.2', '-'*15)
print()
a = int(input(' Digite o lado A do triângulo: '))
b = int(input(' Digite o lado B do triângulo: '))
c = int(input(' Digite o lado C do triângulo: '))

print()
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and c + b > a:
        if a == b and b == c:
            print(' Triângulo Equilátero')
        else:
            if a == b or a == c:
                print(' Triângulo Isósceles ')
            else:
                print(' Triângulo Escaleno')
    else:
        print(' Ao menos um valor digitado não serve para formar um triângulo')
else:
    print(' Ao menos um valor digitado não serve para formar um triângulo')