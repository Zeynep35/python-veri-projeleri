

def tarih_al():
    beklenilen_tarih = input("Hangi tarih için işlem yapmak istiyorsunuz: (gün, ay, yıl şeklinde giriniz.)")
    assert beklenilen_tarih != "", "Tarih boş olamaz"
    return beklenilen_tarih

def etiket_al():
    etiket_kategorisi = input("Hangi etiket için işlem yapmak istiyorsunuz: (yemek, market, eglence)")
    assert etiket_kategorisi in ["yemek", "market", "eglence"], "Kategori hatası."
    return etiket_kategorisi

def sonuc_yaz(sonuc, sonuc2):
    print(f"Tarih: {sonuc} ")
    print(f"Etiket: {sonuc2} ")

