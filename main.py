
mode=input("1.for command line 2.for gui:")
if mode=="1":
    exec(open("cmd.py").read())
elif mode=="2":
    exec(open("gui.py").read())