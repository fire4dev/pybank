# @@@@@ IMPORTS @@@@@@
import random
import bd
import time

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

        sql = "INSERT INTO usuarios(fullname,cpf,email,dataNasc,passwd) VALUES(%s,%s,%s,%s,%s)"
        values = (fullname, cpf, email, dataNasc, passwd)
        bd.mysqli.execute(sql,values)
        if(bd.conexao.commit()):
            print("\n\n Sr(a). {}\n  Seu cadastro foi concluído, agora podes acessar sua conta com /entrar".format(fullname))
            time.sleep(2.5)
            concluido = 1
            bd.mysqli_close

def entrar():
    clear()
    designBank()
    print("\n          @@@@@   Entrar em sua conta   @@@@@\n\n")
    concluido = 0
    while concluido == 0:
        cpf = input("CPF ->  ")
        passwd = input("Senha ->  ")







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
        print("/sair")
        commands = input("\n\nInforme algum comando aqui -> ")
        if commands=="/abrirconta":
            abrirConta()
        if commands=="/entrar":
            entrar()

    print("\n\nVocê optou por sair.\n Até mais! :)")
else:
    print("\n\nOps...\n  Você escreveu algo errado aí e não pudemos prosseguir. Tente novamente mais tarde. :)\n\n"+color.YELLOW+"PyBank"+color.END)
    exit()
