def menu():
    menu = '''
    -------- MENU --------
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar usuário
    [5]\tCriar Conta-Corrente
    [6]\tListar contas
    [0]\tSair
    ----------------------
    => '''
    return input(menu)

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente")
    elif valor > limite:
        print("O valor é superior ao limite")
    elif numero_saques >= limite_saques:
        print("O limite de saques diário foi atingido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Retire o dinheiro no local indicado")
    else:
        print("Falha na operação")
    
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n-------- EXTRATO --------")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("----------------------")

def criar_usuario(usuarios):
    cpf = input("Insira seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("O CPF informado já está cadastrado!")
        return
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Informe seu endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--- Usuário criado com sucesso! ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Faça seu cadastro de usuário antes de abrir a conta.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Insira o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Insira o valor a sacar: "))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação Inválida, por favor selecione a operação desejada.")

main()