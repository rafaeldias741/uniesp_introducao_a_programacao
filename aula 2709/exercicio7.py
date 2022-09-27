cadastros = []

botao = 1000
while botao != 0:
    print('Digite 1 para cadastrar um novo usuário')
    print('Digite 2 para imrprimir um novo usuário')
    print('Digite 0 para sair')
    botao = int(input('Digite a opção desejada: '))

    if botao == 1:
        #Entrada dos dados
        nome = input('Digite o nome: ')
        idade = int(input('Digite sua idade: '))
        email = input('Digite seu e-mail: ')
        #Folha de cadastro
        dados = [nome, idade, email]
        #Guardar a folha de cadastro
        cadastros.append(dados)
    
    elif botao == 2:
        for pessoa in cadastros:
            print(pessoa)

    elif botao == 0:
        print('Obrigado por acessar esse software!')

    else:
        print('Digite um número válido!')
