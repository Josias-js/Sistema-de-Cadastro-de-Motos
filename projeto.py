veículos_cadastrados = []
#função para adicionar itens
def adicionar ():
    Modelo = input('Digite o modelo da moto: ')
    linha()
    Empresa = input('Digite o nome da empresa: ')
    linha()
    cor = input('Digite a cor do veículo: ')
    linha()
    Ano_lançamento = int(input('Digite o ano de lançamento da moto: '))
    linha()
    ano_moto = int(input('Digite o ano da moto: '))
    linha()
    cilindradas = int(input('Digite as cilindradas da moto: '))
    linha()
    print('Moto adicionada com sucesso!')    
    veículos_cadastrados.append({'Nome' : Modelo , 'Marca' : Empresa , 'Cor' : cor, 'Ano_moto' : ano_moto , 'Ano_lançamento' : Ano_lançamento , 'Cilindradas' : cilindradas })
#função para mostrar todos os itens já cadastrados
def listar():
    if len(veículos_cadastrados) == 0:
        print('Ainda não foram adicionados veículos.')

    else:
        print('---Veículos Cadastrados---')
        for i in veículos_cadastrados:
            print(f'Modelo : {i['Nome']} - Marca : {i['Marca']} - Cor : {i['Cor']} - Ano da moto : {i['Ano_moto']} - Ano de lançamento : {i['Ano_lançamento']} - Cilindradas : {i['Cilindradas']}')
#função para pesquisar itens cadastrados
def pesquisar():
    if len(veículos_cadastrados) == 0:
         print('Ainda não foram cadastrados veículos')
    else:
        veículos_encontrados = []
        print('-----Pesquisar Veículos-----')
        linha()
        print('[0] Nome\n[1] Marca\n[2] Cor\n[3] Ano da moto\n[4] Ano de lançamento\n[5] Cilindradas')
        linha()
        num = int(input('Por qual característica você desejaria pesquisar? '))
        linha()

        if num == 0 or num == 1 or num == 2:
            especificacao = input('Por quais especificações eu deveria filtrar? ')
            linha()

        else:
            especificacao = int(input('Por quais especificações eu deveria filtrar? '))

        cont=0
        if num == 0:
            for i in veículos_cadastrados:
                if i['Nome'] == especificacao:
                    cont+=1
                    veículos_encontrados.append(i)

        if num == 1:
             for i in veículos_cadastrados:
                if i['Marca'] == especificacao:
                    cont+=1
                    veículos_encontrados.append(i)

        if num == 2:
            for i in veículos_cadastrados:
                if i['Cor'] == especificacao:
                    cont+=1
                    veículos_encontrados.append(i)

        if num == 3:
            for i in veículos_cadastrados:
                if i['Ano_moto'] == especificacao:
                    cont+=1
                    veículos_encontrados.append(i)

        if num == 4:
            for i in veículos_cadastrados:
                if i['Ano_lançamento'] == especificacao:
                    cont+=1
                    veículos_encontrados.append(i)

        if num == 5:
            for i in veículos_cadastrados:
                if i['Cilindradas'] == especificacao:
                    cont+=1
                    veículos_encontrados.append(i)

        print(f'Foram encontradas o total de {cont} ocorrências')
        linha()
        if cont>0:
            for i in veículos_encontrados:
                print(f'Modelo : {i['Nome']} - Marca : {i['Marca']} - Cor : {i['Cor']} - Ano da moto : {i['Ano_moto']} - Ano de lançamento : {i['Ano_lançamento']} - Cilindradas : {i['Cilindradas']}')
                linha()
#função para traçar linhas na tela, organizar melhor o código
def linha():
    print('-'*20)
#função para excluir intens adicionados
def excluir():
        cont = 0
        if len(veículos_cadastrados) == 0:
            print("Não existem motos cadastradas.")

        else:
            print("Motos cadastradas:")
            linha()                
            for i in veículos_cadastrados:
                cont+=1
                print(f' {cont}- | Modelo : {i['Nome']} - Marca : {i['Marca']} - Cor : {i['Cor']} - Ano da moto : {i['Ano_moto']} - Ano de lançamento : {i['Ano_lançamento']} - Cilindradas : {i['Cilindradas']}')

            linha()
            escolha = int(input("Digite o número da moto que deseja excluir: "))

            if escolha >= 1 and escolha <= len(veículos_cadastrados):
                moto = veículos_cadastrados.pop(escolha - 1)
                print(f'A moto {moto} foi removida da lista')
            else:
                print("Essa moto não foi adicionada.")
