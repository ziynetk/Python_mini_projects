birler_b = ["", "bir", "iki", "uç", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
onlar_b = ["", "on", "yirmi", "otuz", "kirk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
yuzler_b = ["", "yuz", "iki yuz", "uc yuz", "dort yuz", "bes yuz", "alti yuz", "yedi yuz", "sekiz yuz", "dokuz yuz"]
binler_b=["","Bin","Iki bin","Uc bin","Dort bin","Bes bin","Altı bin","Yedi bin","Sekiz bin","Dokuz bin"]

def yaziya_cevir(number):
    print("programi sonlandirmak icin 'cikis' girmeniz yeterlidir.")
    while(number!=-1):
        number = input("bir sayi giriniz: ")
        if number == str("cikis"):
            number=-1
        else:
            binler = int(number) //1000
            yuzler = (int(number)-(binler*1000)) // 100
            onlar  = (int(number)-((yuzler*100)+(binler*1000)))//10
            birler = int(number) %10
            print(binler_b[binler]+yuzler_b[yuzler]+" "+onlar_b[onlar]+" "+birler_b[birler])


    print("Program sonlanıyor...")
number=0
yaziya_cevir(number)

