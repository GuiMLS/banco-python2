from datetime import date
LIMITE_SAQUES = 3
saldo = 2000
contador_saques = 0
lista_saques = [0,0,0]
lista_saldos = [0,0,0]
data_antiga = 0
extrato =''
lista_usuarios = [["nome", "data_nascimento", "00000000000", "endereco"]]
lista_contas_e_usuarios = list()
lista_contas = [[0, "0001", "00000000000"]]

def funcao_saque (*, extrato, quantia, saldo, data_antiga, lista_saldos, contador_saques):
    if(quantia[0].isnumeric() and float(quantia) > 0 and float(quantia) <= 500 and contador_saques<=2):
            if (float(saldo) < float(quantia)):
                print(f"Você não tem saldo suficiente para essa transação! Seu saldo é {saldo}")
            else:
                lista_saldos[contador_saques] = saldo
                saldo-=float(quantia)
                lista_saques[contador_saques] = float(quantia)
                contador_saques+=1
                data_antiga = date.today()
                print(f"Saque de R$ {quantia} realizado com sucesso! Seu novo saldo: {saldo:.2f}")
                extrato += f"Saque: R$ {float(quantia):.2f}\n"
                return saldo, extrato, contador_saques
    elif (contador_saques>2):
            print("Você ultrapassou o limite de 3 saques diários. Volte amanhã!")
            return saldo, extrato, contador_saques
    elif (quantia.isnumeric() and float(saque) > 500):
            print("Você está solicitando um saque maior do que seu limite de R$500.00", end="\n")
            return saldo, extrato, contador_saques

def funcao_extrato (saldo, lista_saldos, lista_saques, /, *, extrato,):
    print(f"Segue seu extrato:\n{extrato}O saldo atual é de: {saldo:.2f}")
def deposito(*, saldo, quantia, extrato):
    if(quantia[0].isnumeric() and float(quantia) > 0):
        saldo+=float(quantia)
        lista_saques[contador_saques] = float(quantia)
        print(f"Depósito de R$ {quantia} realizado com sucesso! Seu novo saldo: {saldo:.2f}")
        extrato += f"Depósito: R$ {float(quantia):.2f}\n"
        return saldo, extrato

def criar_usuario(lista_usuarios, nome, data_nascimento, valor_cpf, endereco):
    for cpf in lista_usuarios:
        if valor_cpf == cpf[2]:
            print ("Usuário já cadastrado!")
            break
    if valor_cpf.find('.') == -1:
        lista_usuarios.append([nome, data_nascimento, valor_cpf, endereco])
        print(f"Usuário {nome} cadastrado com sucesso!")
    else:
        cpf_corrigido = valor_cpf.replace(".", "")
        lista_usuarios.append([nome, data_nascimento, cpf_corrigido, endereco])
        print(f"Usuário {nome} cadastrado com sucesso!")

def criar_conta(lista_contas, lista_usuarios, lista_contas_e_usuarios, valor_cpf):
    indice = int(lista_contas[-1][0]) + 1
    agencia = "0001"
    for cpf in lista_usuarios:
        print(f"Estou tentando comparar {valor_cpf} com {cpf[2]}")
        if valor_cpf == cpf[2]: #Se o usuario existir
            nome_usuario=cpf[0]
            data_nascimento_usuario=cpf[1]
            endereco_usuario=cpf[3]
            lista_contas.append([indice, agencia, valor_cpf])
            lista_contas_e_usuarios.append([nome_usuario, data_nascimento_usuario, endereco_usuario, indice])
            print (f"Conta {indice} criada com sucesso na agencia {agencia}!")
            break
    else: #Se o usuario nao existir
        print(f"Usuario com CPF {valor_cpf} nao cadastrado! Favor cadastrar primeiro!")

def listar_contas(lista_contas):
     print(lista_contas)
     print(lista_usuarios)

def sair():
     print("Obrigado pela preferência! Caixa encerrado.")
     

while(1):
    print("Bem vindo ao banco do Guilherme! Escolha uma opção:\n[1] Sacar\n[2] Consultar Saldo\n[3] Depósito\n[4] Criar Usuário\n[5] Criar Conta\n[6] Listar Contas\n[7] Sair")
    opcao=input()
    data_hoje = date.today()
    if (data_antiga == 0):
         data_antiga = date.today()
    if (data_hoje != data_antiga):
        contador_saques = 0
    
    if (opcao == "1"):
        print("Digite a quantia que você quer sacar ou digite x se você quer retornar ao menu inicial:\n")
        saque = input()
        (saldo, extrato, contador_saques) = funcao_saque(quantia=saque, saldo=saldo, data_antiga=data_antiga, lista_saldos=lista_saldos, contador_saques=contador_saques, extrato=extrato)
        #print(f"Extrato: {extrato} Saldo: {saldo}")
    
    if (opcao == "2"):
        funcao_extrato(saldo, lista_saldos, lista_saques, extrato=extrato)
    
    elif (opcao == "3"):
        print("Digite a quantia que você quer depositar ou digite x se você quer retornar ao menu inicial:\n")
        valor = input()
        (saldo, extrato) = deposito(saldo=saldo, quantia=valor, extrato=extrato)
    
    elif (opcao == "4"):
        nome = input("Digite seu Nome Completo:\n")
        data_nascimento = input("Digite sua data de nascimento:\n")
        cpf = input("Digite seu CPF SEM PONTO:\n")
        endereco = input("Digite seu endereço:\n")
        criar_usuario(lista_usuarios, nome, data_nascimento, cpf, endereco)

    elif (opcao == "5"):
        cpf=input("Para criar a conta, digite o Numero do seu cpf:\n")
        criar_conta(lista_contas, lista_usuarios, lista_contas_e_usuarios, cpf)

    elif (opcao == "6"):
        listar_contas(lista_contas)
    
    elif (opcao == "7"):
        sair()
        break