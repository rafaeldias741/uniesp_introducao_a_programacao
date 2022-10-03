#As maçãs custam 1,30 cada, se forem compradas 
#menos de uma dúzia, e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, #calcule e escreva o custo total da compra.

maca = 1.30
print('A maça custa R$ 1.30.')
compras = float(input('Digite quantas maças vc quer comprar:'))
if compras < 12:
   compras =compras * 1.30
   print(f'O valor da compra é de : R$ {compras}')
else:
    compras = compras *1
    print(f'O valor da compra é de R$ {compras}')