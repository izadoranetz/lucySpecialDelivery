import ajuda
import gerenciador_empresas
import gerenciador_drones

print('*****************************************************')
print('Boas-vindas ao Lucy Special Delivery!\n')
print('Nossos drones entregam rapidamente seus pedidos.')
print('*****************************************************\n')

opcao = 0
empresas_cadastradas = []
drones_cadastrados = []
encomendas_cadastrados = []

def opcoes_menu():
    global empresas_cadastradas
    global drones_cadastrados
    global encomendas_cadastrados
    
    while True:

        print('\nMENU PRINCIPAL')
        print('1. Ajuda')
        print('2. Gerenciar drones')
        print('3. Gerenciar empresas parceiras')
        print('4. Gerenciar encomendas de empresas parceiras')
        print('5. Gerenciar remessas')
        print('6. Sair\n')
        
        print(f'Empresas parceiras cadastradas: {len(empresas_cadastradas)}\nDrones disponíveis: {len(drones_cadastrados)}\n\n')

        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            ajuda.exibir_ajuda()
        elif opcao == 2:
            drones_cadastrados = gerenciador_drones.gerenciar_drones(drones_cadastrados)
        elif opcao == 3:
            empresas_cadastradas = gerenciador_empresas.gerenciar_empresas(empresas_cadastradas)
        elif opcao == 4:
            # vai receber empresas_cadastradas e drones_cadastrados
            if len(drones_cadastrados) == 0 and len(empresas_cadastradas) == 0:
                print('Nenhuma empresa e nenhum drone cadastrados. Cadastre uma empresa e um drone antes de gerenciar remessas.')
                continue
            elif len(empresas_cadastradas) == 0:
                print('Nenhuma empresa cadastrada. Cadastre uma empresa antes de gerenciar remessas.')
                continue
            elif len(drones_cadastrados) == 0:
                print('Nenhum drone cadastrado. Cadastre um drone antes de gerenciar remessas.')
                continue
            else:
                print('Gerenciar remessas')
        elif opcao == 5:
            print('Gerenciar remessa')
        elif opcao == 6:
            print('Finalizando programa. Tchau!')
            return
        else:
            print('Opção inválida. Tente novamente.')

opcoes_menu()