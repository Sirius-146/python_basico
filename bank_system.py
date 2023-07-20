menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Insira o valor do depósito: "))
        if valor < 0:
            print("Valor inválido")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

    elif opcao == "s":
        valor = float(input("Insira o valor a sacar: "))

        if valor > saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print("O valor é maior que seu limite")
        elif numero_saques >= LIMITE_SAQUES:
            print("O limite de saques diário foi atingido")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Retire o dinheiro no local indicado")

    elif opcao == "e":
        print("\n========= EXTRATO =========")
        print("Não foram realizadas operações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida, por favor selecione a operação desejada.")