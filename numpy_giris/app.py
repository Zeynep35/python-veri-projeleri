import random

#liste = list(range(20))
#print(liste)

gider_listesi = []

etiketler = ["yemek","market","eglence"] #kategori başlıkları belirleme.


for i in range(20):
    gun = random.randint(1,28)  #rastgele gün seçimi. 
    ay = random.randint(1,12)   #rastgele ay seçimi.
    yil = random.choice(["2023","2024","2025"]) ##rastgele yıl seçimi.
    tarih = f"{gun:02d}.{ay:02d}.{yil}" 

    etiket = random.choice(etiketler) #yeni kategori başlığını etiket listesinden seçip rastgele üretiyor.
    tutar = random.randint(40,1000) #Belirlenen aralıktan rastgele tutar belirliyor.

    gider = {            #gider oluşturma formatını belirliyoruz.
        "tarih": tarih,
        "etiket": etiket,
        "tutar": tutar
    }            

    gider_listesi.append(gider)  #listeye yeni bir gider geldiğinde ekler. 

def ortalama_hesapla(tutar_bilgisi):   #ortalama hesaplatıyouz. 
    return sum(tutar_bilgisi) / len(tutar_bilgisi)
    

def std_hesapla(tutar_bilgisi):   #standart sapma hesaplatıyoruz.
    ortalama = ortalama_hesapla(tutar_bilgisi)
    fark_karesi = [(x - ortalama) ** 2 for x in tutar_bilgisi]
    standart_sapmasi = (sum(fark_karesi)/len(fark_karesi)) ** 0.5
    return standart_sapmasi

def percentile_hesapla(tutar_listesi):  #yüzdelik hesaplatıyoruz.
    sirali=sorted(tutar_listesi)
    uzunluk = len(sirali)

    p25_index = int(uzunluk * 0.25)
    p50_index = int(uzunluk * 0.50)
    p75_index = int(uzunluk * 0.75)

    p25 = sirali[p25_index]
    p50 = sirali[p50_index]
    p75 = sirali[p75_index]

    return p25,p50,p75

tutar_bilgisi = [x["tutar"] for x in gider_listesi] #gider listesi içinden tutar verisini çekiyoruz.

print("Ortalama:",ortalama_hesapla(tutar_bilgisi))
print("Standart Sapması:",std_hesapla(tutar_bilgisi))
print("Yüzdelik Hesaplaması:",percentile_hesapla(tutar_bilgisi))


