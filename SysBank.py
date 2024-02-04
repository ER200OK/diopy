saldo = 500.00
limite = 500.00
saques = []
depositos = []
LIMITE_SAQUES = 3

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
    
    
def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f"Adicinado R$ {valor} em sua conta.")
        depositos.append(valor)
    else:
        print("O valor deve ser maior que R$ 0")
        
def saque(valor):
    global saldo
    valor = int(valor)
    # if saldo+limite > valor:
    if (valor > 0 and valor <= 500):
        if saldo < 0:
            print("Saldo insuficiente para realizar saque.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
            saques.append(valor)
    else:
        print("Os saques devem ser maiores que R$ 0  ou menores R$ 500")
            
def extrato():
    global saques
    global depo
    print(f"Os saques feitos foram: {saques}\n")
    print(f"Os depositos feitos foram: {depositos}\n")
    print(f"Saldo atual:{saldo}\n")
    
while True:
    
    op = input(menu)
    
    if op == "d":
        v = int(input("Insira o valor do deposito: "))
        deposito(v)
    elif op == "s":
        if LIMITE_SAQUES > 0:
            v = int(input("Insira o valor do saque: "))
            saque(v)
            LIMITE_SAQUES -= 1
        else:
            print("Limite de saques atingido!")
    elif op == "e":
        extrato()
    elif op == "q":
        break
    else:
        print("Opção invalida")
