import subprocess
import getpass
print("welcome to the command line interface of dragon os.")
userl=['aman']
userp={'aman':'bara'}
while True:
    user=input("name of the current user:")
    if user in userl:
        passw=getpass.getpass(prompt="Enter your password:")
        threalpass=userp[user]
        if passw==threalpass:
            print("hello",user)
            while True:
                command=input("dragon>")
                if command=="exit":
                    exit()
                elif command=="clear" or command=="cls":
                    subprocess.call("cls",shell=True)
                elif command=="echo":
                    printv=input("What to print:")
                    print(printv)
                elif command=="input":
                    promptask=input("Give the prompt.")
                    variableask=input("Do you want to store it in a var ?:")
                    if variableask=="yes":
                        varname=input("Give the name of the variable-")
                        varn=varname
                        varn=input(promptask)
                        value=input("what do you want to do with that variable ? 1 for print 2.for eliminate 3.for add some more text into it .")
                        if value=="1":
                            print(varn)
                        elif value=="2":
                            print('ok')
                        elif value=="3":
                            somemt=input("What is the text you want to add?:")
                            print(somemt,varn)
    else:
        register=input("no user like that. Type newuser for adding a user.")
        if register=="newuser":
            nuser=input("Enter the username:")
            npass=getpass.getpass(prompt="enter the password:")
            userl.append(nuser)
            userp[nuser]=npass


