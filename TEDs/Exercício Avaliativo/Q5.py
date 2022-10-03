'''Escrever um algoritmo que leia uma quantidade desconhecida de 
números e conte quantos deles estão nos seguintes 
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.'''
botao = 0
int1 = 0
int2 = 0
int3 = 0
int4 = 0
while botao >= 0:
    botao = int(input('Digite um número: '))
    if botao >=0 and botao<=25:
        int1 = int1 +1
    elif botao >=26 and botao<=50:
        int2 = int2 + 1
    elif botao >=51 and botao<=75:
        int3 = int3 + 1
    elif botao >=76 and botao<=100:
        int4 = int4 + 1
    elif botao < 0:
        print(f'A quantidade entre [0-25] é {int1}. A quantidade entre [26-50] é {int2}. A quantidade entre [51-75] é {int3}. A quantidade entre [76-100] é {int4}.')