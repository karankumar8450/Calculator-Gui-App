import tkinter as tk
#step 1 - create main window 
window = tk.Tk()
window.title("My calculator")
window.geometry("300x400")#widhtx height(pixel)

#step 2 - create a display/entry box to show the expression
display = tk.Entry(window,background="white",font=("Arial",20),justify="right")
display.grid(row=0,column=0,columnspan=4,padx=5,pady=10,sticky="nsew")

#step 3 - create a function for button click
def Button_click(value):
    display.insert(tk.END,value)

# step 4 - create a clear function to remove all the expression from the display
def clear_display():
        display.delete(0,tk.END)

#step 5 - calculate result 
def calculate_result():
    expres = display.get()  # to get an expression
    numbers = []
    operators = []
    current_num = ""

    for ch in expres:
        if ch in "+-*/":
            if current_num == "":
                display.delete(0, tk.END)
                display.insert(tk.END, "Invalid")
                return
            numbers.append(float(current_num))
            operators.append(ch)
            current_num = ""
        else:
            current_num += ch

    if current_num == "":
        display.delete(0, tk.END)
        display.insert(tk.END, "Invalid")
        return
    numbers.append(float(current_num))

    a = numbers[0]
    for i in range(len(operators)):
        op = operators[i]
        b = numbers[i + 1]

        if op == "+":
            a += b
        elif op == "-":
            a -= b
        elif op == "*":
            a *= b
        elif op == "/":
            if b == 0:
                display.delete(0, tk.END)
                display.insert(tk.END, "Div by 0")
                return
            a /= b

    display.delete(0, tk.END)     # purana expression hatao
    display.insert(tk.END, str(a))   # result dikhao

buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("+",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("-",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("*",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("/",4,3),
]

for (text,row,column) in buttons:
    if text == "=":
       btn =  tk.Button(window,text=text,font=("Arial",20),
                        command=calculate_result)
    else:
        btn = tk.Button(window,text=text ,font=("Arial",20),
                        command= lambda t=text : Button_click(t))
    btn.grid(row= row,column= column ,padx=3,pady=3,sticky= "nsew")

clear_button = tk.Button(window,text= "C",font=("Arial",20),
                         command=clear_display,fg="red")
clear_button.grid(row=5,column=0,columnspan=4,padx=3,pady=5,sticky="nsew")


for i in range(6):
    window.rowconfigure(i,weight=1)
for i in range(4):
    window.columnconfigure(i,weight=1)

window.mainloop()