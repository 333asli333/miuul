
#* NUMPY & PANDAS

# *NUMPY
# Numpy python listelerine kıyasla hızlı çalısır.
# Vektörel işlemler yapmayı sağlıyor.
# Çok boyutlu array (dizi) işlemlerini kolaylaştıran bir bilimsel kütüphane.
# Kısacası daha az çabayla daha fazla iş yaptırır.

#* NEDEN NUMPY?
import numpy as np

# klasik yöntem ile bu sekilde
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])
print(ab)

# Numpy ile bu şekilde
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b

# sonuç olarak daha az efor daha cok verim. akıllı çalışma.

#* NUMPY ARRAY OLUŞTURMAK

import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype = int) 
# girilen sayı adedince 0 olusturuyor.

np.random.seed(36)
# tutarlı sonuclar almak için

np.random.randint(0, 10, size = 10)
# 0 dan 10 a kadar rasgele sayılar olusturduk.

np.random.normal(10, 4, (3, 4))
# ortalaması 10 standart sapması 4 olan array olusturduk.
np.linspace(0, 1, 5)
# 0 ile 1 arasında eşit aralıklı 5 sayı üretiyor.
import numpy as np

a = np.random.randint(10, size = 5)
# 10 yanına bir sey yazmadıgım için bunu otomatik olarak 0 alıcak

a.ndim
# boyut sayısı

a.shape
# boyut bilgisi

a.size
# toplam eleman sayısı

a.dtype
# array veri tipi

#* YENİDEN ŞEKİLLENDİRME

np.random.randint(1,10, size= 9)
np.random.randint(1,10,  size = 9).reshape(3,3)
# boyutunu değiştiriyoruz.

####################################################
#* INDEX SECİMİ
####################################################

a = np.random.randint(10, size = 10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10,  size = (3, 5))
m
m[0,0] # 0'ıncı sütun 0'ıncı satır
m[1,1]

m[:, 0] # 0'ıncı sütun da olan sayıları çekelim

m[1, :]# 1. ci satırda olan sayıları cekelim

# ! PYTHONDA SAYILAR HER ZAMAN 0 DAN BASLAR !

#* fancy index 

v = np.arange(0, 30, 3)
# 0 dan 30 a kadar 3 er sekilde array olustur.
v[1]

catch = [1,2,3]
v[catch]

# v numpy array de 0'dan 30' a kadar sayılar var
# cath bir liste 
# bu ikisini birleştirince magic oluyor
# numpy array de olan 1. 2. 3. olan elemanları cağırıyoruz.

##################################################################
# eğer büyük verilerde çağırılıcak olsaydı
v1 = np.arange(0, 1000, 3)
catch1 = [ i for i in range(0, len(v1), 100)]
catch1

##################################################################
#* NUMPY'DA KOŞULLU İŞLEMLER
##################################################################



import numpy as np
v = np.array([1,2,3,4,5])
v < 3 # TRUE ve FALSE OLUSAN BİR ÇIKTIN OLUR.
v[v < 3] # şartı sağlayan elemanları getirir.
# klasik döngü
ab = []

for i in v:
    if i < 3:
        ab.append(i)

print(ab)


#* MATEMATİKSEL İŞLEMLER
import numpy as np
v = np.array([1,2,3,4,5])

v / 5 # hepsi bu sekilde işlem görebilir.

np.subtract(v, 1) # çıkarma işlemi
np.add(v, 1) # toplama işlemini gerçekleştirdi
np.mean(v) # ortalamasını aldık
np.sum(v) # toplama işlemi
np.min(v) # min değer
np.max(v) # maksimum değer
np.var(v) # varyansını aldık
np.std(v) # standart sapma

#* iki bilinmeyenli denklem çözümü
# 5*x0 + x1 = 12
# x0 + 1*x1 = 10

a  = np.array([[5,1], [1,3]])
b = np.array([12, 10])

