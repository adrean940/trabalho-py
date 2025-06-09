import os

ARQUIVO_CONTATOS = "contatos.txt"
SENHA_ACESSO = "proz@2025"

def autenticar():
    senha = input("Digite a senha de acesso: ")
    if senha != SENHA_ACESSO:
        print(" Senha incorreta. Encerrando o sistema.")
        exit()
    print(" Acesso permitido!")

def menu():
    print("\n MENU DE OPÇÕES")
    print("1 - Inserir novo contato")
    print("2 - Listar contatos")
    print("3 - Excluir contato")
    print("X - Encerrar o sistema")

def inserir_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cidade = input("Cidade: ")

    with open(ARQUIVO_CONTATOS, "a", encoding="utf-8") as f:
        f.write(f"{nome};{telefone};{email};{cidade}\n")

    print(" Contato adicionado com sucesso.")

def listar_contatos():
    if not os.path.exists(ARQUIVO_CONTATOS):
        print(" Nenhum contato encontrado.")
        return

    print("\n LISTA DE CONTATOS:")
    with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as f:
        for i, linha in enumerate(f, start=1):
            nome, telefone, email, cidade = linha.strip().split(";")
            print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}, Cidade: {cidade}")

def excluir_contato():
    listar_contatos()

    if not os.path.exists(ARQUIVO_CONTATOS):
        return

    try:
        indice = int(input("Digite o número do contato a ser excluído: "))
        with open(ARQUIVO_CONTATOS, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        if 1 <= indice <= len(linhas):
            del linhas[indice - 1]
            with open(ARQUIVO_CONTATOS, "w", encoding="utf-8") as f:
                f.writelines(linhas)
            print(" Contato excluído com sucesso.")
        else:
            print(" Número inválido.")
    except ValueError:
        print(" Entrada inválida.")

def main():
    autenticar()
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip().upper()
        if opcao == "1":
            inserir_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            excluir_contato()
        elif opcao == "X":
            print(" Encerrando o sistema. Até logo!")
            break
        else:
            print(" Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
