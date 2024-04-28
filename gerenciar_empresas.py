def gerenciar_empresas(empresas):
    sistema_empresas_parceiras = SistemaEmpresasParceiras()
    sistema_empresas_parceiras.empresas = empresas
    
    while True:
        
        print('\n3. Gerenciar empresas parceiras:')
        print('\n    1. Cadastrar empresa parceira')
        print('    2. Listar empresas parceiras')
        print('    3. Excluir empresa parceira')
        print('    4. Retornar ao menu principal\n')
        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            print('Cadastrar empresa parceira:\n')
            nome_empresa = input('Informe o nome da empresa: ')
            cnpj_empresa = input('Informe o CNPJ da empresa: ')
            endereco_empresa = input('Informe o endereço da empresa: ')
            nova_empresa = EmpresaParceira(nome_empresa, cnpj_empresa, endereco_empresa)
            sistema_empresas_parceiras.cadastrar_empresa(nova_empresa)
        elif opcao == 2:
            print('Listar empresas parceiras:\n')
            sistema_empresas_parceiras.listar_empresas()
        elif opcao == 3:
            print('Excluir empresa parceira:\n')
            cnpj_empresa_excluida = input('Informe o CNPJ da empresa a ser excluída: ')
            sistema_empresas_parceiras.excluir_empresa(cnpj_empresa_excluida)
        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return sistema_empresas_parceiras.empresas
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
            print('Nenhuma empresa cadastrada.\n')
            return
        else:
            print('Empresas cadastradas: \n')
            for i, empresa in enumerate(self.empresas,1):
                print(f'Empresa {i}:')
                print(f'Empresa: {empresa.nome}\nCPNJ: {empresa.cnpj}\nEndereço: {empresa.endereco}')
                print()
    
    def excluir_empresa(self, cnpj):
        for empresa in self.empresas:
            if empresa.cnpj == cnpj:
                self.empresas.remove(empresa)
                print('Empresa removida com sucesso.')
                return
        print('Empresa não encontrada.')