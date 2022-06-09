from tkinter import*
from tkinter.ttk import*

from time import strftime
root=Tk()
root.title("CLOCK")
def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)
    
label=Label(root, font=("Helvetica",80,'bold'), background="black", foreground="yellow")
label.pack(anchor='center')
time()
mainloop()
