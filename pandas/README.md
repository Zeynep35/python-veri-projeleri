## Titanic Veri Analizi ve SQLite Çalışması
Bu proje, Titanic veri seti üzerinde temel veri analizi, görselleştirme ve SQLite veritabanı işlemlerini içeren bir Python uygulamasıdır.

Proje; pandas, numpy, matplotlib ve sqlite3 kütüphanelerini kullanmaktadır.

 # Projede Yapılan İşlemler

**Veri Setinin Yüklenmesi

Titanic veri seti GitHub üzerinden okunmuştur.

İlk birkaç satır görüntülenmiştir.

**Pivot Tablo Oluşturma

Aşağıdaki kırılıma göre pivot tablo oluşturuldu:

index = Pclass

columns = Survived

values = Fare

aggfunc = mean

Bu tablo, farklı sınıflarda yolcuların hayatta kalma durumuna göre ortalama bilet ücretlerini inceler.

**Boş Verilerin Düzenlenmesi

Pivot tablo içerisindeki boş değerler (NaN), 0 ile doldurulmuştur.

**Veri Seçme İşlemleri

Age sütunu seçildi.

18 yaş altı yolcular filtrelendi.

Survived ve Fare çift kolon olarak seçildi.

DataFrame içinden belirli satır (iloc) çekme örneği gösterildi.

**Tip Dönüşümü

Name değişkeni string (metin) tipine dönüştürüldü.

**Görselleştirme

Yolcuların yaş bilgisi için histogram çizildi.

18 yaş altı yolcular için line chart oluşturuldu.

**SQLite Veritabanı İşlemleri

titanic.db adlı veritabanına bağlantı sağlandı.

Eğer varsa mevcut TITANIC tablosu silindi.

Yeni bir tablo oluşturuldu:

commit() ile değişiklikler kaydedildi ve bağlantı kapatıldı.

## Kullanılan Kütüphaneler

pandas
numpy
matplotlib
sqlite3

# Çalıştırmak İçin
1.Python 3.x kurulu olmalı.

2.Terminal veya IDE üzerinden:

bash ```
python app.py
```

3.Çalışan kod:

Konsola analiz çıktıları verir,

Grafikleri gösterir,

titanic.db dosyasını proje klasörüne oluşturur.

# Proje Amaçları

Pandas ile veri manipülasyonu öğrenmek

Pivot tablolar ile gruplama ve özetleme yapmak

Matplotlib ile grafik çizmek

SQLite ile temel veritabanı işlemlerini uygulamak

Veri bilimi çalışmalarında Python + SQL birlikte kullanmayı göstermek

#Geliştiren

Zeynep Koç
Python · Veri Bilimi · SQL