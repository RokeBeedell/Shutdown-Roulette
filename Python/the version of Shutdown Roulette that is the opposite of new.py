# The code that is below this descriptor imports the modules that are necessary to perform the functions that this script performs.
from tkinter import * # This should import all of Tkinter's library/libraries (although it doesn't, as if evident when "from tkinter import ttk" is converted to a comment) but it does not. However, it likesly imports too much regardless, so this should be rectified.
from tkinter import ttk
from subprocess import call
import random

# The code that is for "Window_1":
def startclick():
    call(['python', 'start.py'])
def Abort_1():
    call(['python', 'abort.py'])

Output_result_1 = ''    
Main_number_1 = random.randint(0,100)
Window_1 = Tk()
Window_1.title('Shutdown Roulette')

Button_1 = ttk.Button(text = 'Start',
                            command = lambda : (startclick(), ClearBox()))
Button_1.grid(column = 0, row = 0)

Button_2 = ttk.Button(text = 'Abort',
                            command = lambda : (Abort_1()))
Button_2.grid(column = 0, row = 2)

Entry_1 = ttk.Spinbox(increment = 1, from_ = 0, to = 100, wrap = True)
Entry_1.grid(column = 1, row = 2)
#Entry_1.focus()# This focuses the entry box when the window is launched.

def submit(): 
    string_guess = Entry_1.get()
    int_guess = int(string_guess)
    Entry_1.focus()

#   "Breakpoint": below is the code that calculates whether the answer that has been provided by the player is correct.
    if int_guess == Main_number_1:
        print('Correct!')
        output = Label(Window_1, text = 'Correct! 🙂')
        output.grid(column = 0, row = 10)
        call(['python', 'abort.py'])
    if int_guess != Main_number_1:
        print('Incorrect.')
        output = Label(Window_1, text = 'Incorrect… 🙁')
        output.grid(column = 0, row = 10)

# "Breakpoint": below is the code that clears and submits the guess.
def clearbox():
    Entry_1.delete(first = 0,last = 22)
        
Button_3 = ttk.Button(text = '                Submit               ',# The space that this button occupies should be determined by a better means than this.
                            command = lambda : (submit(), clearbox()))
Button_3.grid(column = 1, row = 0)

Window_1.mainloop()




