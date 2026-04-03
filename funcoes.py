import json

arq = "banco_arquivo.json"


def linha(msg="-", quantidade=50):
    print(msg * quantidade)


def cabecalho(msg):
    linha()
    print(msg.center(50))
    linha()


def cria_banco():
    try:
        with open(arq, "r"):
            pass
        print("Banco aberto")
    except FileNotFoundError:
        with open(arq, "w") as arquivo:
            json.dump([], arquivo)
        print("Banco criado")


def leia_int(msg):
    while True:
        try:
            resposta = int(input(msg))
            return resposta
        except ValueError:
            print("Digite apenas números inteiros válidos")


def leia_float(msg):
    while True:
        try:
            resposta = float(input(msg))
            return resposta
        except ValueError:
            print("Digite apenas números.")


def menu(*funcoes):
    for i, v in enumerate(funcoes):
        print(f"{i+1} - {v}")

    while True:
        print("")
        escolha = leia_int("Digite o número da opção desejada: ")
        if 0 < escolha <= len(funcoes):
            return escolha
        else:
            print("Opção inválida")


def carega_arquivo():
    try:
        with open(arq, "r", encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
            return lista
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def salva_arquivo(lista):
    try:
        with open(arq, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo)
    except FileNotFoundError:
        print("Erro, arquivo não econtrado.")
    except Exception:
        print("Desculpe, ocorreu um erro desconhecido.")


def catastrar_produto(dicionario):
    lista = carega_arquivo()
    lista.append(dicionario.copy())
    salva_arquivo(lista)


def listar_produto():
    lista = carega_arquivo()
    return lista
