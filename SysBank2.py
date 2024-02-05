menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cc] Criar Usuario
[ccb] Cria Conta Bancaria
[lc] Listar Contas
[lu] Listar Users
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
users = []
dic_user = {}
AGENCIA = "0001"
accounts = []
accounts_dic = {}

def deposito(valor, saldo, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito feito de R${valor:.2f} com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return(saldo, extrato)

def extrato_a(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario():
    print("Forneca as informacoes a abaixo:\n")
    c = True
    while c:
        try:
            cpf = int(input("CPF: "))
            if cpf not in dic_user:
                nome = str(input("Insira seu nome: "))
                nascimento = str(input("Insira sua data de nascimento: "))
                numero = str(input("Insira sua rua e numero: "))
                bairro = str(input("Insira o seu bairro: "))
                cidadeestado = str(input("Insira o sua cidade/sigla estado: "))
                dic_user[cpf] = {'cpf':cpf, 'nome':nome, 'nascimento':nascimento, 'numero':numero, 'bairro':bairro, 'cidadeestado':cidadeestado}
                users.append(dic_user[cpf])
                print("Cadastro feito com sucesso!")
                break
            else:
                print("CPF já cadastrado")
                pass
        except:
            print("O cpf deve ser apenas numeros!")
            pass

def cadastrar_conta_bancaria():
    print("Cadastro de conta bancaria: \n")
    cpf = int(input("CPF: "))
    num = len(accounts) + 1
    try:
        if dic_user[cpf]:
            accounts_dic[cpf] = {'agencia':AGENCIA, 'num':num, 'cpf':cpf, 'user':dic_user[cpf]['nome']}
            accounts.append(accounts_dic)
            print(f"""
Conta adicionada: 
Agencia: {AGENCIA}
Numero: {num}
CPF: {cpf}
Usuario: {dic_user[cpf]['nome']}\n""")
    except:
        print("CPF inexistente")
        
def listar_contas():
    for a in accounts_dic:
        print(f"""
Usuario: {accounts_dic[a]['user']}
CPF: {accounts_dic[a]['cpf']}
Agencia e numero: {accounts_dic[a]['agencia']}-{accounts_dic[a]['num']}
              \n""")

def listar_users():
    for user in dic_user:
        print(f"""
Nome: {dic_user[user]['nome']}
CPF: {dic_user[user]['cpf']}
Nascimento: {dic_user[user]['nascimento']}
Endereço: Endereco: {dic_user[user]['numero']} - Bairro: {dic_user[user]['bairro']} - Cidade/Estado: {dic_user[user]['cidadeestado']}
              \n""")
while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    elif opcao == "e":
        extrato_a(saldo, extrato=extrato)
    elif opcao == "cc":
        cadastrar_usuario()
    elif opcao == "ccb":
        cadastrar_conta_bancaria()
    elif opcao == "lc":
        listar_contas()
    elif opcao == "lu":
        listar_users()
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
