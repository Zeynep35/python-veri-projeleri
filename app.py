print("Hoşgeldiniz..")

urunler =[]

def urun_ekle():    #kullanıcıdan önce ürün ismi ve tutarını öğreniyoruz.
    while True:     #Kullanıcı q demediği süre boyunca ürün giriş isteği aktif olur.
        urun_adi = input("Ürünün ismini yazınız lütfen: (Çıkış yapmak için q'ya basınız.)")
        if urun_adi == "q":   #kullanıcı "q" derse
            break #döngüden çıkar.
        tutar = int(input("Ürünün tutarını giriniz lütfen: "))

        urun = {            #kullanıcının gireceği bilgilerini saklama yöntemini belirtiyoruz.
            "ad" : urun_adi,
            "tutar": tutar
        }


        urunler.append(urun)  #yeni ürün olduğu zaman listeye ekleme yapıyor.
        print(urunler)



def liste_gor():
    print(urunler)  #listeyi görüntüler.

def toplam_tutar():
    tutarlar = [urun["tutar"] for urun in urunler] #tutar değerlerini bulma adımı.
    toplam = 0
    for i in tutarlar:
        toplam += i  #bulunan tutarlar toplama ekleniyor.
    return toplam    #sonuç döndürülüyor.

def medyan_hesapla():
    tutarlar = [urun["tutar"] for urun in urunler]
    tutarlar.sort()  #medyan almak için önce tutarlar listesini sıralıyoruz
    u = len(tutarlar) #listenin uzunluğu alnıyor.
    if u == 0:
        print("Liste boş, henüz hesaplama yapılamaz.")
        return
    elif u % 2 == 1:  #medyan hesaplaması yapılıyor.
        medyan = tutarlar[u//2]
    else:
        medyan = (tutarlar[u//2-1] + tutarlar[u//2]) / 2
    print(f"Medyan: {medyan}")

def ortalama_hesapla():
    if len(urunler) == 0:
        print("Liste boş, henüz hesaplama yapılamaz.")
        return
    ortalama = toplam_tutar() / len(urunler) #ortalama hesaplaması
    print(f"Ortalama: {ortalama}")

def menu():
   while True:
        print("""

        0. Ürün Ekleyin.
        1. Listeyi Görün.
        2. Ürünlerin toplamını hesapla.
        3. Ürünlerin medyanını hesapla.
        4. Ürünlerin ortalamasını hesapla.
        5. Çıkış
        
        """)
    
        islem = input("Yapmak istediğiniz işlemi seçiniz: (0/5)")
        if islem == "0":
            urun_ekle()
        elif islem == "1":
            liste_gor()
        elif islem == "2":
            print(f"Tüm ürünlerin toplam tutarı: {toplam_tutar()} TL")  
        elif islem == "3":
            medyan_hesapla()    
        elif islem == "4":
            ortalama_hesapla()
        elif islem == "5":
            print("Hoşçakalın")
            break
        else:
            print("Hatalı işlem. Lütfen yapmak istediğiniz işlemi seçiniz!")

if __name__ == "__main__":
    menu()

            