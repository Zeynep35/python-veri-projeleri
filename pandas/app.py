import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import sqlite3 

#titanic verisetini yüklüyoruz
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv") #verisetimizi yüklüyoruz.
print(df.head())

deneme = pd.pivot_table(df, index="Pclass", columns="Survived", values="Fare", aggfunc='mean') #Pivot tablo oluşturma. Argümanlar farklı olabilir.
print(deneme)

deneme = deneme.fillna(0) #boş veri varsa 0 yapıyoruz. 
print(deneme)

yas = df["Age"] #yaş sutununu seçiyoruz. 

yas_kucuk = df[df["Age"] < 18] #tabloda yaşı 18'den küçükleri seçiyoruz. 

secim = df[["Survived","Fare"]]  #çift sutun seçim örneği.

index_yeri = df.iloc[3] #İndex lokasyona göre 3. satırı çağırıyoruz. 0'dan başlar saymaya o yüzden 4. satırı seçer.
print(index_yeri)

df["Name"] = df["Name"].astype(str) #tip dönüşümü örneği.

yas.plot(kind="hist") #histogram grafiği çizdirme. 
plt.show()

yas_kucuk["Age"].plot(kind="line") #çizgi grafik.
plt.show()

connection_obj = sqlite3.connect('titanic.db') #veritabanına bağlanıyoruz. Eğer titanic.db varsa bağlantı kurar yoksa kendi oluşturur.

cursor_obj = connection_obj.cursor() #sql'e komut verdiğimizde çalışmasını sağlayan cursor.

cursor_obj.execute("DROP TABLE IF EXISTS TITANIC") #Eğer titanic tablosu varsa sil yoksa hata vermeden devam et. 

#tablo özelliklerini tanımlıyoruz.
table_creation_query = """   
    CREATE TABLE titanic (
        passengerID INTEGER NOT NULL,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(25),
        Score INT
    );
"""

cursor_obj.execute(table_creation_query) #tablonun çalışmasını sağlar.

print("TABLO")

connection_obj.commit() #yapılan değişiklikleri kaydet demek. 
connection_obj.close() #Veritabanını kapatır. 
