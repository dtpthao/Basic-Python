from tkinter import *
#import Image, ImageTk
from PIL import Image, ImageTk
from math import *

root = Tk()
root.title("Lab4")

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x=x
        self.y=y
    
    def fx(self):
        if self.x <= 0:
            self.y = abs(self.x)**5 + 1/tan(self.x + 2)
        elif 0<self.x and self.x<=5:
            self.y = (5*self.x + self.x*self.x)/pow(self.x*self.x + 3, 3)
        else:
            self.y = pow(sin(self.x+3),2)/(self.x**5 - 1/tan(pi*pow(self.x,3))) #* (10**5)

    def base(self):
        self.x += 30
        self.y = 220 - self.y

class Input:
    def __init__(self, s, r=0):
        self.lbl = Label(root,text= "Type " + s,font="Arial 18")
        self.ent = Entry(root,width=10,bd=3)
        self.grd(r)

    def grd(self, r=0):
        self.lbl.grid(row=r,column=1)
        self.ent.grid(row=r,column=2)

# class Input:
#     lbl = Label(root)
#     ent = Entry(root)
#     def __init__(self, name, r=0):
#         #self.lbl = Label(root, text="Вход "+name, font="Arial 14")
#         #self.ent = Entry(root, width=10, bd=3)
#         self.lbl["text"]="Вход "+name
#         self.lbl["font"]="Arial 14"
#         self.ent['width']=10
#         self.ent['bd']=3
#         self.lbl.grid(row=r,column=1)
#         self.ent.grid(row=r,column=2)
#         #self.grd(r)

#     def grd(self, r=0):
#         self.lbl.grid(row=r,column=1)
#         self.ent.grid(row=r,column=2)

def Graph(event):
    n = float(xn.ent.get())
    k = float(xk.ent.get())
    h = float(xh.ent.get())
    numP = k - n
    incrx = 500/numP
    incry = 5000000
    p = Point(n+h)
    p.fx()
    P = Point()
    P2 = Point()
    P.x = (p.x - n)*incrx + obj.base.x
    P.y = obj.base.y - p.y*incry
    while p.x < k:
        P2 = P
        #P2.x = (p.x - n)*incrx + obj.base.x
        #P2.y = obj.base.y - p.y*incry
        p = Point(p.x+h)
        p.fx()
        P.x = (p.x - n)*incrx + obj.base.x
        P.y = obj.base.y - p.y*incry
        print(P.x,P.y)
        print("P", P2.x, P2.y)
        #print(p2.x, p2.y)
        obj.c.create_line(P.x, P.y,P2.x,P2.y)

class Canv:
    def __init__(self):
        self.base = Point(30.0, 330.0)
        self.c = Canvas(root, width=500, height=350, bg="white", cursor="pencil")
        self.c.create_line(self.base.x,self.base.y,430,self.base.y,width=2,fill="black",arrow=LAST)
        self.c.create_line(self.base.x,self.base.y,self.base.x,20,width=2,fill="black",arrow=LAST)
        self.c.grid(row=9)

# def Canv():
#     bP = Point(30,220)
#     c = Canvas(root, width=550, height=250, bg="lightblue", cursor="pencil")
#     c.create_line(30,220,500,220,width=2,fill="black",arrow=LAST)
#     c.create_line(30,220,30,20,width=2,fill="black",arrow=LAST)
#     c.grid(row=5)
#     return c


#root.geometry("700x600")

lbl1 = Label(root, text="Построение графика функции на интервале [xn;xk]", font="Arial 18")
lbl2 = Label(root, text="Введите данные", font="Arial 16")
xn = Input("xn",2)
xk = Input("xk",3)
xh = Input("xh",4)

obj = Canv()#as(root, width=550, height=250, bg="lightblue", cursor="pencil")
#img = Image.open("lab4.rgb", )
#img2 = ImageTk.PhotoImage(img)
img = Image.open("lab44.gif")
img2 = ImageTk.PhotoImage(img)
lbl3 = Label(root, image=img2)
lbl3.image = img2

but = Button(root, text="Enter")
quitbut = Button(root, text="Quit", command=quit)
lbl1.grid(row=0)
lbl2.grid(row=1,column=1)
#lbl3.grid(row=2,column=0)
lbl3.place(x=50, y=30)
#c.grid(row=5)
but.grid(row=10)
quitbut.grid(row=10,column=1)
#c.bind("<Button>", Graph)
but.bind("<Button-1>", Graph)

# lbl1.pack()
# lbl2.pack()
# c.pack()
# but.pack()


root.bind("<space>",exit)
root.mainloop()