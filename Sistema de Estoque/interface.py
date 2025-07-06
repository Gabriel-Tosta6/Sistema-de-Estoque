from main import *
import json

def carregar_dados(nome_arquivo='estoque.json'):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(lista_de_produtos, nome_arquivo='estoque.json'):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_de_produtos, arquivo, indent=4, ensure_ascii=False)


ARQUIVO_DE_DADOS = 'estoque.json'
estoque = carregar_dados(ARQUIVO_DE_DADOS)

while True:
    print('''\n--- Sistema de Controle de Estoque ---
1- Cadastrar produto
2- Listar produtos
3- Consultar produto por código
4- Alterar produto
5- Remover produto
6- Sair''')
    
    opcao = input("Escolha uma opção: ")

    match opcao:
        case '1':
            cadastrar_produtos(estoque)

        case '2':
            lista(estoque)

        case '3':
            buscar_produto(estoque)

        case '4':
            alterar_produto(estoque)

        case '5':
            remover_produto(estoque)

        case '6':
            print("Salvando dados antes de sair...")
            salvar_dados(estoque, ARQUIVO_DE_DADOS)
            print("Dados salvos. Até logo!")
            break
        case _:
            print("Opção inválida. Por favor, tente novamente.")