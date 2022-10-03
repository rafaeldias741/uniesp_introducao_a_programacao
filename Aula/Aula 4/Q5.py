#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor1 = float(input("Digite um valor: "))
valor2 = float(input('Digite um valor: '))
if valor1 > valor2:
    print(valor1)
elif valor2 > valor1:
    print(valor2)
else:
    print('Os valores são iguais')