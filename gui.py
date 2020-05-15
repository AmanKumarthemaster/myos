from tkinter import*
def cmd():
    exec(open("cmd.py").read())


root=Tk()
welcome=Label(root,text="Welcome to Dragon os.")
welcome.pack()
cmdB=Button(root,text="Hello", command=cmd)
cmdB.pack()
root.mainloop()