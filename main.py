# @@@@@ IMPORTS @@@@@@
import random

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
def designBank():
    print("\n\n")
    print(color.GREEN+"$"*53+color.END)
    print(color.GREEN+"$                                                   $"+color.END)
    print(color.GREEN+"$"+color.END+color.YELLOW+"                       PyBank                      "+color.END+color.GREEN+"$"+color.END)
    print(color.GREEN+"$                                                   $"+color.END)
    print(color.GREEN+"$"*53+color.END)
    print(color.GREEN+"$"*53+color.END)





# @@@@@  MAIN  @@@@@
designBank()
noRobot = 0
noRobot = random.randint(1000, 9999)
print("\nProve que não és um robô e informe o código de 4 dígitos\npara entrar no PyBank")
noRobotInput = int(input(f"\n{noRobot} -> "))
if noRobotInput == noRobot:
    commands = "."
    while(commands!="/sair"):

        commands = input("Informe algum comando aqui -> ")
        designBank()
        print("/criarConta")
        print("/entrar")
        print("/sair")
        commands
else:
    print("\n\nOps...\n  Você escreveu algo errado aí e não pudemos prosseguir. Tente novamente mais tarde. :)\n\n"+color.YELLOW+"PyBank"+color.END)
    exit()