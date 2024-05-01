def gerenciar_itinerarios(encomendas_cadastradas):
   
    while True:
        
        print('\nGERENCIAR ITINERÁRIOS')
        print('1. Criar itinerário')
        print('2. Visualizar itinerário')
        print('3. Excluir itinerário')
        print('4. Retornar ao menu principal\n')
        opcao = int(input('Informe o número da opção desejada: '))

        if opcao == 1:
            print('Criar itinerário:\n')
 
        elif opcao == 2:
            print('Visualizar itinerário:\n')

        elif opcao == 3:
            print('Excluir itinerário:\n')

        elif opcao == 4:
            resposta = input('Retornar ao menu principal? (S/N) ')
            if resposta == 'S' or resposta == 's':
                return sistema_itinearios.itinerarios
        else:
            print('Opção inválida. Tente novamente.')

class NohIntinerario:
    def __init__(self, id_encomenda):
        self.id_encomenda = id_encomenda
        self.proximo = None

class ListaItinerario:
    def __init__(self):
        self.cabeca = NohIntinerario('Centro de Distribuição')
        self.cabeca.proximo = self.cabeca


    def inserir_destino(self, id_encomenda):
        novo_noh = NohIntinerario(id_encomenda)
        atual = self.cabeca

        # Encontrar o penúltimo nó
        while atual.proximo != self.cabeca:
            atual = atual.proximo

        # Inserir o novo nó no penúltimo lugar
        novo_noh.proximo = atual.proximo
        atual.proximo = novo_noh

    def travessia(self):
        atual = self.cabeca
        while atual:
            print(atual.id_encomenda)
            atual = atual.proximo
            if atual == self.cabeca:
                print('Centro de Distribuição')
                break

itinerario = ListaItinerario()
itinerario.inserir_destino('a')
itinerario.inserir_destino('b')
itinerario.inserir_destino('c')
itinerario.travessia()  
