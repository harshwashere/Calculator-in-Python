import tkinter as tk

calculate = ''

def calculation(symbol):
    global calculate
    calculate += str(symbol)
    result.delete(1.0, "end")
    result.insert(1.0, calculate)
    
def evaluate():
    global calculate
    try:
        calculate = str(eval(calculate))
        result.delete(1.0, "end")
        result.insert(1.0, calculate)
    except:
        clear()
        result.insert(1.0, "Undefined")

def clear():
    global calculate
    calculate = ""
    result.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator in Python")
root.geometry("320x300")

result = tk.Text(root, height=2, width=24, font=('Arial', 18))
result.grid(columnspan=5, padx=3, pady=3)

btnClear = tk.Button(root, text='C', command=clear, width=5, font=("Arial", 18))
btnClear.grid(row=2, column=1)

btnDivide = tk.Button(root, text='/', command=lambda: calculation("/"), width=5, font=("Arial", 18))
btnDivide.grid(row=2, column=4)

btn7 = tk.Button(root, text='7', command=lambda: calculation(7), width=5, font=("Arial", 18))
btn7.grid(row=3, column=1)

btn8 = tk.Button(root, text='8', command=lambda: calculation(8), width=5, font=("Arial", 18))
btn8.grid(row=3, column=2)

btn9 = tk.Button(root, text='9', command=lambda: calculation(9), width=5, font=("Arial", 18))
btn9.grid(row=3, column=3)

btnMultiply = tk.Button(root, text='*', command=lambda: calculation("*"), width=5, font=("Arial", 18))
btnMultiply.grid(row=3, column=4)

btn4 = tk.Button(root, text='4', command=lambda: calculation(4), width=5, font=("Arial", 18))
btn4.grid(row=4, column=1)

btn5 = tk.Button(root, text='5', command=lambda: calculation(5), width=5, font=("Arial", 18))
btn5.grid(row=4, column=2)

btn6 = tk.Button(root, text='6', command=lambda: calculation(6), width=5, font=("Arial", 18))
btn6.grid(row=4, column=3)

btnSubstract = tk.Button(root, text='-', command=lambda: calculation("-"), width=5, font=("Arial", 18))
btnSubstract.grid(row=4, column=4)

btn1 = tk.Button(root, text='1', command=lambda: calculation(1), width=5, font=("Arial", 18))
btn1.grid(row=5, column=1)

btn2 = tk.Button(root, text='2', command=lambda: calculation(2), width=5, font=("Arial", 18))
btn2.grid(row=5, column=2)

btn3 = tk.Button(root, text='3', command=lambda: calculation(3), width=5, font=("Arial", 18))
btn3.grid(row=5, column=3)

btn0 = tk.Button(root, text='0', command=lambda: calculation(0), width=5, font=("Arial", 18))
btn0.grid(row=6, column=2)

btnDec = tk.Button(root, text='.', command=lambda: calculation("."), width=5, font=("Arial", 18))
btnDec.grid(row=6, column=3)

btnDoubleZero = tk.Button(root, text='00', command=lambda: calculation("00"), width=5, font=("Arial", 18))
btnDoubleZero.grid(row=6, column=1)

btnAdd = tk.Button(root, text='+', command=lambda: calculation("+"), width=5, font=("Arial", 18))
btnAdd.grid(row=5, column=4)

btnEquals = tk.Button(root, text='=', command=lambda: evaluate(), width=5, font=("Arial", 18))
btnEquals.grid(row=6, column=4)

btnOpen = tk.Button(root, text='(', command=lambda: calculation("("), width=5, font=("Arial", 18))
btnOpen.grid(row=2, column=2)

btnClose = tk.Button(root, text=')', command=lambda: calculation(")"), width=5, font=("Arial", 18))
btnClose.grid(row=2, column=3)

root.mainloop()
