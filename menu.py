import ajuda
import gerenciar_empresas

print('*****************************************************')
print('Boas-vindas ao Lucy Special Delivery!\n')
print('Nossos drones entregam rapidamente seus pedidos.')
print('*****************************************************\n')

opcao = 0

def opcoes_menu():
    while True:
        print('\nMENU PRINCIPAL')
        print('1. Ajuda')
        print('2. Gerenciar drones')
        print('3. Gerenciar empresas parceiras')
        print('4. Gerenciar remessas')
        print('5. Sair\n')

        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            ajuda.exibir_ajuda()
        elif opcao == 2:
            print('Gerenciar drones')
        elif opcao == 3:
            gerenciar_empresas.gerenciar_empresas()
        elif opcao == 4:
            print('Gerenciar remessas')
        elif opcao == 5:
            print('Finalizando programa. Tchau!')
            return
        else:
            print('Opção inválida. Tente novamente.')

opcoes_menu()