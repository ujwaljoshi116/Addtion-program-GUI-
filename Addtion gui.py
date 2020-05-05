from tkinter import *

#------------------------#main code -------------------------- 

def addNumbers():
    try:
        
        res=int(e1.get())+int(e2.get())
        myText.set(res)
    except:
        print("Enter value in digits")
#------------------------#main window-------------------------- 
win1 = Tk()
win1.geometry("700x400")
win1.title("Addtion")
myText=StringVar();

#------------------------#title-------------------------- 

title01=Label(win1,text="Addtion")
title01.configure(font="arial 20")
title01.place(x=270,y=0)

#------------------------#label 1-------------------------- 

l_1=Label(win1, text="Num1")
l_1.place(x=5,y=125)
l_1.configure(font="arial 15")

#------------------------#label 2-------------------------- 

l_2=Label(win1, text="Num2")
l_2.place(x=5,y=220)
l_2.configure(font="arial 15")

#------------------------#label 3-------------------------- 

l_3=Label(win1, text="Result:")
l_3.place(x=5,y=325)
l_3.configure(font="arial 15")

#------------------------#label 4-------------------------- 

result=Label(win1, text="", textvariable=myText)
result.configure(font="arial 15")
result.place(x=150,y=330)

#------------------------#Entry widget 1-------------------------- 

e1 = Entry(win1,bd=4,fg="blue")
e1.configure(font="arial 15")
e1.place(x=150,y=127)

#------------------------#Entry widget 2-------------------------- 

e2 = Entry(win1,bd=4,fg="blue")
e2.configure(font="arial 15")
e2.place(x=150,y=222)

#------------------------#Button widget-------------------------- 
 
b = Button(win1, text="Calculate", command=addNumbers,)
b.configure(font="arial 15")
b.place(x=400,y=180) 
 
mainloop()

            
