
def depositar(saldo,valor,extrato,/):
    print("Depositar".center(20, "#"))
            
    if valor > 0:	
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")         
    else:
        print("Valor inválido")
    return saldo,extrato

def sacar(*,saldo,valor,extrato,limite_diario,numero_saques,limite_saques):
    print("Sacar".center(20, "#"))
    
    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido")
    else:       
        if valor > limite_diario:
            print("O valor ultrapassa o limite para saque")      
        elif valor > saldo:
            print("Saldo insuficiente")        
        else:  
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")  
            print(f"Voce tem {3 - numero_saques} saques restantes.")  
    return saldo,extrato,numero_saques

def exibir_extrato(saldo,/,*,extrato):
    print("Extrato".center(20, "#"))
    if extrato == "":
        print("Nenhuma movimentação realizada")
    else:
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    
def verifica_usuario(cpf,lista_usuarios):
    for usuario in lista_usuarios:
        if cpf == usuario["cpf"]:
            return True
    return False

    
def criar_usuario(lista_usuarios):
    cpf = input("Digite o CPF: ")
    
    if not verifica_usuario(cpf,lista_usuarios):
        nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento(formato -> dd/mm/aaaa): ")
        endereco = input("Digite o endereço(formato -> logradouro,numero - bairro - cidade/sigla estado): ")
        usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
        lista_usuarios.append(usuario) 
    else:
        print("Usuário já cadastrado") 
    return lista_usuarios

def criar_conta_corrente(lista_contas,lista_usuarios,numero_conta,agencia,usuario):
    
    if not verifica_usuario(usuario,lista_usuarios):
        print("Usuário não cadastrado")   
    else:
        conta_corrente = {"numero_conta": numero_conta, "agencia": agencia, "usuario": usuario}
        lista_contas.append(conta_corrente)
        print(f"Conta corrente criada com sucesso! Número da conta: {numero_conta}")
        numero_conta += 1
    return lista_contas,numero_conta

def listar_usuarios(lista_usuarios):
    if not lista_usuarios:
        print("Nenhum usuário cadastrado")
    else:
        print("Usuários cadastrados:")
        for usuario in lista_usuarios:
            print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Data de Nascimento: {usuario['data_nascimento']}, Endereço: {usuario['endereco']}")
        
def listar_contas_correntes(lista_contas):
    if not lista_contas:
        print("Nenhuma conta corrente cadastrada")
    else:
        print("Contas correntes cadastradas:")
        for conta in lista_contas:
            print(f"Conta: {conta['numero_conta']}, Agência: {conta['agencia']}, CPF usuário: {conta['usuario']}")

def main():
    saldo = 0
    limite_diario = 500
    extrato = ""
    numero_saques = 0
    numero_de_contas = 1
    
    lista_usuarios = []
    lista_contas = []
    
    LIMITE_SAQUES = 3
    NUMERO_AGENCIA = "0001"
    
    
    menu = """
    Escolha uma opcao:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuario
    [c] Criar conta corrente
    [lu] Listar usuarios
    [lc] Listar contas correntes
    [q] Sair
    => """

    print("\nBem-vindo ao Banco Richard's Finance")
    while True:

        opcao = input(menu).lower()
        
        if opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo,extrato = depositar(saldo,valor,extrato)
     
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))   
            saldo,extrato,numero_saques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite_diario=limite_diario,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
        
        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)
            
        elif opcao == "u":
            lista_usuarios = criar_usuario(lista_usuarios)
            
        elif opcao == "c":
            usuario = input("Digite o CPF do usuário: ")        
            lista_contas,numero_de_contas = criar_conta_corrente(lista_contas,lista_usuarios,numero_de_contas,NUMERO_AGENCIA,usuario)
        
        elif opcao == "lu":
            listar_usuarios(lista_usuarios)
            
        elif opcao == "lc":
            listar_contas_correntes(lista_contas)
        
        elif opcao == "q":
            print("Sair")
            print("Até logo!")
            break 

        else:
            print("Opção inválida. Tente novamente")
            
if __name__ == "__main__":
    main()