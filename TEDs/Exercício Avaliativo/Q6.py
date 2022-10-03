'''Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 '''

from math import factorial
n = int(input('Fatorial de: '))
print(f'{n}! = ', factorial(n))