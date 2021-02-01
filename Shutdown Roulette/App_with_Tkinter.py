from tkinter import *
import os
from subprocess import call
import random

#InfoWindow Code
def moveon():
    infowindow.destroy()

#infowindow = Tk()
#infowindow.title("Le Shutdown Roulette Info Panel")
#infowindow.geometry("340x150")
#infowindow.configure(background="black")
#infotxt1 = Label(infowindow, fg="white", bg="black", text="""Welcome to the Shutdown Roulette.
#In here,""")
#infotxt1.grid(row=1, column=1)
#movebutton = Button(infowindow, fg="white", bg="black", text="Ok", command=moveon)
#movebutton.grid(row=5, column=5)

#infowindow.mainloop()

#MainWindow Code

def startclick():
    call(["python", "start.py"])

def abort():
    call(["python", "abort.py"])

outputresult123 = ""    
mainnumber = random.randint(0,60)
window = Tk()
window.title("Le Shutdown Roulette")
window.geometry("340x150")
window.configure(background="black")
lbl = Label(window, fg="white", bg="black", text="Welcome to the shutdown roulette!\nWhen your ready to go, click start!")
lbl.grid(column=0, row=0, padx=10, pady=20)
btn = Button(window, fg="white", bg="black", text="start", activeforeground="blue", activebackground="yellow", command=startclick)
btn.grid(column=1, row=0, padx=1, pady=1)
abort = Button(window, fg="white", bg="black", text="abort", activeforeground="blue", activebackground="yellow", command=abort)
abort.grid(column=0, row=10, padx=1, pady=1)
input_entry = Entry(window,width=5, fg="white", bg="black")
input_entry.grid(column=0, row=9, padx=5, pady=5)
input_entry.focus()
Logo = Label(window, fg="white", bg="black", text ="Le shutdown roulette\n| By Leo Tovell |")
Logo.grid(column=1, row = 10, padx=5, pady=5)
def submit():
    
    string_guess = input_entry.get()
    int_guess = int(string_guess)
    input_entry.focus()

#Breakpoint - Below is the Code for calucalting if your correct or not.

    if int_guess == mainnumber:
        print("Correct!")
        output = Label(window, text = "Correct! :)")
        output.grid(column=0, row=10, padx=10, pady=10)
        call(["python", "abort.py"])
    if int_guess != mainnumber:
        print("Incorrect")
        output = Label(window, text = "Incorrect:(")
        output.grid(column=0, row=10, padx=10, pady=10)
#    if int_guess < mainnumber:
#        print("Incorrect")
#        output = Label(window, text = "Incorrect:(")
#        output.grid(column=0, row=11, padx=10, pady=10)

#Breakpoint - Above is the Code for calucalting if your correct or not.
#Breakpoint - Below is the Code for clearing and submitting the guess

def clearbox():
    input_entry.delete(first=0,last=22)
        
sub = Button(window, text="submit", command=lambda:[submit(), clearbox()])
sub.grid(column=1, row=9, padx=10, pady=1)



window.mainloop()




