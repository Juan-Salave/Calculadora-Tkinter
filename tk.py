
from tkinter import *


#def operacion(button1,button_dolar):
#    precio_total = button1 * button_dolar

root = Tk()
root.title("Culculadora")

#funcion para crear una ventama con info.
#def info():
#    messagebox.showinfo("Presupuesto", "Su precio total")

i = 0
#entrada
display = Entry(root,font=("arial",27, "bold"),bd=7, insertwidth = 2, justify="right", textvariable="", width=22,)
display.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5 )

#funciones
def click_button(valor):
    global i
    display.insert(i, valor)
    i+=1

def borrar_todo():
    display.delete(0, END)
    i = 0

def operacion():
    ecuacion = display.get()
    resultado = eval(ecuacion)
    display.delete(0, END)
    display.insert(0, resultado)
    i = 0

#botones
button1 = Button(root, text = "1", width = 5, height = 2, command = lambda:click_button(1))
button2 = Button(root, text = "2", width = 5, height = 2, command = lambda:click_button(2))
button3 = Button(root, text = "3", width = 5, height = 2, command = lambda:click_button(3))
button4 = Button(root, text = "4", width = 5, height = 2, command = lambda:click_button(4))
button5 = Button(root, text = "5", width = 5, height = 2, command = lambda:click_button(5))
button6 = Button(root, text = "6", width = 5, height = 2, command = lambda:click_button(6))
button7 = Button(root, text = "7", width = 5, height = 2, command = lambda:click_button(7))
button8 = Button(root, text = "8", width = 5, height = 2, command = lambda:click_button(8))
button9 = Button(root, text = "9", width = 5, height = 2, command = lambda:click_button(9))
button0 = Button(root, text = "0", width = 5, height = 2, command = lambda:click_button(0))
button_dolar_blue = Button(root, text = "$ Blue", width = 5, height = 2, command = lambda:click_button(1025.00))

button_ac = Button(root, text = "AC", width = 5, height = 2, command=lambda:borrar_todo())
button_parent1 = Button(root, text = "(", width = 5, height = 2, command=lambda:click_button("("))
button_parent2 = Button(root, text = ")", width = 5, height = 2, command=lambda:click_button(")"))
button_punto = Button(root, text = ".", width = 5, height = 2, command=lambda:click_button("."))

button_porcentaje = Button(root, text = "%",width = 5, height = 2, command=lambda:click_button("%"))
button_dolar_ofi = Button(root, text = "$ Oficial",width = 5, height = 2, command=lambda:click_button(847.11))
#button = Button(root, text = ,width = 5, height = 2)
#button = Button(root, text = ,width = 5, height = 2)

button_div = Button(root, text = "÷", width = 5, height = 2, command=lambda:click_button("/"))
button_mul = Button(root, text = "x", width = 5, height = 2, command=lambda:click_button("*"))
button_sum = Button(root, text = "+", width = 5, height = 2, command=lambda:click_button("+"))
button_res = Button(root, text = "-", width = 5, height = 2, command=lambda:click_button("-"))
button_borrar = Button(root, text = chr(9003), width = 5, height = 2, command=lambda:click_button())
button_resul = Button(root, text = "=", width = 16, height = 2, command=lambda:operacion())

#agregar botones a la root 
button_ac.grid(row = 1, column = 0, padx = 5, pady = 5)
button_parent1.grid(row = 1, column = 1, padx = 5, pady = 5)
button_parent2.grid(row = 1, column = 2, padx = 5, pady = 5)
button_div.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 4, pady = 4)
button8.grid(row = 2, column = 1, padx= 4, pady = 4)
button9.grid(row = 2, column = 2, padx= 4, pady = 4)
button_mul.grid(row = 2, column = 3, padx= 4, pady = 4)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_res.grid(row = 4, column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, padx = 5, pady = 5)
button_punto.grid(row = 5, column = 1, padx = 5, pady = 5)
button_porcentaje.grid(row = 5, column = 2, padx = 5, pady = 5)
button_borrar.grid(row = 5, column= 3, padx = 5, pady = 5)

button_dolar_ofi.grid(row = 6, column = 0, padx = 5, pady = 5)
button_dolar_blue.grid(row = 6, column = 1, padx = 5, pady = 5)
button_resul.grid(row = 6, column = 2, columnspan = 2, padx = 5, pady = 5,)
#button.grid(row = , column = , padx = 5, pady = 5)
#button.grid(row = , column = , padx = 5, pady = 5)

root.mainloop()