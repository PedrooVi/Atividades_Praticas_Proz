saldo = 1000
opcao = int(input("INFORME A OPÇÃO DESEJADA! "))

if opcao == 1 :
    saque = float(input("DIGITE O VALOR DO SAQUE: "))
    while saque > saldo:
         print(" SALDO NEGADO SALDO INSUFICIENTE!  ")
         saque = float(input("DIGITE O VALOR DO SAQUE: "))
    saldo -= saque
    print("SEU SAQUE FOI REALIZADO SEU SALDO ATUAL É DE ", saldo)
elif opcao == 2:
    deposito = float(input("INFORME O VALOR DO DEPOSITO: "))
    saldo += deposito
    print ("DEPOSITO REALIZADO SEU SALDO ATUAL É:", saldo)
elif opcao == 3: 
    print ("SEU SALDO É", saldo)
else: 
    print("OPCAO INVALIDA! ")