from tkinter import *
from tkinter import filedialog
import yaml


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initGUI()
        self.pack()

    def initGUI(self):
        self.buton1 = Button(self, text="Aktar", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",
                             command=self.dosya_yukle)
        self.buton1.grid(row=2, column=0)
        self.buton2 = Button(self, text="Secili Sil", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",
                             command=self.secileni_sil)
        self.buton2.grid(row=2, column=1)
        self.buton3 = Button(self, text="Hepsini Sil", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",
                             command=self.hepsini_sil)
        self.buton3.grid(row=2, column=2)
        self.lb = Listbox(self, height=20, width=55, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lb.grid(row=1, column=0, columnspan=3)

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

                file.seek(215)
                for i in file:
                    if (i != "\n"):
                        self.lb.insert(END, i)  # yaml dosyasının içeriğini "lb" yani listboxa aktarıyoruz

        except Exception as e:
            print("***YAML dosyasi okurken bir hata olustu*** \n{}".format(e))


def main():
    root = Tk()
    root.geometry("450x350+300+300")
    app = Example(root)
    root.tk_setPalette("#6A0888")
    root.title("Harcama Raporu")
    root.mainloop()


main()
