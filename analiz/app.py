liste = [-99, 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,556,17,18,19,20,67,21,22,23,24,25,-7]

def ortalama_hesapla(liste):
    ortalama = sum(liste)/len(liste)
    return ortalama

def medyan_hesapla(liste):
    sirala = sorted(liste)
    veri_sayisi = len(sirala)
    orta = veri_sayisi // 2

    if veri_sayisi % 2 == 1:    # eleman sayısı tek ise
        return sirala[orta] 
    else:
        return (sirala[orta-1] + sirala[orta]) / 2

def ceyrek_bul(veri):
    sirala = sorted(veri)
    veri_sayisi = len(sirala)
    orta = veri_sayisi // 2

    # Alt ve üst yarıyı bul
    if veri_sayisi % 2 == 1:
        alt_yari = sirala[:orta]       # ortadaki eleman hariç
        ust_yari = sirala[orta+1:]
    else:
        alt_yari = sirala[:orta]
        ust_yari = sirala[orta:]

    # Q1 ve Q3
    Q1 = medyan_hesapla(alt_yari)
    Q3 = medyan_hesapla(ust_yari)

    # IQR
    IQR = Q3 - Q1

    # Eşikler
    alt_esik = Q1 - 1.5 * IQR 
    ust_esik = Q3 + 1.5 * IQR

    # Uç noktaları bulalım
    outlier_liste = []

    for i in sirala:
        if i < alt_esik or i > ust_esik:
            outlier_liste.append(i)
    
    return Q1, Q3, IQR, alt_esik, ust_esik, outlier_liste


ortalama = ortalama_hesapla(liste)
medyan = medyan_hesapla(liste)

Q1, Q3, IQR, alt_esik, ust_esik, outlier_liste = ceyrek_bul(liste)

print("Sıralı liste : ", sorted(liste))
print("Ortalama     : ", ortalama)
print("Medyan       : ", medyan)
print("Q1           : ", Q1)
print("Q3           : ", Q3)
print("IQR          : ", IQR)
print("Alt eşik     : ", alt_esik)
print("Üst eşik     : ", ust_esik)
print("Uç değerler  : ", outlier_liste)
