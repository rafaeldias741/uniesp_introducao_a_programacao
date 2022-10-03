#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))

if a > b:
    print(f'{a}, {b}')
elif b > a:
    print(f'{b}, {a}')
else:
    print('Valores iguais')


