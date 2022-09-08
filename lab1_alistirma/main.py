import re
from lab5_soru1 import lab5_soru1_sorua_cozum1
from lab5_soru1 import lab5_soru1_sorua_cozum2
from lab5_soru1 import lab5_soru1_sorub_cozum1
from lab5_soru1 import lab5_soru1_sorub_cozum2
from lab5_soru2 import lab5_soru2

def main():
    print("1. soru a şıkkı 1. çözümü: ",end=" ")
    lab5_soru1_sorua_cozum1("Deneme_Yazimi")
    print("1. soru a şıkkı 2. çözümü: ",end=" ")
    lab5_soru1_sorua_cozum2("Deneme_Yazimi")
    print("1. soru b şıkkı 1. çözümü: ",end=" ")
    lab5_soru1_sorub_cozum1([2, 3, 5, 7, 10])
    print("1. soru b şıkkı 2. çözümü: ",end=" ")
    lab5_soru1_sorub_cozum2([2, 3, 5, 7, 10])
    
    listt = ["MukemmelDegisken", "buNasilDegisken", "degisken2Ismi", "degiskenIsmi2", "yilan_degisken",
             "yilan_2degisken", "yilan_degisken3", "SonucDegiskeni3", "HTTPCevabi"]
    print("2. soru çözümü: ")
    lab5_soru2(listt)

main()
