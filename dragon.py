print("welcome to dragon os.")

print("Type help if you want to know the commands or just write cont")
comm=input("")
if comm=="help":
        print("1.echo for print")
        print("2.help for printing help.")
        print("3.clear for clearing the screen.")
        print("4.for making a new file.")
elif(comm=="cont"):
        exec(open("main.py").read())
else:
    
        print("wrong input")

    
