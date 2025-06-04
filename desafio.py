print("\n💰🐍Bem-vindo ao Banco Pycash!🐍💰\n")

# menuzinho básico
menu = """
    ==============================
            MENU PRINCIPAL
    ==============================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ==============================
    
=> """

# variáveis
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

# loop para repetir até o usuário digitar 'q'
while True:
    opcao = input(menu).strip().lower()

    # aqui ficam as opções
    if opcao == "d":
        print("\n🔹 Depósito 🔹")
        depositar = float(input("Digite o valor para depositar: R$ "))

        # aqui vai confirmar se o valor é positivo
        if depositar > 0:
            saldo += depositar
            extrato += f"Depósito: R$ {depositar:.2f}\n"
            print("✅ Depósito realizado com sucesso!")
        else:
            print("❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("\n🔹 Saque 🔹")
        print("O saque tem um limite máximo diário de 3 transações, com um limite máximo de R$500 por saque.")
        saque = float(input("Digite o valor do saque: R$ "))

        saldo_excedido = saque > saldo  # confere se o saque é maior que o saldo disponível
        limite_excedido = saque > limite  # confere se o saque ultrapassa o limite de R$500
        excedeu_saques = numero_de_saques >= limite_de_saques  # verifica se o usuário já atingiu o limite de saques

        if saldo_excedido:
            print("❌ Você não possui saldo suficiente.")

        elif limite_excedido:
            print("❌ O valor do saque ultrapassa o limite diário.")

        elif excedeu_saques:
            print("❌ Você excedeu o número máximo de saques permitidos hoje.")
        
        else:
            # se o saque for permitido, ele é subtraído do saldo e registrado no extrato
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_de_saques += 1
            print("✅ Saque realizado com sucesso!")

    elif opcao == "e":
        print("\n🔹 Extrato 🔹")
        # se o extrato estiver vazio, exibe essa mensagem; senão, exibe o extrato normalmente
        print("\nNão foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\n💲 Saldo disponível: R$ {saldo:.2f}")

    elif opcao == "q":
        print("\nSaindo... Obrigado por usar o Banco Pycash!🚪\n")
        break

    else:
        print("❌ Operação inválida! Por favor, selecione uma opção válida.")
