def gerenciar_empresas(empresas):
    sistema_empresas_parceiras = SistemaEmpresasParceiras()
    sistema_empresas_parceiras.empresas = empresas
    
    while True:
        print('\n-------------------------------------------------------------------------------')
        print('3. Gerenciar empresas parceiras')
        print('-------------------------------------------------------------------------------\n')
        print('OPÇÕES')
        print('1. Cadastrar empresa parceira')
        print('2. Listar empresas parceiras')
        print('3. Excluir empresa parceira')
        print('4. Retornar ao menu principal\n')
        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            print('Cadastrar empresa parceira:\n')
            nome_empresa = input('Informe o nome da empresa: ')
            cnpj_empresa = verifica_cnpj_valido()
            endereco_empresa = input('Informe o endereço da empresa: ')
            nova_empresa = EmpresaParceira(nome_empresa, cnpj_empresa, endereco_empresa)
            sistema_empresas_parceiras.cadastrar_empresa(nova_empresa)
        elif opcao == 2:
            print('Listar empresas parceiras:\n')
            sistema_empresas_parceiras.listar_empresas()
        elif opcao == 3:
            print('Excluir empresa parceira:\n')
            if sistema_empresas_parceiras.empresas == []:
                print('Não é possível excluir: nenhuma empresa cadastrada.')
                input('Pressione enter para retornar ao menu anterior ')
                continue
            else:
                cnpj_empresa_excluida = input('Informe o CNPJ da empresa a ser excluída: ')
                sistema_empresas_parceiras.excluir_empresa(cnpj_empresa_excluida)
        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return sistema_empresas_parceiras.empresas
            elif resposta == 'N' or resposta == 'n':
                continue
            else:
                print('Opção inválida. Tente novamente.')
                continue
        else:
            print('Opção inválida. Tente novamente.')


class EmpresaParceira:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
    
class SistemaEmpresasParceiras:
    def __init__(self):
        self.empresas = []
    
    def cadastrar_empresa(self, empresa):
        self.empresas.append(empresa)
        print('Empresa cadastrada com sucesso.\n')
    
    def listar_empresas(self):
        if len(self.empresas) == 0:
            print('Nenhuma empresa cadastrada.')
            input('Pressione enter para retornar ao menu anterior ')
            return
        else:
            print('Empresas parceiras cadastradas: \n')
            print('-----------------------------------------------------------------------------------------')
            print(f'{"Empresa":<10}{"Nome":<40}{"CNPJ":<20}{"Endereço":<40}')
            print('-----------------------------------------------------------------------------------------')
            for i, empresa in enumerate(self.empresas, 1):
                nome = (empresa.nome[:37] + '...') if len(empresa.nome) > 40 else empresa.nome
                cnpj = empresa.cnpj
                endereco = (empresa.endereco[:37] + '...') if len(empresa.endereco) > 40 else empresa.endereco
                print(f'{f"{i}":<10}{nome:<40}{cnpj:<20}{endereco:<40}')
            print('-----------------------------------------------------------------------------------------')
        input('Pressione enter para retornar ao menu anterior ')
    
    def excluir_empresa(self, cnpj):
        for empresa in self.empresas:
            if empresa.cnpj == cnpj:
                self.empresas.remove(empresa)
                print('Empresa removida com sucesso.')
                return
        print('Empresa não encontrada.')

def verifica_cnpj_valido():
    while True:
        cnpj = input('Informe o CNPJ da empresa: ')
        if not cnpj.isnumeric():
            print('CNPJ deve conter apenas números.')
            continue
        if len(cnpj) != 14:
            print('CNPJ deve conter 14 números.')
            continue
        else:
            return cnpj
        