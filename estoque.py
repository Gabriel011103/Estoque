import locale
import pickle

# Define o local para formatação de números e moedas
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Lista que armazenará os itens do estoque
estoque = []

# Função para salvar os dados do estoque em um arquivo usando pickle
def salvarEstoque(estoque):
    with open('estoque.pkl', 'wb') as f:
        pickle.dump(estoque, f)
    print("REGISTROS SALVOS COM SUCESSO!")

# Função para carregar os dados do estoque de um arquivo
# Se o arquivo não existir, retorna uma lista vazia
def carregarEstoque():
    try:
        with open('estoque.pkl', 'rb') as f:
            estoque = pickle.load(f)
        print("Estoque carregado com sucesso!")
        return estoque
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado. Iniciando um novo estoque.")
        return []

# Função para exibir os itens do estoque
def mostrarEstoque(estoque):
    if not estoque:
        print("Não existe nenhum item no estoque ainda.")
        return
    
    # Exibe os itens numerados
    for n, item in enumerate(estoque, 1):
        print(f"{n}. {item['ITEM']} - {item['QUANTIDADE']} unidades - R$: {item['VALOR_POR_UNIDADE']}")

# Função para adicionar um item ao estoque
def adicionarItem(estoque):
    nome = input("Informe o nome do item: ")
    quantidade = int(locale.atof(input("Quantas unidades devem ser adicionadas? ")))
    valorUnidade = locale.atof(input("Qual o valor por unidade? "))
    
    novoItem = {
        "ITEM": nome,
        "QUANTIDADE": quantidade,
        "VALOR_POR_UNIDADE": valorUnidade
    }
    
    estoque.append(novoItem)

# Função para remover quantidade de um item no estoque
def saidaItem(estoque):
    if not estoque:
        print("ESTOQUE VAZIO.")
        return
    
    itemSaida = input("Qual o produto que deseja alterar? ").lower()
    saidaQuantidade = int(input("Quantos itens devem ser dados baixa? "))
    
    for item in estoque:
        if item["ITEM"].lower() == itemSaida:
            if item["QUANTIDADE"] >= saidaQuantidade:
                item["QUANTIDADE"] -= saidaQuantidade
                print(f"{saidaQuantidade} unidades de {itemSaida} foram removidas do estoque!")
                return
            else:
                print("Quantidade insuficiente no estoque!")
                return
    
    print("Item não encontrado.")

# Função para remover completamente um item do estoque
def removerItem(estoque):
    if not estoque:
        print("ESTOQUE VAZIO.")
        return
    
    qualRemover = input("Qual item deseja remover? ").lower()
    
    for item in estoque:
        if item["ITEM"].lower() == qualRemover:
            estoque.remove(item)
            print(f"Item '{qualRemover}' removido com sucesso!")
            return
    
    print("Item não encontrado, por favor tente novamente.")

# Função para calcular o valor total do estoque
def somarEstoque(estoque):
    if not estoque:
        print("ESTOQUE VAZIO.")
        return
    
    soma_total = sum(item["QUANTIDADE"] * item["VALOR_POR_UNIDADE"] for item in estoque)
    print(f"O valor total do seu estoque é de R$: {soma_total:.2f}")

# Carrega os dados do estoque ao iniciar o programa
estoque = carregarEstoque()

# Loop principal do programa
while True:
    print("====================================")
    print("                MENU                ")
    print("====================================")
    print("1. Visualizar o estoque")
    print("2. Adicionar um novo item")
    print("3. Dar saída de um item")
    print("4. Remover um item")
    print("5. Visualizar o valor total do estoque")
    print("6. Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        mostrarEstoque(estoque)
    elif opcao == "2":
        adicionarItem(estoque)
    elif opcao == "3":
        saidaItem(estoque)
    elif opcao == "4":
        removerItem(estoque)
    elif opcao == "5":
        somarEstoque(estoque)
    elif opcao == "6":
        salvarEstoque(estoque)
        print("MUITO OBRIGADO POR USAR O PROGRAMA!")
        break
    else:
        print("Opção inválida, por favor escolha uma opção válida do menu.")
