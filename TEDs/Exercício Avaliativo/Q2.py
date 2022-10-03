#[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, P(x1, y1) e Q(x2, y2), imprima a distância entre eles.
#A formulá que efetua tal cálculo é: d = (x2 - x1)2 + (y2 - y1)2
print('Digite os valores para P')
x1 = float(input('Digite um valor para x1: '))
y1 = float(input('Digite um valor para y1: '))
print('Digite os valores para Q')
x2 = float(input('Digite um valor para x2: '))
y2 = float(input('Digite um valor para y2: '))

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print(f'Essa é a distância entre P e Q: {d}')