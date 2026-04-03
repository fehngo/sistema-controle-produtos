from time import sleep
import funcoes

funcoes.cria_banco()
while True:
    funcoes.cabecalho("Sistema de Controle de Estoque")
    resposta = funcoes.menu(
        "Cadastrar Produto", "Listar Produtos", "Atualizar Produto", "Excluir Produto"
    )

    if resposta == 1:
        funcoes.cabecalho("Cadastro de Produtos")
        dicionario = dict()
        dicionario["nome"] = input("Digite o nome do produto: ").strip().capitalize()
        dicionario["preco"] = funcoes.leia_float("Digite o preço do produto: ")
        dicionario["quantidade"] = funcoes.leia_int(
            f"Digite a quantidade de {dicionario['nome']} em estoque: "
        )
        funcoes.catastrar_produto(dicionario)
        sleep(2)

    if resposta == 2:
        funcoes.cabecalho("Lista de Produtos")
        lista = funcoes.listar_produto()
        print(f'{"ind":^5}|{"Produto":^19}|{"Preço":^12}|{"Quantidade":^12}')
        for i, v in enumerate(lista):
            print(f"{i+1:^6}{v['nome']:<19} {f"R$: {v['preco']:.2f}":^11} {v['quantidade']:^13}")
        print("")
        sleep(2)
