from tkinter import *
from tkinter import filedialog
import pandas as pd
import pyexcel as pe
import yaml


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()

        self.pack()

    def initGUI(self):
        self.var = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4=StringVar()
        self.buton1 = Button(self, text="Aktar", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.dosya_yukle)
        self.buton1.grid(row=2, column=0, sticky=W, columnspan=2,ipadx=9)
        self.buton2 = Button(self, text="Secili Sil", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.secileni_sil)
        self.buton2.grid(row=2, column=1, sticky=W,columnspan=2,ipadx=15)
        self.buton3 = Button(self, text="Hepsini Sil", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.hepsini_sil)
        self.buton3.grid(row=2, column=2, sticky=W, columnspan=2,ipadx=9)
        self.buton_excel = Button(self, text="2Excel", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.excel_button)
        self.buton_excel.grid(row=2, column=6,sticky=E)
        self.buton_ekle = Button(self, text="Ekle", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.ekle_butonu)
        self.buton_ekle.grid(row=4, column=4, sticky=E,columnspan=2)
        self.label1=Label(self,text="Tarih Ekle:")
        self.label1.grid(row=3, column=0,ipady=10)
        self.label2 = Label(self, text="İsim Ekle:")
        self.label2.grid(row=3, column=1,ipady=10)
        self.label3 = Label(self, text="Kategori Seç:")
        self.label3.grid(row=3, column=2, ipady=10)
        self.label4 = Label(self, text="Miktar Ekle:")
        self.label4.grid(row=3, column=3, ipady=10)
        self.entry1=Entry(self, width=8,bg="pink",fg="purple",textvariable= self.var)
        self.entry1.grid(row=4,column=0,ipadx=12)
        self.entry2 = Entry(self, width=8, bg="pink", fg="purple",textvariable= self.var2)
        self.entry2.grid(row=4, column=1, ipadx=15)
        self.entry3 = Entry(self, width=8, bg="pink", fg="purple",textvariable= self.var3)
        self.entry3.grid(row=4, column=3, ipadx=15)
        self.lb2 = Listbox(self, height=5, width=10, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lb2.grid(row=4, column=2,ipadx=10)
        self.lb = Listbox(self, height=20, width=85, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lb.grid(row=1, column=0, columnspan=7)

        kategori=["Yiyecek","İçecek","Giyim","Ev","Elektronik"]
        for i in kategori:
            self.lb2.insert(END,i)

    def excel_button(self): #verileri excel dosyasına aktarıyoruz
        listboxSel = map(str, self.lb2.curselection())  # Get selections in listbox
        b = str()
        excel_ = {'Tarih': [str(self.var)],
                'İsim': [str(self.var2)],
                'Kategori': [b],
                'Miktar': [str(self.var3)]
                }
        df = pd.DataFrame(excel_, columns=['Tarih', 'İsim','Kategori','Miktar'])
        export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
        df.to_excel(export_file_path, index=False, header=True)

    def ekle_butonu(self):
        listboxSel = map(str, self.lb2.curselection())  # Get selections in listbox
        b= str()

        for sel in listboxSel:
            b=self.lb2.get(sel)
        self.liste = [str(self.var.get())+",  "+str(self.var2.get())+",  "+b+",  "+str(self.var3.get())]
        for i in self.liste:
            self.lb.insert(END, i)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)


    def secileni_sil(self):  # seçileni silme işlemini bu fonksiyonda yapıyoruz
        try:
            self.lb.delete(self.lb.curselection())
        except:
            print("secim yapmadiniz silmek için bir seçim yapmalısınız.")

    def hepsini_sil(self):
        self.lb.delete(0, END)  # hepsini sil butonun işlevini gerçekleştirdiğimiz fonksiyon

    def dosya_yukle(self):  # Aktar butonumuzun işlevini yerine getirebilmesi bilgisayardaki herhangi bir yaml dosyasını
        # çalıştırabilmek için kullanılan bir fonksiyondur.
        try:
            self.statePlantFile = filedialog.askopenfilename(initialdir="/", title="ARA",  # yaml dosyası aratıyoruz
                                                             filetypes=(("txt files", "*.yaml"), ("all files", "*.*")))

            with open(self.statePlantFile) as file:

                file.seek(235)
                for i in file:
                    if (i != "\n"):
                        self.lb.insert(END, i[4:])  # yaml dosyasının içeriğini "lb" yani listboxa aktarıyoruz

        except Exception as e:
            print("***YAML dosyasi okurken bir hata olustu*** \n{}".format(e))


def main():
    root = Tk()
    root.geometry("650x500+300+300")
    app = Example(root)
    root.tk_setPalette("#6A0888")
    root.title("Harcama Raporu")
    root.resizable(width=TRUE, height=TRUE)
    app.mainloop()

main()
