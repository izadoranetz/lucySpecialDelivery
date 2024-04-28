import ajuda
import gerenciar_empresas

print('*****************************************************')
print('Boas-vindas ao Lucy Special Delivery!\n')
print('Nossos drones entregam rapidamente seus pedidos.')
print('*****************************************************\n')

opcao = 0
empresas_cadastradas = []
drones_cadastrados = []

def opcoes_menu():
    global empresas_cadastradas
    global drones_cadastrados
    
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
            # se já tiver cadastrado alguma empresa, essa informação precisa ser mandada de volta pro módulo de gerenciar empresas
            empresas_cadastradas = gerenciar_empresas.gerenciar_empresas(empresas_cadastradas)
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
            print('Finalizando programa. Tchau!')
            # para consulta das empresas cadastradas no outro módulo
            # for i, empresa in enumerate(empresas_cadastradas, 1):
            #     print(f'Empresa {i}:')
            #     print(f'Nome: {empresa.nome}\nCNPJ: {empresa.cnpj}\nEndereço: {empresa.endereco}\n')
            return
        else:
            print('Opção inválida. Tente novamente.')

opcoes_menu()