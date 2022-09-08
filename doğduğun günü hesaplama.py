def tarih_bulma():
    sozluk={0:"Pazar",1:"Pazartesi",2:"Salı",3:"Çarşamba",4:"Perşembe",5:"Cuma",6:"Cumartesi"}
    sozluk2={1:"Ocak",2:"Şubat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}
    sozluk3={"Ocak":0,"Şubat":3,"Mart":3,"Nisan":6,"Mayıs":1,"Haziran":4,"Temmuz":6,"Ağustos":2,"Eylül":5,"Ekim":0,"Kasım":3,"Aralık":5}
    gün=int(input("Lütfen gününü giriniz:"))
    ay=int(input("Lütfen ayı giriniz:"))
    ay=sozluk2[ay] ##ay tarihinin isme dönüşmesi
    ay_kodu = sozluk3[ay] ##ay isminin ay koduna dönüşmesi
    yıl=input("Lütfen yıl giriniz:")##son iki haneyi str alıp sonra hepsi int olucak.
    yıl_2=yıl[2:4]
    yıl_2=int(yıl_2)
    yıl=int(yıl)
    if yıl >= 1700 and yıl < 1800 : ## Yuzyıl kodu bulunuyor
              yuzyıl=4
    elif yıl >= 1800 and yıl < 1900 :
            yuzyıl=2
    elif yıl >= 1900 and yıl < 2000 :
            yuzyıl=0
    elif yıl >= 2000 and yıl < 2100 :
            yuzyıl=6
    elif yıl >= 2100 and yıl < 2200 :
            yuzyıl=4
    elif yıl >= 2200 and yıl < 2300 :
            yuzyıl=2
    elif yıl >= 2300 and yıl < 2400 :
            yuzyıl=0
    yıl_kodu=(yıl_2 + (yıl_2 // 4) % 7)
    if yıl % 400 ==0: ##sayının artık yıl mı değil mi kontrolü yapılıyor.
        artık_yıl=1
    elif yıl % 4 == 0 :
        if yıl % 100==0:
            artık_yıl=0
        else:
            artık_yıl=1
    else:
        artık_yıl=0
    if artık_yıl ==1:
        if ay == "Ocak" or ay=="Şubat":
            pass
        else:
            artık_yıl=0
    gun_numarası=((yıl_kodu + ay_kodu +yuzyıl + gün - artık_yıl) % 7)
    print("Günü:"+sozluk[gun_numarası])
tarih_bulma()
