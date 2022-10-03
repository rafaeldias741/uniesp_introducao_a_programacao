'''O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de uma adulto e mostre sua condição.

IMC em adultos
Condição
abaixo de 18,5 abaixo do peso
entre 18,5 e 25 peso normal
25 e 30 acima do peso
acima de 30 obeso

'''
a = float(input('Insira seu peso: '))
b = float(input('Insira sua altura: '))

imc = a / (b)**2

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <25:
    print(f'Peso normal. IMC = {imc:.1f}')
elif imc >= 25 and imc <30:
    print(f'Acima do peso. IMC = {imc:.1f}')
elif imc >30:
    print(f'Você está obeso. IMC = {imc:.1f}')
else: 
    print('Calcule novamente')

