from tkinter import *

calculation = ""


def button_press(raw_input):
    global calculation
    calculation = calculation + str(raw_input)
    equation.set(calculation)


def solve():
    try:
        global calculation
        total = str(eval(calculation))
        equation.set(total)
        calculation = ""
    except:
        equation.set("ERROR")
        calculation = ""
        equation.set("")


def clear_calculator():
    global calculation
    calculation = ""
    equation.set("")


if __name__ == "__main__":
    calc_window = Tk()
    calc_window.configure(background="gray")
    calc_window.title("Calculator")
    calc_window.geometry("400x200")
    equation = StringVar()
    input_field = Entry(calc_window, textvariable=equation)
    input_field.grid(columnspan=4, ipadx=70)
    equation.set("Enter Equation")
    button1 = Button(calc_window, text=' 1 ', fg='black', bg='white',  command=lambda: button_press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(calc_window, text=' 2 ', fg='black', bg='white', command=lambda: button_press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(calc_window, text=' 3 ', fg='black', bg='white', command=lambda: button_press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(calc_window, text=' 4 ', fg='black', bg='white', command=lambda: button_press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(calc_window, text=' 5 ', fg='black', bg='white', command=lambda: button_press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(calc_window, text=' 6 ', fg='black', bg='white', command=lambda: button_press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(calc_window, text=' 7 ', fg='black', bg='white', command=lambda :button_press(7),height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(calc_window, text=' 8 ', fg='black', bg='white', command=lambda :button_press(8),height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(calc_window, text=' 9 ', fg='black', bg='white', command=lambda :button_press(9), height=1, width=7)
    button9.grid(row=4,column=2)

    button0 = Button(calc_window, text=' 0 ', fg='black', bg='white', command=lambda :button_press(0),height = 1, width = 7)
    button0.grid(row=5, column=0)

    plus = Button(calc_window, text = ' + ', fg='black', bg='white', command=lambda: button_press("+"), height = 1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(calc_window, text = ' - ', fg='black', bg='white', command=lambda :button_press("-"), height = 1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(calc_window, text=' X ', fg='black', bg='white', command=lambda :button_press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(calc_window, text=' / ', fg='black', bg='white', command=lambda: button_press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equals = Button(calc_window, text=' = ', fg='black', bg='white', command=lambda: solve(), height=1, width=7)
    equals.grid(row=5, column=2)

    clear_all = Button(calc_window, text='Clear', fg='black', bg='white', command=lambda: clear_calculator(), height=1, width=7)
    clear_all.grid(row=5, column=1)

    calc_window,mainloop()