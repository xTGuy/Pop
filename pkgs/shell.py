# ----------------------------------------- #
#                    Config                 #
# ----------------------------------------- #

show_logo = True
has_motd_on = True
motd = "Hello, Boss!"
thunder_pm_beta = True

# ----------------------------------------- #
#                    Shell                  #
# ----------------------------------------- #

if has_motd_on == True:
    print(motd)
# Prompts for a input on the terminal
if show_logo == False:
    exec = input('>> ')
elif show_logo == True:
    exec = input('Pop! >> ')

# ----------------------------------------- #
#                   Imports                 #
# ----------------------------------------- #

import os

# ----------------------------------------- #
#                   Thunder                 #
# ----------------------------------------- #
if thunder_pm_beta == True:
    if exec == 'thunder':
        os.system("python3 thunder.pop")
# ----------------------------------------- #
#                   Packages                #
# ----------------------------------------- #

if exec == 'calc':
    os("python3 calculator.pop")
elif exec == 'xedit':
    os.system("python3 xedit.py")
elif exec == 'exit' or 'quit':
    quit()
elif exec == 'clear' or 'cls':
    os("clear")
    os("python3 shell.py")
elif exec == 'hw':
    os("python3 test.pop")

elif exec == 'indy':
    os("python3 shell.py")
elif exec == 'indypm':
    os("python3 indy-pm.py")


