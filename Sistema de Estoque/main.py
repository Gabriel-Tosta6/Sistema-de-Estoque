lista_produtos = []
#Cadastro de produto
def cadastrar_produtos(lista_produtos):
    print("\n--- Cadastro de Produtos ---")
    while True:
        try:
            codigo=int(input('\nDigite o código do produto:\n'))
            for p in lista_produtos:
                if p['codigo'] == codigo:
                    print('O código inserido já está cadastrado em um produto')
                    return
            nome= input('Digite o nome do produto:\n')
            preco= float(input('Digite o preço do produto:\nR$'))
            quant= int(input('Digite a quantidade de produtos:\n'))
            dic_produtos={
            'codigo':    codigo,
            'nome':     nome,
            'preco':    preco,
            'quantidade':   quant
        }
            lista_produtos.append(dic_produtos)
            print('\nO cadastro foi efetuado com sucesso!\n')
            break
        except:
            print('\nNão foi possível cadastrar o produto, tente novamente!\n')

#Lista de Produtos    
def lista(lista_produtos):
    print("\n--- Lista de Produtos Cadastrados ---\n")
    if not lista_produtos:
        print('\nNão há nenhum produto cadastrado!\n')
        return
    quantidade_total_itens = 0
    valor_total_estoque = 0.0
    print(f'{'Código':<10} {'Nome':<20} {'Preço':<8}   {'Quantidade':<5}')
    for p in lista_produtos:
        print(f"{p['codigo']:<10} {p['nome']:<20} R${p['preco']:<8.2f} {p['quantidade']:<5}\n")
        quantidade_total_itens += p['quantidade']
        valor_total_estoque += p['preco'] * p['quantidade']
    print("-" * 50)
    print("\n--- Relatório do Estoque ---")
    print(f"Total de itens no estoque: {quantidade_total_itens}")
    print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")
    print("-" * 28)

#Buscar produtos
def buscar_produto(lista_produtos):
    print("\n--- Buscar Produtos ---")
    while True:
        try:
            codigo_usuario = int(input('\nDigite o código do produto desejado:\n'))
            produto_encontrado = None
            for produto_procurado in lista_produtos:
                if produto_procurado['codigo'] == codigo_usuario: 
                    print('\nProduto encontrado!\n')
                    produto_encontrado = produto_procurado
                    
            if produto_encontrado is not None:
                print(f'{'Código':<10} {'Nome':<20} {'Preço':<8}   {'Quantidade':<5}')
                print(f"{produto_procurado['codigo']:<10} {produto_procurado['nome']:<20} R${produto_procurado['preco']:<8.2f} {produto_procurado['quantidade']:<5}")
                break  
            else:
                print('\nNão há nenhum produto com esse código, tente novamente!\n')
        except:
            print('\nAlgo deu errado, tente novamente!\n')

#Função Alterar Produto:
def alterar_produto(lista_produtos):
    print("\n--- Alterar Produtos ---")
    while True:
        try:
            codigo_usuario = int(input('\nDigite o código do produto que deseja alterar:\n'))
            produto_encontrado = None
            for produto_procurado in lista_produtos:
                if produto_procurado['codigo'] == codigo_usuario: 
                    print('\nProduto encontrado!\n')
                    produto_encontrado = produto_procurado
                    print('\n===Menu de Alterações===\n')
                    print('''1 - Nome do Produto\n
2 - Preço do Produto\n
3 - Quantidade do Produto\n''' )
                    x = int(input('\nO que você deseja alterar?\n'))
                    match x:
                        case 1:
                            nome_novo = str(input('\nQual será o novo nome do produto?:\n'))
                            produto_procurado['nome'] = nome_novo
                            print('\nO nome do produto foi alterado!\n')
                            return
                        case 2:
                            preco_novo = float(input('\nQual será o novo preço do produto?:\nR$'))
                            produto_procurado['preco'] = preco_novo
                            print('\nO preço do produto foi alterado!\n')
                            return
                        case 3:
                            qtde_nova = int(input('\nQual será a nova quantidade do produto?:\n'))
                            produto_procurado['quantidade'] = qtde_nova
                            print('\nA quantidade do produto foi alterada!\n')
                            return
                else:
                    print('\nNão há nenhum produto com esse código, tente novamente!\n')
        except:
            print('\nAlgo deu errado, tente novamente!\n')

#Função Remover Produto
def remover_produto(lista_produtos):
    print("\n--- Remover Produtos ---")
    while True:
        try:
            codigo_procurado = int(input('\nDigite o código do produto que você deseja remover:\n'))
            produto_encontrado = False
            for produto_procurado in lista_produtos:
                if produto_procurado['codigo'] == codigo_procurado: 
                    print('\nProduto encontrado!\n')
                    produto_encontrado = produto_procurado
                    break
            if produto_encontrado:
                print(f'\nProduto encontrado: {produto_encontrado['nome']}, Preço: {produto_encontrado['preco']:.2f}\n')
                confirmação = input('Você realmente deseja remover esse produto? (S para sim, N para não):\n').upper()
                if confirmação == 'S':
                    lista_produtos.remove(produto_encontrado)
                    print("\nProduto removido com sucesso!\n")
                    return
                else:
                    print('\nOperação de remoção cancelada.\n')
                    return
            else:
                print('\nProduto com este código não foi encontrado.\n')

        except:
            print('\nErro: Por favor, digite um código válido (número inteiro).\n')