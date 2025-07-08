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
    print('''\n===Menu de estoque===
1. Cadastrar produto
2. Lista de produtos
3. Consultar produto por código
4. Alterar produto
5. Remover produto
6. Sair
      ''')
    try:
        escolha=int(input('Escolha uma opção para prosseguir:\n'))
        match escolha:
            case 1:
                cadastrar_produtos(estoque)
            case 2:
                lista(estoque)
            case 3:
                buscar_produto(estoque)
            case 4:
                alterar_produto(estoque)
            case 5:
                remover_produto(estoque)
            case 6:
                sair=input('Você realmente deseja sair? Digite S para sim e N para não\n').lower()
                if sair == 's':
                    print('Salvando alterações no estoque...')
                    salvar_dados(estoque, ARQUIVO_DE_DADOS)
                    print('Dados salvos. Até logo!\nPrograma finalizado')
                    break
                elif sair == 'n':
                    print('Operação cancelada.')
                else:
                    print('Opção inválida inserida, tente novamente!')
            case _:
                print("Opção inválida. Por favor, tente novamente.")
    except:
        print('Digite um número inteiro de 1 a 6 para escolher a opção.')