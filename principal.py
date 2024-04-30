import ajuda
import gerenciador_empresas
import gerenciador_drones
import gerenciador_encomendas

print('*******************************************************************************')
print()
print(f'{"Boas-vindas ao Lucy Special Delivery! ".center(80)}')
print(f'{"Nossos drones entregam rapidamente seus pedidos.".center(80)}')
print()
print('*******************************************************************************')

opcao = 0
empresas_cadastradas = []
drones_cadastrados = []
encomendas_cadastradas = []

# Descomentar as linhas abaixo para que as listas de empresas cadastradas e drones cadastrados já iniciem pré preenchidos com pelo menos um elemento cada (facilitar testes)
# drone1 = gerenciador_drones.Drone(1, 2)
# empresa1 = gerenciador_empresas.EmpresaParceira('Trololo', 00000000000000, 'Rua etc')
# empresas_cadastradas.append(empresa1)
# drones_cadastrados.append(drone1)


def opcoes_menu():
    global empresas_cadastradas
    global drones_cadastrados
    global encomendas_cadastradas
    
    while True:

        print('\n-------------------------------------------------------------------------------')
        print(f'{"STATUS DO SISTEMA".ljust(80)}')
        print('-------------------------------------------------------------------------------')
        print(f'Empresas parceiras cadastradas: {len(empresas_cadastradas)}'.ljust(80))
        print(f'Drones disponíveis para entregas: {len(drones_cadastrados)}'.ljust(80))
        print(f'Encomendas cadastradas: {len(encomendas_cadastradas)}'.ljust(80))
        print('-------------------------------------------------------------------------------\n')
        
        print('MENU PRINCIPAL')
        print('1. Ajuda')
        print('2. Gerenciar drones')
        print('3. Gerenciar empresas parceiras')
        print('4. Gerenciar encomendas de empresas parceiras')
        print('5. Gerenciar remessas')
        print('6. Sair\n')
        

        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            ajuda.exibir_ajuda()
        elif opcao == 2:
            drones_cadastrados = gerenciador_drones.gerenciar_drones(drones_cadastrados)
        elif opcao == 3:
            empresas_cadastradas = gerenciador_empresas.gerenciar_empresas(empresas_cadastradas)
        elif opcao == 4:
            if len(empresas_cadastradas) == 0:
                print('Nenhuma empresa cadastrada. Cadastre uma empresa antes de gerenciar as encomendas.\n')
                input('Voltar para o menu principal? (S) ')
                continue
            else:
                encomendas_cadastradas = gerenciador_encomendas.gerenciar_encomendas(encomendas_cadastradas, empresas_cadastradas)
        elif opcao == 5:
            # vai receber empresas_cadastradas e drones_cadastrados
            if len(drones_cadastrados) == 0 and len(empresas_cadastradas) == 0:
                print('Nenhuma empresa e nenhum drone cadastrados. Cadastre uma empresa e um drone antes de gerenciar remessas.\n')
                input('Voltar para o menu principal? (S) ')
                continue
            elif len(empresas_cadastradas) == 0:
                print('Nenhuma empresa cadastrada. Cadastre uma empresa antes de gerenciar remessas.\n')
                input('Voltar para o menu principal? (S) ')
                continue
            elif len(drones_cadastrados) == 0:
                print('Nenhum drone cadastrado. Cadastre um drone antes de gerenciar remessas.\n')
                input('Voltar para o menu principal? (S) ')
                continue
            else:
                print('Gerenciar remessas')
        elif opcao == 6:
            print('Finalizando programa. Tchau!')
            return
        else:
            print('Opção inválida. Tente novamente.')

opcoes_menu()