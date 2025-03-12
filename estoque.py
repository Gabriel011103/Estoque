#ESTOQUE SIMPLES
#TRATAR EXCESSÕES COMO, SÓ REMOVER UM ITEM EXISTENTE
#NOTIFICAR QUANDO ALGUM DOS ITENS ESTIVER EM ESTOQUE CRITICO
#DEPOIS DE FEITO IMPLEMENTAR CORES DESTACANDO A IMPORTANCIA DE CADA ITEM.
#ADICIONAR CORES AO STATUS, DISPONIVEL, CRITICO, INDISPONIVEL.
import locale
import pickle
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

estoque = []

#uso a função do pickle para guardar os dados da lista
def salvarEstoque(estoque):
    with open('estoque.pkl', 'wb') as f:
        pickle.dump(estoque, f)
    print("REGISTROS SALVOS COM SUCESSO !")

#função para carregar o estoque
def carregarEstoque():
    try:
        with open('estoque.pkl', 'rb') as f:
            estoque = pickle.load(f)
        print ("Estoque carregado com sucesso !")
        return estoque
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Iniciando um novo estoque")
        return []

#ESSA FUNÇÃO PRINTA O ESTOQUE E TRATA A EXCESSÃO(CASO O ESTOQUE ESTEJA VAZIO ELA MOSTARA MENSAGEM) OPCAO 1
def mostrarEstoque(estoque):
    if not estoque:
        print ("Não existe nenhum item no estoque ainda.")
        return
#PARA UMA MELHOR EXPERIÊNCIA DO USUÁRIO E PARA UMA MELHOR REFERÊNCIAÇÃO, USO A FUNÇÃO ENUMERATE PARA NUMERAR OS ITENS 
    for n, item in enumerate(estoque, 1):
        print(f"{n}. {item['ITEM']} - {item['QUANTIDADE']} - R$: {item['VALOR_POR_UNIDADE']}")

#A FUNÇÃO ABAIXO PEDE ENTRADA DE DADOS DO USUÁRIO E CRIA DICIONÁRIO PARA SEREM ADICIONADOS A LISTA (ESTOQUE) OPCAO 2
def adicionarItem(estoque):
    nome = input("ME INFORME O NOME DO ITEM.")
    quantidade = int(locale.atof(input("QUANTAS UNIDADES DEVEM SER ADICIONADAS? ")))
    valorUnidade = locale.atof(input("QUAL VALOR POR UNIDADE? "))
    novoItem = {"ITEM": nome,
    "QUANTIDADE": quantidade,
    "VALOR_POR_UNIDADE": valorUnidade}
    estoque.append(novoItem)
#NESSA FUNÇÃO SUBTRAI O ESTOQUE DO ITEM COM BASE NA ENTRADA DO INPUT DO USUÁRIO OPCAO 3   
def saidaItem(estoque):
    print(estoque)
    if not estoque:
        print ("ESTOQUE VAZIO.")
    else:
        itemSaida = input("QUAL O PRODUTO QUE DESEJA ALTERAR? ")
        saidaQuantidade = int (input("QUANTOS ITENS DEVEM SER DADO BAIXAS?"))
    
        for saida in estoque:
            if saida["ITEM"].lower() == itemSaida and saida["QUANTIDADE"].lower() == saidaQuantidade.lower():
                saida["QUANTIDADE"] -= saidaQuantidade
            print (f"O {itemSaida} FOI ALTERADO COM SUCESSO !")
    
#NESSA FUNÇÃO O ITEM É REMOVIDO TENDO O REFERENCIAL O INPUT DO USUARIO OPCAO 4
def removerItem(estoque):
    print(estoque)
    if not estoque:
        print ("ESTOQUE VAZIO.")
    else:
        qualRemover = input("Qual dos intens acima você deseja remover? ")
    
        for remover in estoque:
            if remover["ITEM"].lower() == qualRemover.lower():
                estoque.remove(remover)
                print(f"tarefa 'qualRemover' removido com sucesso !!")
                return
            print ("ITEM NÃO ENCONTRADO, POR FAVOR TENTE NOVAMENTE.")
#ESSA FUNÇÃO SOMA TODO O VALOR DO ESTOQUE OPCAO 5
def somarEstoque(estoque):
    print(estoque)
    soma_total = sum (item["VALOR_POR_UNIDADE"] for item in estoque)
    print (f"O valor total do seu estoque é de R$: {soma_total}")

estoque = carregarEstoque()

while True:
#ESSA ESTRUTURA DO WHILE FAZ COM QUE O PROGRAMA ESTEJA EM LOOPING ATÉ QUE O USUÁRIO PEÇA SAIDA.    
    
    print ("====================================")
    print ("                MENU                ")
    print ("====================================")
    print ("DIGITE 1. PARA VISUALIZAR O ESTOQUE.")
    print ("DIGITE 2. PARA ADICIONAR UM NOVO ITEM AO SEU ESTOQUE.")
    print ("DIGITE 3. PARA DAR SAIDA ALGUM ITEM DO SEU ESTOQUE.")
    print ("DIGITE 4. PARA REMOVER ALGUM ITEM DO SEU ESTOQUE.")
    print ("DIGITE 5. PARA VISUALIZAR QUANTO VALE O SEU ESTOQUE ATUALMENTE")
    print ("DIGITE 6. PARA SAIR.")
    
    opcao = input("DIGITE A OPÇÃO QUE DESEJA.")
    
    if opcao == "1":
        mostrarEstoque(estoque)
    elif opcao =="2":
        adicionarItem(estoque)
    elif opcao =="3":
        saidaItem(estoque)
    elif opcao =="4":
        removerItem(estoque)
    elif opcao =="5":
        somarEstoque(estoque)
    elif opcao =="6":
        salvarEstoque(estoque)
        print("MUITO OBRIGADO POR USAR ATÉ AQUI.")
        break      
    else:
        print("O NUMERO QUE DIGITOU NÃO CORRESPONDE A NENHUMA DAS OPÇÕES LISTADAS ACIMA, POR FAVOR ESCREVA UM NUMERO VALIDO")