np.linalg.solve(a,b)


################################################################
#* PANDAS

# Veri yapılarına kolayca yönetmek için kullanılır.
# data frameler ve series gibi özel veri yapıları sunar.

import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)
# veri tipinin yapısını bilmek çıktılarda,
# hata alındıgında hızlı bir şekilde anlayabiliriz

s.index # index sayısı?
s.dtype # içerideki verinin tip bilgisini verir.
s.size # eleman sayısı
s.ndim # boyut
s.values # içindekiler gösteriyor
type(s.values)

# pandas da indexler ilk kodun çıktısı gibi. yanında defaulte olarak yer alır
# fakat biz s.values yazdıgımızda indexler ile ilgilenmediğimiz için numpy 
# array olarak karşımıza gelmektedir.

s.head(3) # ilk üç gözlem
s.tail(3) # son üç gözlem


df = pd.read_csv(r"C:\Users\TORUN\Desktop\miuul_calisma\InsPostComparison.csv")
df.head()

import seaborn as sns

df1 = sns.load_dataset("titanic")
df1.head 
df1.shape
df1.info()
df1.index # sayısı
df1.describe().T  # tanımlayıcı istatistikler
df1.isnull().values.any() # NULL veri var mı?
df1.isnull().sum() # NULL verinin toplamı nedir?

#* SEÇİM İŞLEMLERİ
df1["sex"].head() # seçilen değişkenin ilk 5'i
df1[0:13]
df1.drop(0, axis = 0).head() # seçilen değişkeni(burada 0 ı seçtik)sikme işlemi
# axis = 0 satırlar üzerinden işlem yap, axis = 1 ise sütunlar üzerinden

print(df1.columns) # kolon isimleri

#* DEĞİŞKENİ İNDEX CEVİRMEK
df1["age"].head()
df1.age.head()# aynı işlem

df1.index = df1["age"] # indexe cevirildi

df1.drop("age", axis = 1).head()
df1.drop("age", axis = 1, inplace = True)

#* İNDEXİ DEĞİŞKENE ÇEVİRMEK
df1.index

df1["age"] = df1.index

df1.head()
df1.drop("age", axis = 1, inplace= True)

df1.reset_index(inplace= True) # indexlere reset atıp eski haline getirdik.

delete_indexes = [1,3,5,7]
df1.drop(delete_indexes, axis = 0).head(10)
# ! ATAMA YAPILMADIĞI İÇİN KALICI DEĞİLDİR ANCAK 
# drop(delete_indexes, axis = 0, inplace =TRUE)
# ! YAPILIRSA O ZAMAN DA İŞLEM KALICI OLUCAKTIR!

#* DEĞİŞKENLER ÜZERİNDE İŞLEMLER

pd.set_option("display.max_columns", None)
# bütün kolonları göster demektir.

"age" in df1
type(df1["age"].head()) # tek boyutlu veri dizisi (liste gibi ama indexli)

type(df1[["age"]].head()) # burada data frame olarak alıyoruz. iki boyutlu tablo

df1[["age", "alive"]] # dataframe olarak iki değişkenin seçimi

col_names = ["age", "adult_male", "alive"]

df1.drop(col_names, axis=1).head()

df1[col_names]

df1["age2"] = df1["age"]**2
df1["age3"] = df1["age"] / df1["age2"]

#* İLOC: İNTEGER BASED SELECTİON
# satır sütun koumunu biliyorsan
# her zaman integer based 
df1.iloc[0:3] # 3. satırı dışlar.
df1.iloc[0,0]

df1.iloc[0:3, "age"] # ! hata integer kabul ede sadece
df1.iloc[0:3, 0:3]

#* LOC: LABEL BASED SELECTİON
# etiketli veri ile çalısıyorsan, satır sütun adı varsa
df1.loc[0:3] # 3. satırı da dahil eder

df1.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df1.loc[0:3, col_names] # çoklu seçim


