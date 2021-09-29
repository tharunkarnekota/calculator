from tkinter import *

mw = Tk()
mw.title('calculator')


def clear():
    display_box.delete(0, END)


def btn_click(num):
    current_num = display_box.get()  # down explained clearly
    clear()
    final_num = current_num + num
    display_box.insert(0, final_num)


first_num = 0
math = ''


def calc(mathtype):
    global first_num, math
    math = mathtype
    first_num = display_box.get()
    clear()


def equal():
    result = ''
    global first_num
    second_num = display_box.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)
    elif math == 'div':
        result = int(first_num) / int(second_num)
    display_box.insert(0, str(result))


# CREATING WIDGETS
display_box = Entry(mw, width=14, font=('arial', 28), justify=RIGHT)  # justify:display of input from which direction

btn_0 = Button(mw, text='0', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('0'))
btn_1 = Button(mw, text='1', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('1'))
btn_2 = Button(mw, text='2', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('2'))
btn_3 = Button(mw, text='3', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('3'))
btn_4 = Button(mw, text='4', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('4'))
btn_5 = Button(mw, text='5', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('5'))
btn_6 = Button(mw, text='6', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('6'))
btn_7 = Button(mw, text='7', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('7'))
btn_8 = Button(mw, text='8', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('8'))
btn_9 = Button(mw, text='9', padx=36, pady=10, font=('Arial', 14), command=lambda: btn_click('9'))

# btn_clear= Button(mw, text='clear', padx=36, pady=10, font=('Arial', 14))
btn_clear = Button(mw, text='clear', padx=74, pady=10, font=('Arial', 14), command=clear)

btn_div = Button(mw, text='/', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('div'))
btn_mul = Button(mw, text='*', padx=38, pady=10, font=('Arial', 14),
                 command=lambda: calc('mul'))  # why?38 instead of 36 :text also defines the size

btn_add = Button(mw, text='+', padx=36, pady=10, font=('Arial', 14), command=lambda: calc('add'))
btn_sub = Button(mw, text='-', padx=38, pady=10, font=('Arial', 14), command=lambda: calc('sub'))

# btn_equal= Button(mw, text='=', padx=36, pady=10, font=('Arial', 14))
btn_equal = Button(mw, text='=', padx=36, pady=40, font=('Arial', 14), command=equal)

# SHOWING WIDGETS
display_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_0.grid(row=4, column=0, padx=2, pady=2)
btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

btn_div.grid(row=5, column=1, padx=2, pady=2)
btn_mul.grid(row=5, column=0, padx=2, pady=2)

btn_add.grid(row=6, column=1, padx=2, pady=2)
btn_sub.grid(row=6, column=0, padx=2, pady=2)

btn_equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)

mw.mainloop()

# firstly display.get()=''
# then we store it in current_num,,,then curent_num=''
# by clear func we will delete '' of display then display will be cleared
# final_num=current_num+num ->suppose i enter 9(num),,, 9+''=9,,,final_num=9,
# by insert function we will display 9

# now display.get()=9
# then we store it in current_num,,,then curent_num=9
# by clear func we will delete '' of display then display will be cleared
# final_num=current_num+num ->suppose i enter 3(num),,, 9+3=93[as they are string,just merge together],,,final_num=93,
# by insert function we will display 93

#get() :
#.delete(0, END)
#.insert(0, final_num)


#clear
#button_click[0-9]        #current_num,final_num=current_num+num
#calc[+-/*]                #firstnum,math=mathtype
#equal[=]                  #second_num,first_num,#  ,result