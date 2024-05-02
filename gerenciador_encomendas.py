def gerenciar_encomendas(encomendas, empresas_cadastradas):
    sistema_encomendas = SistemaEncomendas()
    sistema_encomendas.encomendas = encomendas
    
    while True:
        
        print('\nGERENCIAR ENCOMENDAS')
        print('1. Cadastrar encomenda')
        print('2. Listar encomendas')
        print('3. Excluir encomenda')
        print('4. Retornar ao menu principal\n')
        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            print('Cadastrar encomenda:\n')
            if sistema_encomendas.encomendas == []:
                id_encomenda = 1
            else:
                id_encomenda = len(sistema_encomendas.encomendas)+1
            print('Empresas parceiras cadastradas: \n')
            print('----------------------------------------------------')
            print(f'{"CNPJ empresa".ljust(18)}{"Nome Empresa".ljust(34)}')
            print('----------------------------------------------------')
            for empresa in empresas_cadastradas:
                print(f'{str(empresa.cnpj).ljust(18)}{str(empresa.nome).ljust(34)}')
            print('----------------------------------------------------')         
            cnpj_empresa_remetente = input('Informe o CNPJ da empresa remetente: ')
            cpf_destinatario = input('Informe o CPF do destinatário: ')
            nome_destinatario = input('Informe o nome do destinatário: ')
            endereco_destinatario = input('Informe o endereço do destinatário: ')
            telefone_destinatario = input('Informe o telefone do destinatário: ')
            while True:
                peso_encomenda = input('Informe o peso da encomenda (em kg): ')
                try:
                    peso_encomenda = float(peso_encomenda)
                    break 
                except ValueError:
                    print('Valor inválido. Informe valores numéricos, com casas decimais separadas por "." (ponto).')
            nova_encomenda = Encomenda(id_encomenda, cnpj_empresa_remetente, cpf_destinatario, nome_destinatario,  endereco_destinatario, telefone_destinatario, peso_encomenda)
            sistema_encomendas.cadastrar_encomenda(nova_encomenda)
        elif opcao == 2:
            print('Listar encomendas:\n')
            sistema_encomendas.listar_encomendas()
        elif opcao == 3:
            print('Excluir encomenda:\n')
            cnpj_empresa_excluida = input('Informe o ID da encomenda a ser excluída: ')
            sistema_encomendas.excluir_encomenda(cnpj_empresa_excluida)
        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return sistema_encomendas.encomendas
        else:
            print('Opção inválida. Tente novamente.')


class Encomenda:
    def __init__(self, id_encomenda, cnpj_empresa_remetente, cpf_destinatario, nome_destinatario,  endereco_destinatario, telefone_destinatario, peso_encomenda):
        self.id_encomenda = id_encomenda
        self.cnpj_empresa_remetente = cnpj_empresa_remetente
        self.cpf_destinatario = cpf_destinatario
        self.nome_destinatario = nome_destinatario
        self.endereco_destinatario = endereco_destinatario
        self.telefone_destinatario = telefone_destinatario
        self.peso_encomenda = peso_encomenda
    
class SistemaEncomendas:
    def __init__(self):
        self.encomendas = []
    
    def cadastrar_encomenda(self, encomenda):
        self.encomendas.append(encomenda)
        print('Encomenda cadastrada com sucesso.\n')
    
    def listar_encomendas(self):
        
        if len(self.encomendas) == 0:
            print('Nenhuma encomenda cadastrada.\n')
            return
        else:
            print('Encomendas cadastradas: \n')
            print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(f'{"ID Encomenda".ljust(14)}{"CNPJ Empresa".ljust(18)}{"CPF Destinatário".ljust(20)}{"Nome destinatário".ljust(27)}{"Endereço destinatário".ljust(32)}{"Telefone destinatário".ljust(25)}{"Peso encomenda".ljust(17)}')
            print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
            
            for encomenda in self.encomendas:
                print(f'{str(encomenda.id_encomenda).ljust(14)}{str(encomenda.cnpj_empresa_remetente).ljust(18)}{str(encomenda.cpf_destinatario).ljust(20)}{encomenda.nome_destinatario.ljust(27)}{encomenda.endereco_destinatario.ljust(32)}{str(encomenda.telefone_destinatario).ljust(25)}{str(encomenda.peso_encomenda).ljust(17)}')
            print('---------------------------------------------------------------------------------------------------------------------------------------------------------')
    def excluir_encomenda(self, id_encomenda):
        id_encomenda = int(id_encomenda)
        for encomenda in self.encomendas:
            if encomenda.id_encomenda == id_encomenda:
                self.encomendas.remove(encomenda)
                print('Encomenda removida com sucesso.')
                return
        print('Encomenda não encontrada.')