def gerenciar_empresas():
    print('\n3. Gerenciar empresas parceiras:')
    
    print('\n    1. Cadastrar empresa parceira')
    print('    2. Listar empresas parceiras')
    print('    3. Excluir empresa parceira')
    print('    4. Retornar ao menu principal\n')
    
    
    while True:
        opcao = int(input('Informe o número da opção desejada: '))
        
        if opcao == 1:
            print('Cadastrar empresa parceira')
        elif opcao == 2:
            print('Listar empresas parceiras')
        elif opcao == 3:
            print('Excluir empresa parceira')
        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return
        else:
            print('Opção inválida. Tente novamente.')
    