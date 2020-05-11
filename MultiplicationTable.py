from tkinter import *
from tkinter import messagebox

#window
top=Tk()
top.geometry("700x400")
top.title("Multiplication Tables")
top.configure(bg="black")

#defining string variable
E1 = StringVar()

#multiplication code
def tables():
     try:
          print("---------------")
          m =int( E1.get())
          for i in range(1,11):
               print(m ,'x' , i ,'=',i * m )
     except:
          print("Enter a number!!!")
          
     
          
#Label,Entry and Button widgets
Head = Label(top,text="Multiplication Table",font=("Arial 18"),fg="white",bg="black")
Head.place(x = 240,y = 10)

e1=Entry(top,bd=1,textvariable=E1,font=("Arial 18"),fg="black",bg="white")
e1.place(x=210,y=100)

sbmitbtn = Button(top, text = "Get Table",command=tables,font=("Arial 18"),activebackground = "pink", activeforeground = "blue")
sbmitbtn.place(x = 280, y = 190)


top.mainloop()  
