# @@@@@ IMPORTS @@@@@@
import random
import bd
import time
from datetime import datetime

# @@@@@ CLASS @@@@@
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# @@@@@ FUNCTIONS @@@@@

def clear():
    print("\n"*100)

def designBank():
    print("\n\n")
    print(color.GREEN+"$"*53+color.END)
    print(color.GREEN+"$                                                   $"+color.END)
    print(color.GREEN+"$"+color.END+color.YELLOW+"                       PyBank                      "+color.END+color.GREEN+"$"+color.END)
    print(color.GREEN+"$                                                   $"+color.END)
    print(color.GREEN+"$"*53+color.END)
    print(color.GREEN+"$"*53+color.END)


def abrirConta():
    clear()
    designBank()
    print("\n          @@@@@   Abrir Conta   @@@@@\n\n")
    concluido = 0
    logado = 0
    while concluido == 0:
        fullname = input("Nome completo ->  ")
        cpf = input("CPF ->  ")
        # valida o cpf
        if(len(cpf)<11 or len(cpf)>11):
            print("\n\nErro: o cpf deve ter 11 digitos e você digitou {}\n".format(len(cpf)))
            continue
        email = input("E-mail ->  ")
        verificaEmail = (email.find('@'),email.find('.com'))
        if verificaEmail[0] == -1:
            print("\n\nErro: email inválido [missing: '@']\n")
            continue
        if verificaEmail[1] == -1:
            print("\n\nErro: email inválido [missing: '.com/.com.br/...']\n")
            continue
        dataNasc = input("Data de nasc. [dd/mm/yyyy] ->  ")
        # valida a data de nascimento
        if(len(dataNasc)<10 or len(dataNasc)>10):
            print("\n\nErro: data de nascimento inválida\n")
            continue
        passwd = input("Senha ->  ")
        if(len(passwd)<6):
            print("\n\nErro: a senha deve conter pelo menos 6 digitos\n")
            continue

        #verificar se existe
        bd.cursor.execute("SELECT cpf FROM usuarios WHERE cpf=%s;",(cpf,))
        rowCount = bd.cursor.rowcount
        if(rowCount==0):
            moneyInit = 0
            bd.cursor.execute("INSERT INTO usuarios(fullname,cpf,email,datanasc,passwd) VALUES(%s,%s,%s,%s,%s)",(fullname, cpf, email, dataNasc, passwd))
            bd.cursor.execute("INSERT INTO saldos(cpf,saldo) VALUES(%s,%s)",(cpf,moneyInit))
            bd.connection.commit()
            print("\n\n Sr(a). {}\n  Seu cadastro foi concluído, agora podes acessar sua conta com /entrar".format(fullname))
            time.sleep(2.5)
            concluido = 1
        else:
            print("\n\nSr(a). {}, o CPF digitado ({}) já foi usado aqui no PyBank.\n\n".format(fullname,cpf))
            time.sleep(2.5)
            continue

            
            

def entrar():
    clear()
    designBank()
    print("\n          @@@@@   Entrar em sua conta   @@@@@\n\n")
    concluido = 0
    while concluido == 0:
        cpf = input("CPF ->  ")
        if(len(cpf)<11 or len(cpf)>11):
            print("\n\nErro: o cpf deve ter 11 digitos e você digitou {}\n".format(len(cpf)))
            continue
        passwd = input("Senha ->  ")
        # @@ pegar dados do banco
        bd.cursor.execute("SELECT cpf, passwd FROM usuarios WHERE cpf=%s and passwd=%s;",(cpf,passwd))
        rowCount = bd.cursor.rowcount
        # @@ verificar se o login está certo
        if (rowCount == 1):
            concluido = 1
            logado = 1
            while logado==1:
                clear()
                designBank()
                userLogado(cpf)
                commands = input("\n\nInforme algum comando aqui -> ")
                exitBank(commands)
                # @@ verificações
                if commands == "/sairconta":
                    print("\nVocê foi desconectado!")
                    time.sleep(2.5)
                    logado = 0
                if commands == "/minhaconta":
                    clear()
                    designBank()
                    myacc(cpf)
                    commands = input("\n\nInforme algum comando aqui -> ")
                    exitBank(commands)
                    if commands == "/voltar":
                        continue
                if commands == "/meusaldo":
                    clear()
                    designBank()
                    myMoney(cpf)
                    commands = input("\n\nInforme algum comando aqui -> ")
                    exitBank(commands)
                    if commands == "/voltar":
                        continue
                if commands == "/transferir":
                    clear()
                    designBank()
                    transferir(cpf)
                    commands = input("\n\nInforme algum comando aqui -> ")
                    exitBank(commands)
                    if commands == "/voltar":
                        continue
                if commands == "/pagar":
                    clear()
                    designBank()
                    pagar(cpf)
                    commands = input("\n\nInforme algum comando aqui -> ")
                    exitBank(commands)
                    if commands == "/voltar":
                        continue
                if commands == "/pagamentos":
                    clear()
                    designBank()
                    pagamentos(cpf)
                    commands = input("\n\nInforme algum comando aqui -> ")
                    exitBank(commands)
                    if commands == "/voltar":
                        continue
                
        else:
            print("\n\n Não existe nenhum cadastro com o CPF ou Senha especificado, por favor\nverifique se você digitou certo ou abra sua\nconta com o comando /abrirconta")
            time.sleep(2.5)
            concluido = 1

