from tkinter import *
from math import *
from PIL import Image, ImageTk

def Output(event):
    x = int(X.ent.get())
    a = int(A.ent.get())
    result.delete(1.0, END)
    if x <= 0:
        result.insert(END, "f(x) = cosx + x^3 = ")
        result.insert(END, cos(x) + x**3)
    elif 0<x and x<=a:
        result.insert(END, "f(x) = sqrt(x^3) * sinx = ")
        result.insert(END, sqrt(x**3) * sin(x))
    else:
        result.insert(END, "f(x) = 8 + cos3x = ")
        result.insert(END, 8 + cos(3*x))

class Input:
    def __init__(self, s, r=0):
        self.lbl = Label(root,text= "Type " + s,font="Arial 18")
        self.ent = Entry(root,width=10,bd=3)
    #     self.grd(r)
    # def grd(self, r=0):
	# 	self.lbl.grid(row=r,column=0)
	# 	self.ent.grid(row=r,column=1,pdax=5,pday=5)
        #self.lbl.pack()#side=LEFT, padx = 1, pady = 3)
        #self.ent.pack()#side=RIGHT, padx = 1, pady = 3)

root = Tk()
root.title("Simple")
root.geometry("250x300")

X = Input("x:",0)
A = Input("a:",1)

Lbl = Label(root,text="Result: ",font="Arial 18")
result = Text(root,width=20,height=3,bd=3,font="14",wrap=WORD)
but = Button(root,text="Enter")
quitBut = Button(root,text="Quit",command=quit)

# img = Image.open("img.gif")
# img2 = ImageTk.PhotoImage(img)
# lbl1 = Label(root, image=img2)
# lbl1.image = img2
# lbl1.place(x=20, y=20)

but.bind("<Button-1>", Output)

X.lbl.grid(row=30,column=0,padx=5)
X.ent.grid(row=30,column=1,padx=5,pady=10)
A.lbl.grid(row=31,column=0)#,padx=5)
A.ent.grid(row=31,column=1)#,padx=5,pady=10)
Lbl.grid(row=2,column=0,padx=5)
result.grid(row=2,column=1,padx=5,pady=10)
but.grid(row=3,column=0,padx=5)
quitBut.grid(row=3,column=2,padx=20)

#Lbl.pack()#side=LEFT)
#result.pack()
#but.pack(side=LEFT)
#quitButton.pack(side=RIGHT)
root.bind("<space>", exit)
root.mainloop()
