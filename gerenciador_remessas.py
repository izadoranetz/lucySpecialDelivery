def gerenciar_remessas(drones, encomendas):
    sistema_remessas = SistemaDeRemessas()
    
    while True:
        print('\n-------------------------------------------------------------------------------')
        print('5. Gerenciar remessas')
        print('-------------------------------------------------------------------------------\n')
        print('OPÇÕES')
        print('1. Criar uma remessa')
        print('2. Consultar remessa')
        print('3. Gerar Itinerário')
        print('4. Retornar ao menu principal\n')
        
        opcao = int(input('Informe o número da opção desejada: '))
        
        if opcao == 1:
            print('Criar uma remessa:\n')
            sistema_remessas.cadastrar_remessa(drones, encomendas)
            #gerar_itinerario()
        elif opcao == 2:
            print('Consultar remessa:\n')
            sistema_remessas.listar_remessas()
        elif opcao == 3:
            print('Gerar Itinerário:\n')
            sistema_remessas.gerar_itinerario(drones, encomendas)
        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return sistema_remessas.remessas
            elif resposta == 'N' or resposta == 'n':
                continue
            else:
                print('Opção inválida. Tente novamente.')
                continue
        else:
            print('Opção inválida. Tente novamente.')
            continue
    

class Remessa:
    def __init__(self, drones, encomendas):
        self.drones = drones
        self.encomendas = encomendas
        self.itinerario = []
    
    def gerar_itinerario(self):
        pass
    
    def finalizar_remessa(self):
        pass

class SistemaDeRemessas:
    def __init__(self):
        self.remessas = []
    
    def cadastrar_remessa(self, drones, encomendas):
        print('Para cadastrar uma remessa, primeiro selecione um drone que fará as entregas:\n')
        #lista os drones
        #selecione o drone
        print('Drones Cadastrados')
        print('--------------------------------')
        print(f'{"ID Drone":<10}{"Capacidade em (kg)":<40}')
        print('--------------------------------')
        for drone in drones:
            print(f'{drone.id_drone:<10}{drone.capacidade_drone:<40}')
        print('--------------------------------\n')

        #loop para seleção e confirmação da seleção do drone
        while True:   
            id_drone_escolhido = input('Informe o ID do Drone desejado: ')
        
            #informa a capacidade do drone
            for drone in drones:
                if drone.id_drone == int(id_drone_escolhido):
                    print(f'Capacidade do Drone selecionado: {drone.capacidade_drone} kg')
                 
            confirmacao = input('Confirma a seleção deste drone? (S/N) ')
        
            if confirmacao == 'N' or confirmacao == 'n':
                continue
            elif confirmacao == 'S' or confirmacao == 's':
                print('Drone selecionado com sucesso.\n')
                break
            else:
                print('Opção inválida, tente novamente.')
                continue
        
        print('Agora, selecione as encomendas vinculadas a remessa:\n')
        print('Encomendas cadastradas')
        print('--------------------------------------------------------------------------------------------------------------------')
        print(f'{"ID Encomenda":<15}{"CNPJ Remetente":<15}{"CPF destinatário":<20}{"Nome destinatário":<20}{"Endereço destinatario":<30}{"Peso encomenda":<10}')
        print('--------------------------------------------------------------------------------------------------------------------')
        #lista encomendas cadastradas
        for encomenda in encomendas:
            print(f'{encomenda.id_encomenda:<15}{encomenda.id_empresa_remetente:<15}{encomenda.cpf_destinatario:<20}{encomenda.nome_destinatario:<20}{encomenda.endereco_destinatario:<30}{encomenda.peso_encomenda:<10}')
        
        #selecione a encomenda
        #verifica se o peso da encomenda é compativel com o drone
        #se sim, confirma a inclusão
        #se não, informa que o peso da encomenda é incompatível com o drone
        
        #adicionar mais uma?
        #sim
        #selecione a encomeda
        
        #não
        #encerra a remessa
        #informa que a remessa foi cadastrada com sucesso
        #informa o número da remessa e o resumo do número de encomendas e peso total das entregas
        
        #pergunta, deseja gerar o itinerário?
        #se sim, inicia a função gerar itinerário
        #se não, volta ao menu anterior
        #remessa = 
        #self.remessas.append(remessa)
        print('Remessa cadastrada com sucesso.\n')
    
    def listar_remessas(self):
        if self.remessas == []:
            print('Nenhuma remessa cadastrada.\n')
        else:
            for remessa in self.remessas:
                print(f'Drones: {remessa.drones}')
                print(f'Encomendas: {remessa.encomendas}')
                print(f'Itinerário: {remessa.itinerario}\n')
    
    def excluir_remessa(self, drones, encomendas):
        for remessa in self.remessas:
            if remessa.drones == drones and remessa.encomendas == encomendas:
                self.remessas.remove(remessa)
                print('Remessa excluída com sucesso.\n')
                return
        print('Remessa não encontrada.\n')
    
    def finalizar_remessa(self, drones, encomendas):
        for remessa in self.remessas:
            if remessa.drones == drones and remessa.encomendas == encomendas:
                remessa.finalizar_remessa()
                print('Remessa finalizada com sucesso.\n')
                return
        print('Remessa não encontrada.\n')
    
    #def gerar_itinerario(self, drones, encomendas):
        
        # lista encadeada
    
    def retornar_remessas(self):
        return self.remessas