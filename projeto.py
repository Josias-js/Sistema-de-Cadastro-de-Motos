#alterar, pesquisar e excluir
def linha():
    print('-'*20)

def adicionar ():
        lista=[]

        Modelo = input('Digite o modelo da moto que deseja adicionar: ').lower()
        linha()
        Empresa = input('Digite o nome da empresa: ')
        linha()
        print('Temos como cores dispiníveis:\n[1] Preta\n[2] Branca\n[3] Cinza\n[4] Vermelha\n[5] Azul')
        linha()
        cor = int(input('Digite o número da cor da moto: '))
        if cor == 1:
            cor = "Preta"
            print("Você selecionou a cor: Preta")


        elif cor == 2:
            cor = "Branca"
            print("Você selecionou a cor: Branca")

                    
        elif cor == 3:
            cor = "Cinza"
            print("Você selecionou a cor: Cinza")


        elif cor == 4:
             cor = "Vermelha"
             print("Você selecionou a cor: Vermelha")


        elif cor == 5:
             cor = "Azul"
             print("Você selecionou a cor: Azul")

        elif cor not in (1,2,3,4,5):
            while True:
                print('Cor inválida')
                cor = int(input('Digite o número da cor da moto: '))

                if cor in (1,2,3,4,5):
                    break
            
        linha()
        lancamento = int(input('Digite o ano de lançamento da moto: '))
        linha()
        cilindradas = int(input('Digite quantas cilindradas a moto possui: '))
        linha()
        print('Moto cadastrada com sucesso!!')
        lista.append({'Modelo' : Modelo , 'Ano' : lancamento, 'Empresa' : Empresa , 'Cilindradas' : cilindradas})
        veículos_cadastrados.append(lista)


    #MENU

def buscar():
    nome = input('Digite o modelo da moto que você está buscando')
    for i in veículos_cadastrados:
        if i['Modelo'] == nome:
            print(f'Veículo encontrado!!')
            print("Modelo {i['Modelo']} | Ano {i['Ano']}")

veículos_cadastrados = []

while True:
    linha()
    print('---- Sistema de Veículos ----')
    linha()
        
    print('[0] Adicionar Veículo\n[1] Listar Veículo\n[2] Pesquisar Veículo\n[3] Alterar Veículo\n[4] Excluir Veículo\n[5] Relatório de Veículos Registrados\n[6] Sair')
    linha()

    #O que o usuário deseja fazer        
    teste = int(input('Digite o que você deseja fazer: '))
    linha()

    #Se o usuário digitar um número inválido
    if teste not in (0,1,2,3,4,5,6):
        linha()
        print ('Número não executa nenhuma função no menu!\nDigite novemnte')
        linha()

    #Adicionar moto
    if teste == 0:
        adicionar()

    #buscar
    if teste == 2:
        buscar()

    #Encerramento do código
    if teste == 6:
        break
    
print('Obrigado por usar nosso sistema!')
    #Funcionamento do código, teste da resposta do usuário