def userLogado(cpfDigitado):
    # @@ pegar o nome no bd
    bd.cursor.execute("SELECT fullname FROM usuarios WHERE cpf=%s;",(cpfDigitado,))
    nome = bd.cursor.fetchone()[0]
    print("\nBem vindo ao PyBank, {}!".format(nome))
    print("\n/minhaconta")
    print("/meusaldo")
    print("/transferir")
    print("/pagar")
    print("/pagamentos")
    print("\n/sairconta")
    print("/sair")

def myacc(cpfDigitado):
    bd.cursor.execute("SELECT * FROM usuarios WHERE cpf=%s",(cpfDigitado,))
    dados = bd.cursor.fetchall()
    print("\nSeus dados:\n")
    for rows in dados:
        print("Nome ->  {}".format(rows[1]))
        print("E-mail ->  {}".format(rows[3]))
        print("CPF ->  {}".format(rows[2]))
        print("Senha ->  {}".format(rows[5]))
        print("Data de nascimento [yyyy-mm-dd] ->  {}".format(rows[4]))
    print("\n/voltar")

def myMoney(cpfDigitado):
    bd.cursor.execute("SELECT saldo FROM saldos WHERE cpf=%s",(cpfDigitado,))
    dados = bd.cursor.fetchone()
    print("\nSeu saldo:")
    print("R${:.2f}".format(dados[0]))
    print("\n/voltar")

def transferir(cpfDigitado):
    concluido = 0
    while concluido == 0:
        bd.cursor.execute("SELECT saldo FROM saldos WHERE cpf=%s",(cpfDigitado,))
        saldo = bd.cursor.fetchone()[0]
        dateNow = ""
        if saldo>0:
            cpfTransf = input("\nInforme o CPF do usuário ->  ")
            if cpfTransf!=cpfDigitado:
                bd.cursor.execute("SELECT cpf FROM usuarios WHERE cpf=%s",(cpfTransf,))
                rows = bd.cursor.rowcount
                if rows>0:
                    value = float(input("Valor ->  R$"))
                    if value <= saldo:
                        dateNow = datetime.today().strftime('%Y-%m-%d')
                        # @@ pegando a foreign key e adicionando em outra tabela
                        bd.cursor.execute("SELECT userID FROM usuarios WHERE cpf=%s",(cpfDigitado,))
                        userID = bd.cursor.fetchall()[0]
                        bd.cursor.execute("INSERT INTO transferencias(userID,cpf,cpfTransf,valor,dataTransf) VALUES(%s,%s,%s,%s,%s)", (userID,cpfDigitado,cpfTransf,value,dateNow))
                        bd.connection.commit()
                        bd.cursor.execute("UPDATE saldos SET saldo=saldo+%s WHERE cpf=%s",(value,cpfTransf))
                        bd.cursor.execute("UPDATE saldos SET saldo=saldo-%s WHERE cpf=%s",(value,cpfDigitado))
                        bd.connection.commit()
                        print("\n Transferência efetuada com sucesso!")
                        print("\n/voltar")
                        time.sleep(2.5)
                        concluido=1
                    else:
                        print("\nSaldo insuficiente...")
                        time.sleep(3)
                        concluido=1
                else:
                    print("\nO usuário informado não existe")
                    time.sleep(3)
                    concluido=1
            else:
                print("\n Oops...\nVocê não pode transferir para você mesmo! :)")
                continue
        else:
            print("\n Você ainda não tem saldo, deposite em sua conta\nno menu inicial com /depositar")
            print("\n/voltar")
            commands = input("\n\nInforme algum comando aqui -> ")
            exitBank(commands)
            if commands == "/voltar":
                exit()
            
    

