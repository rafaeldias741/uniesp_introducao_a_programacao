# RAFAEL DIAS PEREIRA - EXERCICIO AVALIATIVO
#[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raizes reais).

a = float(input('Digite um valor para A: '))
b = float(input('Digite um valor para B: '))
c = float(input('Digite um valor para C: '))

delta = b**2 - (4*a*c)
x1 = (-(b) + delta**(1/2)) / 2* a
x2 = (-(b) - delta**(1/2)) / 2* a
print(f'X1 é igual a {x1} e X2 é igual a {x2}')