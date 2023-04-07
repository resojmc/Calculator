import tkinter as tk
from sympy import *

root = tk.Tk()
root.geometry("200x130")
root.resizable(False, False)
root.title("Calculator")

def equation():
    m = main_entry.get()
    eq = eval(m)
    return eq

def solve_equation():
    solution = equation()
    result_label_2.config(text=f"{solution}")

main_entry = tk.Entry(root, )
main_entry.place(relx=0.485, rely=0.08, width=102, height=20, anchor="w")

result_label = tk.Label(root, text="Result: ")
result_label.place(relx=0.485, rely=0.25, width=102, anchor="w")

result_label_2 = tk.Label(root, text="")
result_label_2.place(relx=0.485, rely=0.40, width=102, anchor="w")

def add_zero():
    main_entry.insert(tk.END, "0")
button_0 = tk.Button(root, text="0", width=6, height=1, command=add_zero)
button_0.place(relx=0.238, rely=0.9, anchor="e")

def add_one():
    main_entry.insert(tk.END, "1")
button_1 = tk.Button(root, text="1", width=int(2.85), height=1, command=add_one)
button_1.place(relx=0.12, rely=0.7, anchor="e")

def add_two():
    main_entry.insert(tk.END, "2")
button_2 = tk.Button(root, text="2", width=int(2.9), height=1, command=add_two)
button_2.place(relx=0.241, rely=0.7, anchor="e")

def add_three():
    main_entry.insert(tk.END, "3")
button_3 = tk.Button(root, text="3", width=int(2.9), height=1, command=add_three)
button_3.place(relx=0.362, rely=0.7, anchor="e")

def add_four():
    main_entry.insert(tk.END, "4")
button_4 = tk.Button(root, text="4", width=int(2.9), height=1, command=add_four)
button_4.place(relx=0.12, rely=0.5, anchor="e")

def add_five():
    main_entry.insert(tk.END, "5")
button_5 = tk.Button(root, text="5", width=int(2.9), height=1, command=add_five)
button_5.place(relx=0.241, rely=0.5, anchor="e")

def add_six():
    main_entry.insert(tk.END, "6")
button_6 = tk.Button(root, text="6", width=int(2.9), height=1, command=add_six)
button_6.place(relx=0.362, rely=0.5, anchor="e")

def add_seven():
    main_entry.insert(tk.END, "7")
button_7 = tk.Button(root, text="7", width=int(2.9), height=1, command=add_seven)
button_7.place(relx=0.12, rely=0.3, anchor="e")

def add_eight():
    main_entry.insert(tk.END, "8")
button_8 = tk.Button(root, text="8", width=int(2.9), height=1, command=add_eight)
button_8.place(relx=0.241, rely=0.3, anchor="e")

def add_nine():
    main_entry.insert(tk.END, "9")
button_9 = tk.Button(root, text="9", width=int(2.9), height=1, command=add_nine)
button_9.place(relx=0.362, rely=0.3, anchor="e")

def add_decimal():
    main_entry.insert(tk.END, ".")
button_d = tk.Button(root, text=".", width=int(2.9), height=1, command=add_decimal)
button_d.place(relx=0.362, rely=0.9, anchor="e")

button_e = tk.Button(root, text="=", width=int(2.9), height=1, command=solve_equation)
button_e.place(relx=0.482, rely=0.9, anchor="e")

def add_plus():
    main_entry.insert(tk.END, "+")
button_p = tk.Button(root, text="+", width=int(2.9), height=1, command=add_plus)
button_p.place(relx=0.482, rely=0.7, anchor="e")

def add_minus():
    main_entry.insert(tk.END, "-")
button_s = tk.Button(root, text="-", width=int(2.9), height=1, command=add_minus)
button_s.place(relx=0.482, rely=0.5, anchor="e")

def add_multiply():
    main_entry.insert(tk.END, "*")
button_m = tk.Button(root, text="*", width=int(2.9), height=1, command=add_multiply)
button_m.place(relx=0.482, rely=0.3, anchor="e")

def add_divide():
    main_entry.insert(tk.END, "/")
button_q = tk.Button(root, text="/", width=int(2.9), height=1, command=add_divide)
button_q.place(relx=0.482, rely=0.1, anchor="e")

def clear():
    main_entry.delete(0, tk.END)
button_clear = tk.Button(root, text="CLEAR ALL", width=int(9), height=1, command=clear)
button_clear.place(relx=0.36, rely=0.1, anchor="e")

def delete_entry():
    main_entry.delete(len(main_entry.get())-1, tk.END)
button_delete = tk.Button(root, text="Delete", width=6, height=1, command=delete_entry)
button_delete.place(relx=0.485, rely=0.9, width=104, anchor="w")

root.mainloop()