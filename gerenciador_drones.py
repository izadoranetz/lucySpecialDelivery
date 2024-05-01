def gerenciar_drones(drones):
    sistema_drones = SistemaDrones()
    sistema_drones.drones = drones
    
    while True:
        
        print('\nGERENCIAR DRONES')
        print('1. Cadastrar drone')
        print('2. Listar drones cadastrados')
        print('3. Excluir drone cadastrado')
        print('4. Retornar ao menu principal\n')
        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            print('Cadastrar drone:\n')
            if sistema_drones.drones == []:
                id_drone = 1
            else:
                id_drone = len(sistema_drones.drones)+1
            capacidade_drone = float(input('Informe a capacidade do drone (em kg): '))
            novo_drone = Drone(id_drone, capacidade_drone)
            sistema_drones.cadastrar_drone(novo_drone)
        elif opcao == 2:
            print('Listar drones cadastrados:\n')
            sistema_drones.listar_drones()
        elif opcao == 3:
            print('Excluir drone cadastrado:\n')
            id_drone_excluido = int(input('Informe o ID do drone a ser excluído: '))
            sistema_drones.excluir_drone(id_drone_excluido)
        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return sistema_drones.drones
        else:
            print('Opção inválida. Tente novamente.')


class Drone:
    def __init__(self, id_drone, capacidade_drone):
        self.id_drone = id_drone
        self.capacidade_drone = capacidade_drone
    
class SistemaDrones:
    def __init__(self):
        self.drones = []
    
    def cadastrar_drone(self, drone):
        self.drones.append(drone)
        print('Drone cadastrado com sucesso.\n')
    
    def listar_drones(self):
        
        if len(self.drones) == 0:
            print('Nenhum drone cadastrado.\n')
            return
        else:
            print('Drones cadastrados: \n')
            print('--------------------------')
            print(f'{"ID Drone".ljust(10)}{"Capacidade drone".ljust(18)}')
            print('--------------------------')
            for drone in self.drones:
                print(f'{str(drone.id_drone).ljust(10)}{str(drone.capacidade_drone).ljust(18)}')
            print('--------------------------')
    
    def excluir_drone(self, id_drone):
        for drone in self.drones:
            if drone.id_drone == id_drone:
                self.drones.remove(drone)
                print('Drone removido com sucesso.')
                return
        print('Drone não encontrado.')