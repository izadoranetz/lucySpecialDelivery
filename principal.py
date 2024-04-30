import ajuda
import gerenciador_empresas
import gerenciador_drones
import gerenciador_encomendas
import gerenciador_remessas

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
remessas_cadastradas = []

# Descomentar as linhas abaixo mockar dados e facilitar testes
drone1 = gerenciador_drones.Drone(1, 2)
drone2 = gerenciador_drones.Drone(2, 4)
empresa1 = gerenciador_empresas.EmpresaParceira('Farmacia Popular', 10000000000112, 'Rua Asa Sul Loja 1')
empresa2 = gerenciador_empresas.EmpresaParceira('Farmaceutica', 30000000000135, 'Rua Asa Sul Loja 2')
empresa3 = gerenciador_empresas.EmpresaParceira('Farmaceutica Popular de nome Enorme de Grande sera que cabe tudo', 20000000000222, 'Rua Asa Sul Loja 4')
encomenda1 = gerenciador_encomendas.Encomenda(1, 20000000000222, 12345678901, 'João', 'Rua 1', 61999999999, 1)
encomenda2 = gerenciador_encomendas.Encomenda(2, 10000000000112, 12345678902, 'Maria', 'Rua 2', 61999999998, 2)
empresas_cadastradas.append(empresa1)
empresas_cadastradas.append(empresa2)
empresas_cadastradas.append(empresa3)
drones_cadastrados.append(drone1)
drones_cadastrados.append(drone2)
encomendas_cadastradas.append(encomenda1)
encomendas_cadastradas.append(encomenda2)


def opcoes_menu():
    global empresas_cadastradas
    global drones_cadastrados
    global encomendas_cadastradas
    global remessas_cadastradas
    
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
                input('Pressione enter para retornar ao menu principal ')
                continue
            else:
                encomendas_cadastradas = gerenciador_encomendas.gerenciar_encomendas(encomendas_cadastradas, empresas_cadastradas)
        elif opcao == 5:
            # vai receber empresas_cadastradas e drones_cadastrados
            if len(drones_cadastrados) == 0:
                print('Não há drones cadastrados. Cadastre drones antes de gerenciar remessas.')
                input('Pressione enter para retornar ao menu principal ')
                continue
            if len(encomendas_cadastradas) == 0:
                print('Não há encomendas pendentes de entrega. Cadastre encomendas antes de gerenciar remessas.')
                input('Pressione enter para retornar ao menu principal ')
                continue
            else:
                remessas_cadastradas = gerenciador_remessas.gerenciar_remessas(drones_cadastrados, encomendas_cadastradas)
        elif opcao == 6:
            print('Finalizando programa. Tchau!')
            return
        else:
            print('Opção inválida. Tente novamente.')

opcoes_menu()