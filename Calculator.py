import tkinter as t
top = t.Tk()
top.title("Calculator")
top.geometry("354x460")
textin = t.StringVar()
operator = ""
def clickbut(numbers):
	global operator
	operator += str(numbers)
	textin.set(operator)
'''def equalbut():
	global operator
	add = str(eval(operator))
	textin.set(add)
	operator = add'''
def equalbut():
	global operator
	add = str(eval(inputting.get()))
	textin.set(add)
	operator = add
def entrykey(event):
	global operator
	add = str(eval(inputting.get()))
	textin.set(add)
	operator = add
top.bind("<Return>",lambda a: entrykey(a))
def exitkey(event):
	quit()
top.bind("<Alt-F4>",lambda a : exitkey(a))
def clrbut():
	global operator
	textin.set("")
	operator = ""
greeting = t.Label(top,text = "CALCULATOR",font = ("Arial",30,"bold"))
inputting = t.Entry(top,font = ("Arial",12,"bold"),textvar = textin,width = 25,bd = 5, bg = "powder blue")
buttons = t.Button(text = "%", height = 3, width = 4,fg = "black",command = lambda: clickbut("%"),bg = "powder blue")
buttons.place(x = 130, y = 100)
buttons2 = t.Button(text = "CE",height = 3, width = 4,fg = "black",command = lambda: clrbut(),bg = "powder blue").place(x = 50,y=100)
buttons3 = t.Button(text = "C",height = 3, width = 4,fg = "black",command = lambda: clrbut(),bg = "powder blue").place(x = 90,y=100)
buttons4 = t.Button(text = "÷",height = 3, width = 4,fg = "black",command = lambda: clickbut("/"),bg = "powder blue").place(x = 170,y=100)
buttons5 = t.Button(text = "7",height = 3, width = 4,fg = "black",command = lambda: clickbut("7"),bg = "powder blue").place(x = 50,y=160)
buttons6 = t.Button(text = "8",height = 3, width = 4,fg = "black",command = lambda: clickbut("8"),bg = "powder blue").place(x = 90,y=160)
buttons7 = t.Button(text = "9",height = 3, width = 4,fg = "black",command = lambda: clickbut("9"),bg = "powder blue").place(x = 130,y=160)
buttons8 = t.Button(text = "X",height = 3, width = 4,fg = "black",command = lambda: clickbut("*"),bg = "powder blue").place(x = 170,y=160)
buttons9 = t.Button(text = "4",height = 3, width = 4,fg = "black",command = lambda: clickbut("4"),bg = "powder blue").place(x = 50, y=220)
buttons12 = t.Button(text = "5",height = 3, width = 4,fg = "black",command = lambda: clickbut("5"),bg = "powder blue").place(x = 90,y=220)
buttons13 = t.Button(text = "6",height = 3, width = 4,fg = "black",command = lambda: clickbut("6"),bg = "powder blue").place(x = 130,y=220)
buttons14 = t.Button(text = "-",height = 3, width = 4,fg = "black",command = lambda: clickbut("-"),bg = "powder blue").place(x = 170,y=220)
buttons15 = t.Button(text = "1",height = 3, width = 4,fg = "black",command = lambda: clickbut("1"),bg = "powder blue").place(x = 50, y = 280)
buttons22 = t.Button(text = "2",height = 3, width = 4,fg = "black",command = lambda: clickbut("2"),bg = "powder blue").place(x = 90,y=280)
buttons23 = t.Button(text = "3",height = 3, width = 4,fg = "black",command = lambda: clickbut("3"),bg = "powder blue").place(x = 130,y=280)
buttons24 = t.Button(text = "+",height = 3, width = 4,fg = "black",command = lambda: clickbut("+"),bg = "powder blue").place(x = 170,y=280)
buttons25 = t.Button(text = "x^",height = 3, width = 4,fg = "black",command = lambda: clickbut("**"),bg = "powder blue").place(x = 50, y = 340)
buttons32 = t.Button(text = "0",height = 3, width = 4,fg = "black",command=lambda: clickbut("0"),bg = "powder blue").place(x = 90,y=340)
buttons33 = t.Button(text = ".",height = 3, width = 4,fg = "black",command=lambda: clickbut("."),bg = "powder blue").place(x = 130,y=340)
buttons34 = t.Button(text = "=",height = 3, width = 4,fg = "black",command = lambda: equalbut(),bg = "powder blue").place(x = 170,y=340)
greeting.pack()
inputting.pack()
top.mainloop()
