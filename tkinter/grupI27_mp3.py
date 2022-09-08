from tkinter import *
from tkinter import filedialog
import csv
import pandas as pd
from tkinter import messagebox
import numpy as np

class Miniproje(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()
        self.pack()

    def initGUI(self): #widgetlar
        self.var = StringVar()
        self.label1 = Label(self, text="Yandaki butonu kullanarak diger kullanicilari yukleyebilirsiniz: ")
        self.label1.grid(row=0, column=1, columnspan=5)
        self.buton1 = Button(self, text="Cvs Dosya Sec", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.dosya_yukle)
        self.buton1.grid(row=0, column=6,columnspan=3)
        self.label2 = Label(self, text="Kullanici Bilgilerini Gir", font="verdana 18 bold ")
        self.label2.grid(row=1, column=1, columnspan=10)
        self.lbkategori = Listbox(self, height=9, width=30, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lbkategori.grid(row=3, column=0, columnspan=3)
        self.label3 = Label(self, text="Kategoriler")
        self.label3.grid(row=2, column=0, columnspan=2)
        self.label4 = Label(self, text="Toplam Miktar")
        self.label4.grid(row=2, column=3, columnspan=1,sticky=W)
        self.label5 = Label(self, text="Kullanici Harcamalari")
        self.label5.grid(row=2, column=6, columnspan=2)
        self.entry1 = Entry(self, width=15, bg="pink", fg="purple",textvariable=self.var)
        self.entry1.grid(row=3, column=3, columnspan=1, sticky=W)
        self.buton2= Button(self, text="Harcama Gir", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",comman=self.harcama_gir)
        self.buton2.grid(row=3,column=4, columnspan=2)
        self.lbharcama = Listbox(self, height=9, width=43, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lbharcama.grid(row=3, column=6, columnspan=2)
        self.label6 = Label(self, text="Oneri Ekrani", font="verdana 18 bold ")
        self.label6.grid(row=4, column=1, columnspan=10)
        self.v= IntVar()
        self.radiobutton1 = Radiobutton(self,text="Kategori-Tabanli-Oneri", variable=self.v, value=0)
        self.radiobutton1.grid(row=6, column=0, sticky='we')
        self.radiobutton2 = Radiobutton(self,text="Firma-Tabanli-Oneri", variable=0, value=0)
        self.radiobutton2.grid(row=7, column=0, sticky='we')
        self.label7 = Label(self, text="Oneriler")
        self.label7.grid(row=5, column=3, columnspan=2)
        self.label8 = Label(self, text="Magazalar:")
        self.label8.grid(row=5, column=5, columnspan=2)
        self.buton3 = Button(self, text="Oneri Yap", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.oneri)
        self.buton3.grid(row=6, column=1, columnspan=2)
        self.buton4 = Button(self, text="Benzer Magaza Bul", bg="#F5A9A9", fg="purple", font="verdana 8 bold ")
        self.buton4.grid(row=7, column=1, columnspan=2)
        self.lboneri = Listbox(self, height=9, width=30, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lboneri.grid(row=6, column=3, columnspan=2,rowspan=2)
        self.lbmagaza = Listbox(self, height=9, width=30, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lbmagaza.grid(row=6, column=5, columnspan=2,rowspan=2)


    def dosya_yukle(self):  #dosya yükleme işlemleri bu fonksiyonda yapılıyor
        try:
            self.statePlantFile = filedialog.askopenfilename(initialdir="/", title="ARA",  # csv dosyası aratıyoruz
                                                                 filetypes=(
                                                                 ("txt files", "*.csv"), ("all files", "*.*")))

            with open(self.statePlantFile) as file:
                csv_reader = csv.reader(file, delimiter=',')
                line_count = 0

                eskideger=str() #row'un eski değerini tutuyoruz aynı kategoriyi birden fazla kez bastırmamak için
                for row in csv_reader:
                    if row[0] == eskideger:
                        continue
                    elif line_count != 0:
                        self.lbkategori.insert(END, row[0]) #kategori değerlerini alıyoruz
                        eskideger=row[0]

                    line_count += 1

        except Exception as e: #hata kontrolü
            print("***YAML dosyasi okurken bir hata olustu*** \n{}".format(e))

    def harcama_gir(self): #harcamaları harcama ekranına ve database'e aktarma işlemleri bu fonksiyonda yapılıyor
        if not self.lbkategori.curselection(): #kategori seçimi yapılmadıysa hata mesajı veriyor
            messagebox.showinfo("Hata!", "Lutfen bir kategori secimi yapiniz!")
        elif self.var.get() == "": #miktar girilmediyse hata mesajı veriyor
            messagebox.showinfo("Hata!", "Lutfen miktar giriniz!")
        else:
            listboxSel = map(str, self.lbkategori.curselection())  # Get selections in listbox
            b = str()
            for sel in listboxSel:
                b = self.lbkategori.get(sel)

            self.liste = [b + ":  " +str(self.var.get())]
            with open("veriler.db", "a") as file: #verileri yazdığımız db dosyamızı oluşturuyoruz
                for i in self.liste:
                    self.lbharcama.insert(END, i) #harcama verilerini harcama listboxuna aktarıyoruz
                    file.write(i) #harcama verilerini db dosyamıza aktarıyoruz
                    file.write("\n")

        self.entry1.delete(0, END) #her aktarmanın sonunda entry temizleniyor

    def oneri(self):

        df = pd.read_csv('kredikarti_verii.csv', #csv dosyasının içindeki değerleri alıyoruz # her şirket için  her kategorideki toplam fiyatları hesaplıyoruz
                         delimiter=',',
                         dtype={'Account': np.str, 'Company': np.str, 'JV Value': np.float32},
                         usecols=["Account", "Company", "JV Value"])

        a = df.groupby(by=['Company', "Account"]).aggregate({'JV Value': 'sum'})
        print(a) #her şirket için her kategoride yapılan harcamaların toplamını gösterir (critics yapısı)

        #jaccard benzerliği kodu
        kesisim = {}
        for item in prefs[person1]:
            if item in prefs[person2]:
                kesisim[item] = 1
        birlesim = {}
        for item in prefs[person1]:
            if item in prefs[person2]:
                birlesim[item] = 1
            if item in prefs[person1]:
                birlesim[item] = 1

        return float(len(kesisim) / len(birlesim))


def main():
    root = Tk()
    root.geometry("750x450+350+250")
    app = Miniproje(root)
    root.tk_setPalette("#6A0888")
    root.title("Harcama Öneri Sistemi")
    app.mainloop()

main()
