#Modelo de banco basicoD


menu = """
[D] Depositar
[S] Sacar 
[E] Extrato 
[Q] Sair 

=> """

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES  = 3

while True:
    opção = input(menu)

    if opção == "D":
        valor = float(input("Valor do deposito:"))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Valor depositado.")
        else:
            print("OPERAÇÃO FALHOU! VALOR INVALIDO!!")


    elif opção == "S":
        valor = float(input("Valor para saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, sem saldo suficiente")
        elif excedeu_limite:
            print("Operação falhou, valor do saque excedeu o limite")
        elif excedeu_saques:
            print("Operação falhou, numero de saques excedido")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R${valor:.2f}\n"
            numero_saques += 1
            print("Valor sacado.")
        else:
            print("Operação falhou, valor invalido")     


    elif opção == "E":
        print("\n -------------------- EXTRATO -----------------")
        print("não foram realizados movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("--------------------------------------------------")
    elif opção == "Q":
        break
    else:
        print("Operação invalida, por favor selecione novamente.")