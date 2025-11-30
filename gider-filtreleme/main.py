from io_utils import tarih_al
from io_utils import etiket_al
from io_utils import sonuc_yaz
import calc

if __name__ == "__main__":
    
    gider_listesi =  [
        {"tarih": "28.11.2025", "etiket":"yemek"},
        {"tarih": "02.12.2025", "etiket":"market"},
        {"tarih": "25.05.2026", "etiket":"eglence"}
    ]

    t = tarih_al()
    e = etiket_al()
    

    sonuc= calc.filtre(t, gider_listesi)
    sonuc2 = calc.etiket(e, gider_listesi)

    print(f"Sonuç: {sonuc}")
    print(f"Sonuç: {sonuc2}")