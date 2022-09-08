latin_alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def sifre_cozum(sifrecozum):
    cozum = " "
    for i in sifrecozum:
        if (i==" "): #şifreli metni girerken boşluk koyarsak hatayı engelliyor
            continue
        cozum+=latin_alf[(latin_alf.index(i)-n)%len(latin_alf)] #liste biterse başa donmesi için mod alıyoruz
    print("girilen metinin sifresinin cozulmus hali :",cozum)
    return sifrecozum

def sifreleme(text):
    sifre = " "
    for i in text:
        if (i==" "): #şifrelemek istediğimiz metni girerken boşluk koyarsak hatayı engelliyor
            continue
        sifre+=latin_alf[(latin_alf.index(i)+n)%len(latin_alf)] #liste biterse başa donmesi için mod alıyoruz
    print("girilen metinin sifrelenmis hali :",sifre)
    return text
n=int(input("sifrelemek istediginiz N degerini giriniz: "))
text= input("sifrelemek istediginiz metni giriniz:")
sifreleme(text)
sifrecozum=input("sifresini cozmek istediginiz metni giriniz: ")
sifre_cozum(sifrecozum)

n=int(input("sifrelemek istediginiz N degerini giriniz:"))
text=input("sifrelemek istediginiz metni giriniz:")
sifreleme(text)
sifrecozum=input("sifresini cozmek istediginiz metni giriniz:")
sifre_cozum(sifrecozum)


