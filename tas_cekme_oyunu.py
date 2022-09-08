def tas_cikarma_oyna(toplam_tas_adedi, max_tas):
    while (toplam_tas_adedi>0):
        a=int(input("1.OYUNCU-çıkaracağınız taş adedini giriniz: "))
        if (a>5 or a<=0):
            print("kalan taş adedi=",toplam_tas_adedi)
            while(a>5 or a<=0):
                print("Lütfen 1 ile 5 arasında sayı giriniz.Tekrar deneyiniz...")
                a = int(input("1.OYUNCU-çıkaracağınız taş adedini giriniz: "))
            toplam_tas_adedi -= a
            if (a == toplam_tas_adedi):
                toplam_tas_adedi -= a
                print("*****TEBRİKLER!*****\n1.OYUNCU KAZANDI!")
                print("kalan taş adedi =", toplam_tas_adedi)
        elif a > toplam_tas_adedi:
            print("Geçersiz Hamle. Tekrar deneyiniz...")
            print("kalan taş adedi=",toplam_tas_adedi)
            while (a > toplam_tas_adedi):
                a = int(input("1.OYUNCU-çıkaracağınız taş adedini giriniz: "))
            toplam_tas_adedi -= a
            if (a == toplam_tas_adedi):
                toplam_tas_adedi -= a
                print("*****TEBRİKLER!*****\n1.OYUNCU KAZANDI!")
                print("kalan taş adedi =", toplam_tas_adedi)
        elif a == toplam_tas_adedi:
            toplam_tas_adedi -= a
            print("*****TEBRİKLER!*****\n1.OYUNCU KAZANDI!")
            print("kalan taş adedi =",toplam_tas_adedi)
            break
        else:
            toplam_tas_adedi -= a
            print("kalan taş adedi =",toplam_tas_adedi)
        #2.oyuncu
        a = int(input("2.OYUNCU-çıkaracağınız taş adedini giriniz: "))
        if (a>5 or a<=0):
            print("Lütfen 1 ile 5 arasında sayı giriniz.Tekrar deneyiniz...")
            print("kalan taş adedi =",toplam_tas_adedi)
            while (a > 5 or a <= 0):
                a = int(input("2.OYUNCU-çıkaracağınız taş adedini giriniz: "))
            toplam_tas_adedi -= a
            if (a == toplam_tas_adedi):
                toplam_tas_adedi -= a
                print("*****TEBRİKLER!*****\n2.OYUNCU KAZANDI!")
                print("kalan taş adedi =", toplam_tas_adedi)
        elif a > toplam_tas_adedi:
            print("Geçersiz Hamle. Tekrar deneyiniz...")
            print("kalan taş adedi =",toplam_tas_adedi)
            while (a > toplam_tas_adedi):
                a = int(input("2.OYUNCU-çıkaracağınız taş adedini giriniz: "))
            toplam_tas_adedi -= a
            if (a == toplam_tas_adedi):
                toplam_tas_adedi -= a
                print("*****TEBRİKLER!*****\n2.OYUNCU KAZANDI!")
                print("kalan taş adedi =", toplam_tas_adedi)
        elif a == toplam_tas_adedi:
            toplam_tas_adedi -= a
            print("*****TEBRİKLER!*****\n2.OYUNCU KAZANDI!")
            print("kalan taş adedi =",toplam_tas_adedi)
            break
        else:
            toplam_tas_adedi -= a
            print("kalan taş adedi =",toplam_tas_adedi)
tas_cikarma_oyna(100,5)


