#Solicite ao usuário um valor numérico, inteiro ou real, 
#e escrever se é positivo ou negativo (considere o valor zero como positivo).

numero = float(input("Digite um número: "))
if numero >= 0:
    print(f'{numero} é positivio!')
else:
    print(f'{numero} é negativo')