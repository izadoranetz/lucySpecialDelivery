import gerenciador_itinerarios

def gerenciar_remessas(drones, encomendas):
    sistema_remessas = SistemaDeRemessas()
    
    while True:
        print('\n-------------------------------------------------------------------------------')
        print('5. Gerenciar remessas')
        print('-------------------------------------------------------------------------------\n')
        print('OPÇÕES')
        print('1. Criar uma remessa e gerar itinerário')
        print('2. Consultar remessa')
        print('3. Retornar ao menu principal\n')
        
        opcao = int(input('Informe o número da opção desejada: '))
        
        if opcao == 1:
            print('Criar uma remessa e gerar itinerário:\n')
            sistema_remessas.cadastrar_remessa(drones, encomendas)
        elif opcao == 2:
            print('Consultar remessa:\n')
            sistema_remessas.listar_remessas()
        elif opcao == 3:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return
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
    
    def gerar_itinerario(self):
        pass
    
    def finalizar_remessa(self):
        pass

class SistemaDeRemessas:
    def __init__(self):
        self.remessas = []
    
    def cadastrar_remessa(self, drones, encomendas):
        print('Para cadastrar uma remessa, primeiro selecione um drone que fará as entregas:\n')
        #lista os drones para seleção
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
            drone_escolhido = None
        
            #informa a capacidade do drone
            for drone in drones:
                if drone.id_drone == int(id_drone_escolhido):
                    print(f'Capacidade do Drone selecionado: {drone.capacidade_drone} kg')
                    drone_escolhido = drone
                 
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
        #lista encomendas cadastradas
        print('Encomendas cadastradas')
        print('--------------------------------------------------------------------------------------------------------------------')
        print(f'{"ID Encomenda":<15}{"CNPJ Remetente":<15}{"CPF destinatário":<20}{"Nome destinatário":<20}{"Endereço destinatario":<30}{"Peso encomenda":<10}')
        print('--------------------------------------------------------------------------------------------------------------------')
        for encomenda in encomendas:
            print(f'{encomenda.id_encomenda:<15}{encomenda.id_empresa_remetente:<15}{encomenda.cpf_destinatario:<20}{encomenda.nome_destinatario:<20}{encomenda.endereco_destinatario:<30}{encomenda.peso_encomenda:<10}')
        print()
        
        #loop de seleção
        encomenda_encerrada = False
        peso_utilizado = 0
        peso_capacidade = drone_escolhido.capacidade_drone
        #lista com os ids das encomendas escolhidas para evitar repetição na seleção
        encomendas_escolhidas = []
        
        while True:
            if encomenda_encerrada == True:
                break
            print(f'Capacidade do drone: {peso_capacidade} kg')
            print(f'Peso da remessa: {peso_utilizado} kg')
            id_encomenda_escolhida = input('Informe o ID da encomenda desejada ou FINALIZAR: ')
            #verificações
            #se quer finalizar
            if id_encomenda_escolhida == 'FINALIZAR' or id_encomenda_escolhida == 'finalizar':
                print('Fechando remessa...\n')
                encomenda_encerrada = True
                break
            #se o número da encomenda existe (usa list comprehension para iterar nos ids de encomendas)
            if int(id_encomenda_escolhida) not in [encomenda.id_encomenda for encomenda in encomendas]:
                print('Encomenda não encontrada.\n')
                continue
            #se o número já não foi informado
            elif id_encomenda_escolhida in encomendas_escolhidas:
                print('Encomenda já selecionada.\n')
                continue
            
            #vincula o objeto da encomenda com aquele cujo id foi selecionado
            encomenda_escolhida = None
            for encomenda in encomendas:
                if encomenda.id_encomenda == int(id_encomenda_escolhida):
                    encomenda_escolhida = encomenda
                    break

            #se peso é compatível com a carga do drone e da remessa
            if peso_utilizado + encomenda_escolhida.peso_encomenda > peso_capacidade:
                print('Peso da encomenda incompatível com a carga do drone.\n')
                continue
            
            confirmacao = input('Confirma a seleção desta encomenda? (S/N) ')
            if confirmacao == 'N' or confirmacao == 'n':
                continue
            elif confirmacao == 'S' or confirmacao == 's':
                encomendas_escolhidas.append(encomenda_escolhida)
                print('Encomenda selecionada com sucesso.')
                peso_utilizado += encomenda_escolhida.peso_encomenda
                
                #se a carga total já foi atingida
                if float(peso_utilizado) == float(peso_capacidade):
                    print('Carga do drone atingida. Fechando remessa...\n')
                    encomenda_encerrada = True
                    break
                
                resposta = input('Deseja adicionar mais uma encomenda? (S/N) ')
                    
                if resposta == 'S' or resposta == 's':
                    continue
                elif resposta == 'N' or resposta == 'n':
                    encomenda_encerrada = True
                    break
                else:
                    print('Opção inválida, tente novamente.')
                    continue
            else:
                print('Opção inválida, tente novamente.')
                continue
        
        print(f'{len(encomendas_escolhidas)} encomenda(s) vinculada(s). Peso total da remessa {peso_utilizado} kg.')
        
        if len(encomendas_escolhidas) == 0:
            print('Nenhuma encomenda selecionada. Remessa não criada.\n')
            return
        else:
            nova_remessa = Remessa(drone_escolhido, encomendas_escolhidas)
            self.remessas.append(nova_remessa)
            print('Remessa criada com sucesso!')

            #inicia a função gerar itinerário
            gerenciador_itinerarios.gerenciar_itinerarios(self.remessas)
            #printa a lista do itinerário
            
        
    
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
        # direciona para módulo com lista encadeada
    
    def retornar_remessas(self):
        return self.remessas