#função com relatorio de intens já cadastrados
def relatorio():
    print('---Relatórios dos veículos registrados---')
    total = 0
    maior = 0
    menor = 0
    maiorc = 0
    menorc = 0
    maiora = 0
    menora = 0
    if len(veículos_cadastrados) == 0:
        print('Ainda não foi adicionado nenhum veículo')
        linha()

    else:
        for i in veículos_cadastrados:
            total+=1
            if i['Ano_lançamento'] >=2010:
                maior+=1
            else:
                menor+=1

            if i['Cilindradas'] > 500:
                maiorc +=1
            else:
                menorc +=1

            if i['Ano_moto'] >=2010:
                maiora+=1
            else:
                menora +=1
                 
        linha()
        print(f'{total} -----> Veículos cadastrados\n{maior} -----> Veículos com ano de lançamento acima de 2010\n{menor} -----> Veículos com ano abaixo de 2010\n{menorc} -----> Motos com cilindradas inferiores a 500\n{maiorc} -----> Motos com cilindradas superior a 500')
#função para alterar valores dos itens da lista (nome, marca, cor, ano...)
def alterar():
    print('---Alterar Veículo---')
    if len(veículos_cadastrados) == 0:
        print('Ainda não foram cadastrados veículos!')

    else:
        cont = 0
        for i in veículos_cadastrados:
            cont+=1
            print(f' {cont}- | Modelo : {i['Nome']} - Marca : {i['Marca']} - Cor : {i['Cor']} - Ano da moto : {i['Ano_moto']} - Ano de lançamento : {i['Ano_lançamento']} - Cilindradas : {i['Cilindradas']}')
        linha()
        alterar = int(input('Qual número correspondente do veículo que você deseja alterar? '))
        linha()
        print('O que você deseja alterar?\n[0] Nome\n[1] Marca\n[2] Cor\n[3] Ano da Moto\n[4] Ano de lançamento\n[5] Cilindradas\n')
        linha()

        resp = int(input("O que você deseja alterar? "))
        linha()

        if resp == 0:
            valor = input('Digite o valor que você deseja inserir: ')
            veículos_cadastrados[alterar-1]['Nome'] = valor
            print('Veículo alterado com sucesso')

        if resp == 1:
                valor = input('Digite o valor que você deseja inserir: ')
                veículos_cadastrados[alterar-1]['Marca'] = valor
                print('Veículo alterado com sucesso')

        if resp == 2:
                valor = input('Digite o valor que você deseja inserir: ')
                veículos_cadastrados[alterar-1]['Cor'] = valor
                print('Veículo alterado com sucesso')

        if resp == 3:
                valor = input('Digite o valor que você deseja inserir: ')
                veículos_cadastrados[alterar-1]['Ano da moto'] = valor
                print('Veículo alterado com sucesso')

        if resp == 4:
                    valor = input('Digite o valor que você deseja inserir: ')
                    veículos_cadastrados[alterar-1]['Ano de lançamento'] = valor
                    print('Veículo alterado com sucesso')

        if resp == 5:
                    valor = input('Digite o valor que você deseja inserir: ')
                    veículos_cadastrados[alterar-1]['Cilindradas'] = valor
                    print('Veículo alterado com sucesso')

while True:
#menu infinito, até o usuário sair
    print('---- Sistema de Veículos ----')
    linha()
        
    print('[0] Adicionar Veículo\n[1] Listar Veículos\n[2] Pesquisar Veículo\n[3] Alterar Veículo\n[4] Excluir Veículo\n[5] Relatório de Veículos Registrados\n[6] Sair')
    linha()

    teste = (input('Digite o que você deseja fazer: '))
#caso a opção não for válida, ele printa o menu de novo
    if teste.isdigit() and int(teste) in range(7):
        teste = int(teste)

    linha()

    if teste == 0:
        adicionar()

    if teste == 1:
        listar()

    if teste == 2:
        pesquisar()

    if teste == 3:
        alterar()

    if teste == 4:
        excluir()

    if teste == 5:
        relatorio()

    #Encerramento do código
    elif teste == 6:
        break
    
    
print('Obrigado por usar nosso sistema!')