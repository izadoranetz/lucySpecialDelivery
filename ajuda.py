def exibir_ajuda():
    print('\n1. Ajuda:')
    print('\n1) Para que serve este sistema?\n')
    print('   Este sistema, Lucy Special Delivery, é um serviço de entregas especializado\n   em medicamentos fornecendo entregas rápidas e seguras para farmácias\n   localizadas na Asa Sul, especificamente na rua das farmácias.')
    print('\n2) Como utilizar este sistema?\n')
    print('   Para utilizar este sistema, siga estes passos:')
    print('      1. Inclua ou tenha pelo menos um drone na frota usando a opção "2. Gerenciar drones".')
    print('      2. Inclua ou tenha uma empresa parceira registrada usando a opção de "3. Gerenciar empresas parceiras".')
    print('      3. Gere uma remessa contendo as encomendas a serem entregues usando a opção "4. Gerenciar remessas".')
    print('      4. Inclua as encomendas na remessa criada.')
    print('      5. Finalize a remessa para iniciar o processo de entrega.\n')
    print('   Quando a remessa é finalizada e o processo de entrega é iniciado,\n   o sistema irá gerar o itinerário indicando a ordem de entrega\n   dos medicamentos. Após a conclusão do processo de entrega,\n   o drone sairá para entrega conforme o itinerário gerado.\n')
    print('   Finalize o programa quando todas as entregas forem concluídas.\n')
    
    opcao = input('Retornar ao menu principal? (S/N) ')
    if opcao == 'S' or opcao == 's':
        return