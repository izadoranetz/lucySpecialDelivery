#encomendas_cadastradas = [] #tirar depois
empresas_cadastradas = [[1, 'Empresa SA', 20000091]] #tirar depois
import principal

def gerenciar_encomendas(encomendas):
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
            print(f'{'--------Empresas parceiras disponíveis--------'.center(60)}')
            for empresa in empresas_cadastradas:
                print(f'{'ID empresa'.center(12)}|{'Nome Empresa'.center(30)}|{'CNPJ Empresa'.center(18)}')
                print(f'{str(empresa[0]).center(12)}|{str(empresa[1]).center(30)}|{str(empresa[2]).center(18)}')    
                print()          

                #print(f'{str(empresa.id_empresa).center(14)}|{empresa.nome.center(12)}|{str(empresa.CNPJ).center(18)}')
            id_empresa_remetente = int(input('Informe o ID da empresa remetente: '))
            cpf_destinatario = int(input('Informe o CPF do destinatário: '))
            nome_destinatario = input('Informe o nome do destinatário: ')
            endereco_destinatario = input('Informe o endereço do destinatário: ')
            telefone_destinatario = int(input('Informe o telefone do destinatário: '))
            peso_encomenda = float(input('Informe o peso da encomenda: '))
            nova_encomenda = Encomenda(id_encomenda, id_empresa_remetente, cpf_destinatario, nome_destinatario,  endereco_destinatario, telefone_destinatario, peso_encomenda)
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
    def __init__(self, id_encomenda, id_empresa_remetente, cpf_destinatario, nome_destinatario,  endereco_destinatario, telefone_destinatario, peso_encomenda):
        self.id_encomenda = id_encomenda
        self.id_empresa_remetente = id_empresa_remetente
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
            print(f'{'ID Encomenda'.center(14)}|{'ID Empresa'.center(12)}|{'CPF Destinatário'.center(18)}|{'Nome destinatário'.center(25)}|{'Endereço destinatário'.center(23)}|{'Telefone destinatário'.center(23)}|{'Peso encomenda'.center(15)}')
            
            for encomenda in self.encomendas:
                print(f'{str(encomenda.id_encomenda).center(14)}|{str(encomenda.id_empresa_remetente).center(12)}|{str(encomenda.cpf_destinatario).center(18)}|{encomenda.nome_destinatario.center(25)}|{encomenda.endereco_destinatario.center(22)}|{str(encomenda.telefone_destinatario).center(23)}|{str(encomenda.peso_encomenda).center(15)}')
    
    def excluir_encomenda(self, id_encomenda):
        id_encomenda = int(id_encomenda)
        for encomenda in self.encomendas:
            if encomenda.id_encomenda == id_encomenda:
                self.encomendas.remove(encomenda)
                print('Encomenda removida com sucesso.')
                return
        print('Encomenda não encontrada.')


#encomendas_cadastradas = gerenciar_encomendas(encomendas_cadastradas) #tirar depois