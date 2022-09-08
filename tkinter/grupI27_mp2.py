import tkinter as tk
from tkinter import *
from tkinter import filedialog
import yaml


class PlotEkrani(tk.Frame):

    def __init__(self, parent, width, height):
        tk.Frame.__init__(self, parent, background="blue")
        self.parent = parent
        self.width = width
        self.height = height
        self.fill_color = "red"
        self.yazi_handles = []
        self.pack()
        self.initGui()

    def initGui(self):
        self.buton1 = tk.Button(self, text="Aktar", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.dosya_yukle)
        self.buton1.grid(row=2, column=0, sticky=W, columnspan=2,ipadx=15)
        self.buton2 = tk.Button(self, text="Secili Sil", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.secileni_sil)
        self.buton2.grid(row=2, column=1, sticky=W,columnspan=2,ipadx=10)
        self.buton3 = tk.Button(self, text="Hepsini Sil", bg="#F5A9A9", fg="purple", font="verdana 8 bold ",command=self.hepsini_sil)
        self.buton3.grid(row=2, column=2, sticky=W, columnspan=2,ipadx=9)
        self.lb = tk.Listbox(self, height=20, width=85, bg="#F6CEE3", fg="purple", selectmode="single")
        self.lb.grid(row=1, column=0, columnspan=7)
        self.canvas_bg = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas_bg.grid(row=3, column=0, columnspan=7)



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

    def bar_diagram(self, data=[90, 100, 80, 90, 100]):
        """
        Disaridan verilen yuzde degerleri icin bar diagram cizer

        Args:
            data: Liste halinde verilen yuzde degerleri
        """
        x_poses = range(0, self.width, int(self.width / len(data)))
        print(x_poses)
        x_width = x_poses[1] * 0.9

        for i, y in enumerate(data):
            # calculate reactangle coordinates (integers) for each bar
            x0 = x_poses[i]
            y1 = (100 - y) * self.height / 100
            x1 = x_poses[i] + x_width
            y0 = self.height
            print(x0, x1, y0, y1)
            # draw the bar
            self.canvas_bg.create_rectangle(x0, y0, x1, y1, fill=self.fill_color)
            # put the y value above each bar
            self.yazi_handles.append(self.canvas_bg.create_text(
                x0 + x_width / 2, y0, anchor=tk.SW, text=str(y), fill=self.fill_color))

        self.canvas_bg.bind("<Button-1>", self.button_click)
        self.canvas_bg.bind("<Enter>", self.mouse_on)
        self.canvas_bg.bind("<Leave>", self.mouse_off)

    def mouse_on(self, event):
        for yazi in self.yazi_handles:
            self.canvas_bg.itemconfig(yazi, fill="white")

    def mouse_off(self, event):
        for yazi in self.yazi_handles:
            self.canvas_bg.itemconfig(yazi, fill=self.fill_color)

    def button_click(self, event):
        posx = event.x
        posy = event.y
        self.item_handle = self.canvas_bg.find_closest(posx, posy)
        self.canvas_bg.itemconfig(self.item_handle, fill="blue")
        self.canvas_bg.tag_bind(
            self.item_handle, "<ButtonRelease-1>", self.button_released)

    def button_released(self, event):
        self.canvas_bg.itemconfig(self.item_handle, fill=self.fill_color)


def main():
    root = tk.Tk()
    root.title("Goruntu Ekrani")
    ekran_boyutlari = [600, 350]
    root.geometry("{}x{}".format(ekran_boyutlari[0], ekran_boyutlari[1]))
    plt = PlotEkrani(root, ekran_boyutlari[0], ekran_boyutlari[1])
    plt.bar_diagram([100, 90, 70, 60, 100])
    root.mainloop()

main()