def pagar(cpfDigitado):
    concluido = 0
    situacao = ""
    dateNow = ""
    while concluido == 0:
        bd.cursor.execute("SELECT saldo FROM saldos WHERE cpf=%s",(cpfDigitado,))
        saldo = bd.cursor.fetchone()[0]
        if saldo>0:
            nomePag = input("\nNome do pagamento ->  ")
            codBarras = int(input("Código de barras ->  "))
            value = float(input("Valor ->  R$"))           
            if value <= saldo:
                situacao = "pendente"
                dateNow = datetime.today().strftime('%Y-%m-%d')
                # @@ pegando a foreign key e adicionando em outra tabela
                bd.cursor.execute("SELECT userID FROM usuarios WHERE cpf=%s",(cpfDigitado,))
                userID = bd.cursor.fetchall()[0]
                bd.cursor.execute("INSERT INTO pagamentos(userID,nomePag,cpf,codBarras,valor,dataPag,situacao) VALUES(%s,%s,%s,%s,%s,%s,%s)", (userID,nomePag,cpfDigitado,codBarras,value,dateNow,situacao))
                bd.connection.commit()
                load = 0
                seg = 59
                mins = 1
                while load<120:
                    clear()
                    designBank()
                    print("\n Aguarde...\nSeu pagamento está sendo processado e será atualizado em alguns minutos.")
                    if seg<10:
                        print(" {}:0{}".format(mins,seg))
                    else:
                        print(" {}:{}".format(mins,seg))
                    time.sleep(1)                   
                    if seg == 0:
                        mins-=1
                        seg=59
                    seg-=1
                    if (mins==0) and (seg==0):
                        break
                    load+=1
                    
                situacao = "pago"
                bd.cursor.execute("UPDATE saldos SET saldo=saldo-%s WHERE cpf=%s",(value,cpfDigitado))
                bd.cursor.execute("UPDATE pagamentos SET situacao=%s WHERE cpf=%s",(situacao,cpfDigitado))
                bd.connection.commit()
                print("\n Pagamento realizado com sucesso!")
                print("\n/voltar")
                time.sleep(3)
                concluido=1
            else:
                print("\nSaldo insuficiente...")
                time.sleep(2.5)
                continue
        else:
            print("\n Você ainda não tem saldo, deposite em sua conta\nno menu inicial com /depositar")
            print("\n/voltar")
            commands = input("\n\nInforme algum comando aqui -> ")
            exitBank(commands)
            if commands == "/voltar":
                exit()

def pagamentos(cpfDigitado):
    bd.cursor.execute("SELECT * FROM pagamentos WHERE cpf=%s",(cpfDigitado,))
    rows = bd.cursor.fetchall()
    numRows = bd.cursor.rowcount
    if numRows>0:
        print("\n    Histórico de Pagamentos:\n")
        cont=0
        for dados in rows:
            cont+=1
            print("{} ->   NOME: {}    CÓD.BARRAS: {}    VALOR: R${}    DATA: {}    SITUAÇÃO: {}".format(cont,dados[2],dados[4],dados[5],dados[6],dados[7]))
        print("\n/voltar")
    else:
        print("\nNenhum pagamento foi efetuado")
        print("\n/voltar")

def exitBank(commandWrited):
    if commandWrited == "/sair":
        print("\n\nVocê optou por sair.\n Até mais! :)")
        exit()

def deposit():
    concluido=0
    while concluido==0:
        clear()
        designBank()
        name = input("\nInforme seu nome ->  ")
        # @@ cpf do depositante
        cpf = input("Informe seu CPF ->  ")
        if(len(cpf)<11 or len(cpf)>11):
            print("\n\nErro: o cpf deve ter 11 digitos e você digitou {}\n".format(len(cpf)))
            continue
            
        # @@ cpf para quem quer depositar        
        cpfDeposit = input("CPF da pessoa para quem quer depositar ->  ")
        if(len(cpf)<11 or len(cpf)>11):
            print("\n\nErro: o cpf deve ter 11 digitos e você digitou {}\n".format(len(cpf)))
            continue

        # @@ verificar se o usuario existe
        bd.cursor.execute("SELECT cpf FROM usuarios WHERE cpf=%s",(cpfDeposit,))
        rows = bd.cursor.rowcount
        if rows > 0:
            value = float(input("Valor ->  R$"))
            bd.cursor.execute("INSERT INTO depositos(nome,cpf,cpfDeposit,valor) VALUES(%s,%s,%s,%s)", (name,cpf,cpfDeposit,value))
            bd.connection.commit()
            bd.cursor.execute("UPDATE saldos SET saldo=saldo+%s WHERE cpf=%s",(value,cpfDeposit))
            bd.connection.commit()
            print("\n Depósito efetuado com sucesso!")
            time.sleep(2.5)
            concluido=1
        else:
            print("\nO usuário informado não existe")
            time.sleep(2.5)
            continue
    



# @@@@@  MAIN  @@@@@
designBank()
noRobot = 0
noRobot = random.randint(1000, 9999)
print("\nProve que não és um robô e informe o código de 4 dígitos\npara entrar no PyBank")
noRobotInput = int(input("\n{} -> ".format(noRobot)))
if noRobotInput == noRobot:
    commands = "."
    while(commands!="/sair"):
        clear()
        designBank()
        print("\n/abrirconta")
        print("/entrar")
        print("/depositar")
        print("/sair")
        commands = input("\n\nInforme algum comando aqui -> ")
        if commands=="/abrirconta":
            abrirConta()
        if commands=="/entrar":
            entrar()
        if commands=="/depositar":
            deposit()

    print("\n\nVocê optou por sair.\n Até mais! :)")
else:
    print("\n\nOps...\n  Você escreveu algo errado aí e não pudemos prosseguir. Tente novamente mais tarde. :)\n\n"+color.YELLOW+"PyBank"+color.END)
    exit()
