#Ler as notas da 1a. e 2a. avaliações de um aluno. 
#Calcular a média aritmética simples e escrever uma mensagem que diga se o 
#aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
print('Calcule a média e se você foi aprovado')
nota1 = float(input('Digite o valor da sua primeira avaliação: '))
nota2 = float(input('Digite o valor da sua segunda avaliação: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print(f'Você foi aprovado com média {media}')
else:
    print(f'Você foi reprovado com média {media}')