'''Elabore um algoritmo que leia o valor de dois números inteiros e a operacão aritimética desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operacão aritmética escolhida.
Símbolo
Operação aritmética
+
Adição
-
Subtração
*
Multiplicacão
/
Divisão
**
Potenciação'''

print('CALCULADORA')
numero1 = int(input('Digite o primeiro número:'))
print('Escolha a operação')
print('Digite 1 para somar')
print('Digite 2 para subtrair')
print('Digite 3 para dividir')
print('Digite 4 para multiplicar')
print('Digite 5 para pontencializar')
botao = int(input())
numero2 = int(input('Digite o segundo número: '))
if botao == 1:
    print(numero1 + numero2)
elif botao == 2:
    print(numero1 - numero2)
elif botao == 3:
    print(numero1 / numero2)
elif botao == 4:
    print(numero1 * numero2)
elif botao == 5:
    print(numero1 ** numero2)
else:
    print('Valor inválido')





