
bir_satir = int(input("birinci matrisin satir sayisini giriniz: "))
bir_sutun = int(input("birinci matrisin sutun sayisini giriniz: "))
ilk_matris = [[0 for x in range(bir_sutun)] for y in range(bir_satir)]
print("birinci matrisin degerlerini giriniz: ")
for i in range(bir_satir):
    for j in range(bir_sutun):
        ilk_matris[i][j] = int(input())
print("birinci matris")
for i in range(bir_satir):
    print(ilk_matris[i])
print()

satir2 = int(input("ikinci matrisin satir sayisini giriniz: "))
sutun2 = int(input("ikinci matrisin sutun sayisini giriniz: "))
ikinci_matris = [[0 for x in range(sutun2)] for y in range(satir2)]
print("ikinci matrisin degerlerini giriniz: ")
for i in range(satir2):
    for j in range(sutun2):
        ikinci_matris[i][j] = int(input())
print("ikinci matris")
for i in range(satir2):
    print(ikinci_matris[i])
print()

carpim_sonucu=[[0 for x in range(sutun2)]for y in range(bir_satir)]
if bir_satir != sutun2:
    print("matris carpimi yapilamaz!\nilk matrisin satiri ile ikinci matrisin sütunu eşit olmalı.")
else:
    for p in range(len(ilk_matris)):
        for q in range(len(ikinci_matris[0])):
            for r in range(len(ikinci_matris)):
                carpim_sonucu[p][q] += ilk_matris[p][r] * ikinci_matris[r][q]
    print("iki matrisin carpimi:")
    for i in range(bir_satir):
        print(carpim_sonucu[i])


