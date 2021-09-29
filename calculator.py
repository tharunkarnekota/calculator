#justify

from tkinter import *

mw = Tk()
mw.title('calculator')

#CREATING WIDGETS
db = Entry(mw, width=14, font=('arial',28), justify=RIGHT)          #justify:display of input from which direction

#SHOWING WIDGETS
db.grid(row=0, column=0,padx=10,pady=10)

mw.mainloop()