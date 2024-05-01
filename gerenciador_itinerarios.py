from datetime import datetime, timedelta

def gerenciar_itinerarios(remessa):
    print('Gerando itinerário...')
    itinerario = ListaItinerario()
    for item in remessa:
        itinerario.inserir_destino(item)
    itinerario.travessia_itinerario()
class NohItinerario:
    def __init__(self, encomenda):
        self.encomenda = encomenda
        self.proximo = None

class ListaItinerario:
    def __init__(self):
        self.cabeca = NohItinerario('Centro de Distribuição')
        self.cabeca.proximo = self.cabeca

    def inserir_destino(self, encomenda):
        novo_noh = NohItinerario(encomenda)
        novo_noh.proximo = self.cabeca.proximo
        self.cabeca.proximo = novo_noh

    def travessia_itinerario(self):
        atual = self.cabeca.proximo
        tempo_entrega = datetime.now() + timedelta(minutes=30)
        
        
        print('--------------------------------------------------------------------------------------------------------')
        print(f'{"Previsão da entrega":<25}{"ID da encomenda":<25}{"Destinatário":<20}{"Endereço":<30}')
        print('--------------------------------------------------------------------------------------------------------')
        
        while atual != self.cabeca:
            for encomenda in atual.encomenda.encomendas:  
                print(f'{tempo_entrega.strftime("%d/%m/%y %H:%M"):<25}{encomenda.id_encomenda:<25}{encomenda.nome_destinatario:<20}{encomenda.endereco_destinatario:<30}')
                tempo_entrega += timedelta(minutes=20)
            atual = atual.proximo
        print(f'Retorno ao Centro de Distribuição às {tempo_entrega.strftime("%H:%M")}')
