#Solicite ao usuário um valor numérico, inteiro ou real, 
#e verifique se ele é maior ou menor que 10. O programa deve
# escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

usuario = int(input('Digite um número: '))
if usuario >= 10:
    print(f'{usuario} é igual ou maior a 10')
else:
    print(f'{usuario} é menor que 10')