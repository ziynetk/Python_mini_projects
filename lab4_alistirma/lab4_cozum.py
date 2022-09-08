from tkinter import *

class Labdort(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self , parent)
        self.parent = parent
        self.initUI()
        self.eventt()

    def initUI(self,event=None): #canvas ve sutunlarımızın tanımlanmaları
        self.pack()
        self.canvas = Canvas(self,height=310, width=400)
        self.sutun = self.canvas.create_rectangle(10, 300,80, 1, outline="black", fill="red", width=1)
        self.sutun2 = self.canvas.create_rectangle(90, 300, 160, 25, outline="black", fill="red", width=1)
        self.sutun3 = self.canvas.create_rectangle(170, 300, 240, 70, outline="black", fill="red", width=1)
        self.sutun4 = self.canvas.create_rectangle(250, 300, 320, 95, outline="black", fill="red", width=1)
        self.sutun5 = self.canvas.create_rectangle(330, 300, 400, 1, outline="black", fill="red", width=1)
        self.create_text = self.canvas.create_text(40, 300, anchor=SW, text="100", fill="red")
        self.create_text2 = self.canvas.create_text(120, 300, anchor=SW, text="90", fill="red")
        self.create_text3= self.canvas.create_text(200,300,anchor=SW,text="70",fill="red")
        self.create_text4= self.canvas.create_text(280,300,anchor=SW,text="60",fill= "red")
        self.create_text5=self.canvas.create_text(360,300,anchor=SW,text="100",fill="red")
        self.canvas.pack()

    def eventt(self,event=None): #eventleri tanımladığımız fonksiyonumuz
        self.canvas.tag_bind(self.sutun, '<Enter>', self.yuzdeler)
        self.canvas.tag_bind(self.sutun2, '<Enter>', self.yuzdeler)
        self.canvas.tag_bind(self.sutun3, '<Enter>', self.yuzdeler)
        self.canvas.tag_bind(self.sutun4, '<Enter>', self.yuzdeler)
        self.canvas.tag_bind(self.sutun5, '<Enter>', self.yuzdeler)
        self.canvas.tag_bind(self.sutun, "<Button-1>", self.sutun_bastir)
        self.canvas.tag_bind(self.sutun, "<Leave>", self.sutun_ayril)
        self.canvas.tag_bind(self.sutun2, "<Button-1>", self.sutun2_bastir)
        self.canvas.tag_bind(self.sutun2, "<Leave>", self.sutun_ayril)
        self.canvas.tag_bind(self.sutun3, "<Button-1>", self.sutun3_bastir)
        self.canvas.tag_bind(self.sutun3, "<Leave>", self.sutun_ayril)
        self.canvas.tag_bind(self.sutun4, "<Button-1>", self.sutun4_bastir)
        self.canvas.tag_bind(self.sutun4, "<Leave>", self.sutun_ayril)
        self.canvas.tag_bind(self.sutun5, "<Button-1>", self.sutun5_bastir)
        self.canvas.tag_bind(self.sutun5, "<Leave>", self.sutun_ayril)


    def sutun_ayril(self,event=None): #sutundan ayrıldığımızda eski rengine dönmesi için
        if self.canvas.itemcget(self.sutun, 'fill') == 'blue':
            self.canvas.itemconfig(self.sutun, fill="red")
        elif self.canvas.itemcget(self.sutun2, 'fill') == 'blue':
            self.canvas.itemconfig(self.sutun2, fill="red")
        elif self.canvas.itemcget(self.sutun3, 'fill') == 'blue':
            self.canvas.itemconfig(self.sutun3, fill="red")
        elif self.canvas.itemcget(self.sutun4, 'fill') == 'blue':
            self.canvas.itemconfig(self.sutun4, fill="red")
        elif self.canvas.itemcget(self.sutun5, 'fill') == 'blue':
            self.canvas.itemconfig(self.sutun5, fill="red")


    def sutun_bastir(self,event=None): #1.sutuna tıklayınca mavi olması için
        if (self.canvas.itemcget(self.sutun, 'fill')) == 'red':
            self.canvas.find_closest(90, 300, halo=None, start=None)
            self.canvas.itemconfig(self.sutun, fill="blue")
        else:
            self.canvas.itemconfig(self.sutun, fill="red")
    def sutun2_bastir(self,event=None): #2.sutuna tıklayınca mavi olması için
        if (self.canvas.itemcget(self.sutun2, 'fill')) == 'red':
            self.canvas.find_closest(90, 300, halo=None, start=None)
            self.canvas.itemconfig(self.sutun2, fill="blue")
        else:
            self.canvas.itemconfig(self.sutun2, fill="red")
    def sutun3_bastir(self,event=None): #3.sutuna tıklayınca mavi olması için
        if (self.canvas.itemcget(self.sutun3, 'fill')) == 'red':
            self.canvas.find_closest(90, 300, halo=None, start=None)
            self.canvas.itemconfig(self.sutun3, fill="blue")
        else:
            self.canvas.itemconfig(self.sutun3, fill="red")
    def sutun4_bastir(self,event=None): #4.sutuna tıklayınca mavi olması için
        if (self.canvas.itemcget(self.sutun4, 'fill')) == 'red':
            self.canvas.find_closest(90, 300, halo=None, start=None)
            self.canvas.itemconfig(self.sutun4, fill="blue")
        else:
            self.canvas.itemconfig(self.sutun4, fill="red")
    def sutun5_bastir(self,event=None): #5.sutuna tıklayınca mavi olması için
        if (self.canvas.itemcget(self.sutun5, 'fill')) == 'red':
            self.canvas.find_closest(90, 300, halo=None, start=None)
            self.canvas.itemconfig(self.sutun5, fill="blue")
        else:
            self.canvas.itemconfig(self.sutun5, fill="red")


    def yuzdeler(self, event): #yuzdelerin görünmesi için gerekli fonksiyon
        if ((self.canvas.itemcget(self.sutun, 'fill')) or
                (self.canvas.itemcget(self.sutun2, 'fill')) or
                (self.canvas.itemcget(self.sutun3, 'fill')) or
                (self.canvas.itemcget(self.sutun4, 'fill'))or
                (self.canvas.itemcget(self.sutun5, 'fill')) == 'red'):
            self.canvas.itemconfig(self.create_text, fill="white")
            self.canvas.itemconfig(self.create_text2, fill="white")
            self.canvas.itemconfig(self.create_text3, fill="white")
            self.canvas.itemconfig(self.create_text4, fill="white")
            self.canvas.itemconfig(self.create_text5, fill="white")

