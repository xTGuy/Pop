##################################
##            Shell             ##
##################################
exec = input('>> ')

##################################
##           Imports            ##
##################################

import os

##################################
##       Package Template       ##
##################################

# This is a Pre-Installed template for your creations. If you want to make a creation, please go to /pkgs/make/make.txt.

if exec == 'test':
    os.system("python3 test.pop")

##################################
##        System Packages       ##
##################################

if exec == 'exit' or "quit":
    quit()
if exec == 'help':
    print("Pop! v1.0 Does not have this command. Coming soon.")
    os.system("python3 indy.py")


##################################
##           Packages           ##
##################################
