# The code for changing pages was derived from: "//stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter".
# License: "//creativecommons.org/licenses/by-sa/3.0/".

# The code that is below this descriptor imports the modules that are necessary to perform the functions that this script performs.
import tkinter as tk # Remove "as tk" when all of the code that consitutes this script is functional, then replace all instances of "tk" with "Tkinter" or, is that does not work, "tkinter".
from tkinter import ttk
from subprocess import call
import random

class Window_1(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Shutdown Roulette")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne): # This code does not function when less than two frames are parsed as its parameters/arguments (which?).

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(sticky="nw")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(ttk.Frame):

    def startclick():
        call(['python', 'Start.py'])
        
    def Abort_1():
        call(['python', 'abort.py'])

    def submit(): 
        String_guess_1 = Entry_1.get()
        int_guess = int(String_guess_1)
        Entry_1.focus()

        # "Breakpoint": the code that is below this descriptor calculates whether the answer that has been provided by the player is correct.
        if int_guess == Main_number_1:
            print('Correct!')
            output = Label(Window_1, text = 'Correct! 🙂')
            output.pack()
            call(['python', 'abort.py'])
            
        if int_guess != Main_number_1:
            print('Incorrect.')
            output = Label(Window_1, text = 'Incorrect… 🙁')
            output.pack()

    # "Breakpoint": the code that is below this descriptor and submits the guess and subsequently clears the input box.
    def ClearBox():
        Entry_1.delete(first = 0,last = 22)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
#       Header_1 = ("Segoe_Historic", 12) # Segoe Historic is better than all fonts that constitute the font family that is called "Segoe" that are not Segoe Historic! (Although unlike Segoe Mono, it is not monospaced.)
        Header_1 = (12) # However, all text should respect the system font, as the user/player's operating system may not use a font that is a constituent of the font family that is called "Segoe", which would make the visual appearance of the title seem strange.
        Label1 = ttk.Label(self, text = "Shutdown Roulette", font = Header_1)
        Label1.pack(pady=10,padx=10)

        Button_1 = ttk.Button(self, text = 'Start',
                            command = lambda : call(['python', 'Start.py']))
        Button_1.pack()

        Button_2 = ttk.Button(self, text = 'Submit',
                            command = lambda : (submit(), ClearBox()))
        Button_2.pack()

        Entry_1 = ttk.Spinbox(self, increment = 1, from_ = 0, to = 100, wrap = True)
        Entry_1.pack()

        Button_3 = ttk.Button(self, text='Abort',
                            command = lambda : call(['python', 'abort.py']))
        Button_3.pack()

class PageOne(ttk.Frame): # This exists merely because I do not know how to create only one frame and have it display as the "for F in [...]" code requires more than one frame, or better yet, remove all frames so that I can remove the unnecessary graphical computation and smallen the size of the script.

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

Application_1 = Window_1()
Application_1.mainloop()

