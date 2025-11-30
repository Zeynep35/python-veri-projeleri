

def filtre(tarih, gider_listesi):
    liste = []
    for i in gider_listesi:
        kayit_tarihi = i["tarih"]
        if kayit_tarihi == tarih:
            assert kayit_tarihi == tarih, "tarihler eşleşmiyor."
            liste.append(i)
        
    return liste

def etiket(etiket, gider_listesi):
    liste2 = []
    for i in gider_listesi:
        kayit_etiket = i["etiket"]
        if kayit_etiket == etiket:
            liste2.append(i)
        
    return liste2

