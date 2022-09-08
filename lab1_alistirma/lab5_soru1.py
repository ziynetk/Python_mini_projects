import re
def lab5_soru1_sorua_cozum1(deneme):#for döngüsü ve if kullanarak çözüm

    s = '' 
    for k in deneme:

        if k == "_":
            s += ''
        else:
            s+= k
    print(s.lower())




def lab5_soru1_sorua_cozum2(deneme): #list/dictionary comprehension ile çözüm

    result = re.sub(r'_',  '',   deneme).lower()
    print(result)





def  lab5_soru1_sorub_cozum1(x): #for döngüsü ve if kullanarak çözüm
    for i in x:
        if (i % 2 == 0):
            print("{}: cift".format(i),end=" ")
        else:
            print("{}: tek".format(i),end=" ")

    print("\n")



def  lab5_soru1_sorub_cozum2(x): #list/dictionary comprehension ile çözüm
    tek_cift = {"{}: cift".format(i) if i % 2 == 0 else "{}: tek".format(i) for i in x}
    print(tek_cift)