############################################################
#* KOŞULLU SEÇİM
############################################################

df1[df1["age"] > 50].head()
df1[df1["age"] > 50]["age"].count() 

df1.loc[df1["age"] > 50, ["age", "class"]].head()
df1.loc[(df1["age"] > 50) & (df1["sex"] == "female"),["age", "class", "sex"]].head()
#! 2 AYRI KOŞUL VARSA BUNLARI PARANTEZ İÇERİSİNE ALIYORUZ!
# YANDAKİ BLOK İSİMLERİNİ GÖRMEMİZİ SAĞLIYOR ["age", "class", "sex"]


#######################################################################
#* TOPLULAŞTIRMA VE GRUPLAMA (Aggregation & Grouping)
#######################################################################
import pandas as pd
import seaborn as sns 
pd.set_option("display.max_columns", None) # bütün kolonları alalım
df = sns.load_dataset("titanic") # bu sefer df'ye aldım daha rahat olur diye
df.head() # ilk beş 

df["age"].mean()

df.groupby("sex")["age"].mean() # cinsiyete göre yaş ortalamaları

df.groupby("sex").agg({"age": "mean"}) # yukarıdakinin aynısı

df.groupby("sex").agg({"age": ["mean", "sum"]}) # cinsiyete göre yaşın ortalması
# ve toplamı - ikisinin birlikte yazılımı liste şeklindedir her zamannn----

df.groupby(["sex", "embark_town"]).agg({ "age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(["sex","embark_town", "class"]).agg({"age": ["mean"],
                                                "survived": "mean"})
df.groupby(["sex","embark_town", "class"]).agg({"age": ["mean"],
                                                "survived": "mean",
                                                "sex": "count"})

#* PİVOT TABLE

df.pivot_table("survived","sex", "embarked")
# hücrelerin kesişimi defaultta mean olarak yer alır
# ilk yazılan ort değer ("survived")
# ikinci yazılan satır ("sex")
# üçüncü yazılan sütun ("embarked")

df.pivot_table("survived","sex", "embarked", aggfunc = "std")
# bu sekilde standart sapma bilgisine de erişim sağlayabilirsin.

df.pivot_table("survived","sex", ["embarked", "class"])
# her sütun bir kombinasyon ["embarked", "class"]

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
# pd.cut bunu çeyreklere göre ayır demek qcut ise otomatik çeyreklere göre ayırır
# yukarıda kinde kendimiz ayırdık

df.pivot_table("survived", "sex", "new_age")

df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option("display.width", 500) # okunabilirlik adına yan yana dizilmesi için


#* APPLY ve LAMBDA

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10
        

df[["age","age2","age3"]].apply(lambda x: x/10).head()
# çift [[]] birden fazla sütun seçmek için
# lambda döngü gibi davranır ve o işlemi uygular.
# tek satırda kod yazmanı sağlar.

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()
# loc ile satır ve sütun seçimi yapılır 
# : diğer tüm satırlar demektir
# df.columns.str.contains bu içinde age olanları bulur
df.loc[:, df.columns.str.contains("age") & (df.columns != "new_age")].apply(
    lambda x: (x - x.mean()) / x.std()).head()


df.loc[:, df.columns.str.contains("age")].dtypes

#* lambda dısında da klasik fonksiyonlarla kullanmak için

def standar_scaler(col_name):
    return(col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age") 
       & (df.columns != "new_age")].apply(standar_scaler).head()

#* ATAMA İŞLEMİ İÇİN
df.loc[:, df.columns.str.contains("age") & (df.columns != "new_age")] = df.loc[:, df.columns.str.contains("age") 
       & (df.columns != "new_age")].apply(standar_scaler).head()


##############################################################################
#* BİRLEŞTİRME İŞLEMLERİ (JOIN)
##############################################################################

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5,3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2], ignore_index=True)
# concat metodu data frameleri birleştirir 


















