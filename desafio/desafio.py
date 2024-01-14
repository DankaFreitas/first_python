menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operacao falhou! o valor informado é invalido.")
    
    elif opcao == "s":
        valor = float(input("digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES


        if excedeu_saldo:
            print("Operacao falhou! Você não tem saldo sulficiente.")

        elif excedeu_limite:
            print("Operacao falhou!O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operacao falhou! Numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operacao falhou! O valor informado é inválido.")    

    elif opcao == "e":
        print("\n==================EXTRATO===================")
        print("Não foram realizadas movimentacoes." if not extrato  else extrato)
        print(f"\nExtrato R$ {saldo:.2f}")
        print("\n============================================")

    elif opcao == "q":
        break

    else:
        print("Operacao inválida, por favor selecione novamente a operacão desejada")