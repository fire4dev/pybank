# @@@@@ IMPORTS @@@@@@
import random
import psycopg2
import bd

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
        usuarioUP = input("CPF ->  ")
        senhaUP = input("Senha ->  ")


def entrar():
    clear()
    designBank()
    print("\n          @@@@@   Entrar em sua conta   @@@@@\n\n")
    concluido = 0
    while concluido == 0:
        usuarioIN = input("CPF ->  ")
        senhaIN = input("Senha ->  ")


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
