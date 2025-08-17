
#* KEŞİFÇİ VERİ ANALİZİ

# GENEL RESİM
# Veriye ilk bakış kesinlikle önemlidir. Veri'nin ruhu ile tanışalım. İlk buluşma. 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()
df.tail() # son satırı gösterir
df.shape # boyutunu gösteriyor- boyutumuz büyük kalabalık bir geçmişi var.-
df.info() # genel info - hmm.. bazı yerlerde eksik konuşuyor age ve embarked kısmı ketum-
df.columns # kolon adları. -kolon isimlerine baktım hayat hikayesi dolu dolu-
df.index # kaç tane oldugu 
df.describe().T # tanımlayıcı istatistikler
# - ortalama yaşı 29.7 genç ama yaşanmışlıkları var. min yaşı 0.42 maksimum 80 .
# hayatın her evresinden biri olmuş. ücretler arasında uçurum var bazıları lüks bazıları
# zar zor binmiş. sosyo ekonomik çeşitlilik var.-
df.isnull().values.any() # null veri var mı?
df.isnull().sum() # hangi kolonlarada null oldugu - Eksik veriler onun sessiz alanları.
# Cabin neredeyse tamamen boş. Belki de bu onun özeli. Age kolonundaki eksikler, 
#zamanla açılacak yönleri. Her ruh gibi, bazı şeyleri hemen paylaşmıyor..

def check_df(dataframe, head = 5):
    print("#################### SHAPE ####################")
    print(dataframe.shape)
    print("#################### TYPE ####################")
    print(dataframe.dtypes)
    print("#################### HEAD ####################")
    print(dataframe.head(head))
    print("#################### TAİL ####################")
    print(dataframe.tail(head))
    print("#################### NA ####################")
    print(dataframe.isnull().sum())
    print("#################### DESCRİPTİVE ####################")
    print(dataframe.describe().T)

# kendi hazırladıgım sorularda genel çerçevede onu daha hızlı tanıdım. Bana zaman kazandırdı
# Titanic veri seti ile ilk buluşmam bana eksiklikleriyle, çeşitliliğiyle, istatistiksel karakteri
# ile tam bir roman kahramanını anımsattı.

check_df(df)
##########################################################################################################

#* KATEGORİK DEĞİŞKEN ANALİZİ

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["sex"].unique()
df["sex"].nunique()

cat_cols = [col for col in df.columns if str(df[col].dtype) in ["category","object", "bool"]]
# veri tipine göre kategorik olan sütunları buldururuz.
cat_cols

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtype in ["int","float"]]
# sayısal veri tipine sahip ama kategorik davranan sütunları buldururuz.
# unique => görselleştirme etiketleme mapping işlemlerinde çıktı int()
# nunique => kategorik mi, sayısal mı karar verirken filtreleme yaparken
num_but_cat

cat_but_car = [col for col in df.columns 
               if df[col].nunique() > 20 
               and str(df[col].dtype) in ["category", "object"]]
# katagorik olarak gözüken ama aslında çok fazla eşsiz değeri olan sütunları bulduruyoruz.
cat_but_car

cat_cols = cat_cols + num_but_cat
cat_cols

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols]

#* NELER YAPTIK?🎀 VERİ SARAYINDA SİNSİRELLAR VERSİYONU 🎀
# Veri sarayında herkes sütun gibi görünüyordu ama bazıları vardı ki... pek bir sinsiydi. İşte onlara süslü bir hitapla “Sinsirella” deniyordu 🎀
# Bazı sütunlar sayısal gibi takılıyordu (int, float) ama aslında sadece 3–5 farklı değer taşıyorlardı. Bunlar gizli kategorik Sinsirellalardı → num_but_cat.
# Bazıları ise metin tipindeydi (object, category) ama 1000 farklı değerle ortalığı karıştırıyorlardı. Bunlar da çeşidi bol, gösterişli Sinsirellalardı → cat_but_car.
# Gerçekten kategorik olanlar ise zaten kendilerini belli ediyordu → cat_cols listesinde yerlerini almışlardı. Onlar sinsi değil, sadece süslüydü.
# Sinsirellaları ayırt etmek için nunique() ile kaç farklı yüzleri olduğunu saydık, unique() ile kim olduklarını tanıdık.
# Ve böylece veri sarayında kim rol yapıyor, kim gerçekten ne — hepsi açığa çıktı. Sinsirellalar maskelerini düşürdü 🎭

def sinsirellalari_ayikla(df):
    cat_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    num_but_cat = [col for col in df.select_dtypes(include=["int", "float"]).columns 
                   if df[col].nunique() < 10]
    cat_but_car = [col for col in df.select_dtypes(include=["object", "category"]).columns 
                   if df[col].nunique() > 20]

    print(f"🎀 Gerçek kategorikler (cat_cols): {(cat_cols)} sütun")
    print(f"🕵️‍♀️ Sayısal ama gizli kategorikler (num_but_cat): {(num_but_cat)} sütun")
    print(f"🎭 Süslü ama karmaşık kategorikler (cat_but_car): {(cat_but_car)} sütun")

    return cat_cols, num_but_cat, cat_but_car

sinsirellalari_ayikla(df)

df["survived"].value_counts()
100* df["survived"].value_counts() / len(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() /  len(dataframe)}))
    print("####################################################################################")


cat_summary(df,"sex" )

for col in cat_cols:
    cat_summary(df, col)


def cat_summary(dataframe, col_name, plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() /  len(dataframe)}))
    print("####################################################################################")
    
    if plot:
        sns.countplot(x = dataframe[col_name], data = dataframe)
        plt.show(block = True)



cat_summary(df, "sex", plot=True)

for col in cat_cols:
    cat_summary(df, col, plot = True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("asliasliasliasli")
    else:
        cat_summary(df, col,plot=True)


##########################################################################################
#* SAYISAL DEĞİŞKEN ANALİZİ

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df[["age", "fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]

num_cols = [col for col in num_cols if col not in cat_cols]

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 1.00]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)

def num_summary(dataframe, numerical_col, plot = False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 1.00]
    print(dataframe[numerical_col].describe(quantiles).T)
    
    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block = True)


num_summary(df, "age", plot = True)

for col in num_cols:
    num_summary(df, col, plot=True)


########################################################################################
#* DEĞİŞKENLERİN YAKALANMASI ve İŞLEMLERİN GENELLEŞTİRİLMESİ

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
df.head()
df.info()


def grab_col_names(dataframe, cat_th = 10, car_th=20):
    """
    Veri setindeki kategorik, numeric ve kategorik fakat kardinal değişkenlerin
    isimlerini verir.
    
    PARAMETERS
    ``````````````
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numereik fakat kategorik olan değişkenler için sınıf eşik değeri.
    car_th: int, float
        kateforik fakat kardinal değişkenler için sınıf eşik değeri.
        
    RETURNS
    ````````````````
    cat_cols: List
        kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat but car: list
        kategorik görünümlü kardinal değişken listesi
    
    NOTE
    ``````````````````
    cat_cols + cum_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.
    
    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in df.columns if str(df[col].dtype) in ["category","object", "bool"]]
    
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtype in ["int","float"]]
    
    cat_but_car = [col for col in df.columns 
               if df[col].nunique() > 20 
               and str(df[col].dtype) in ["category", "object"]]
    
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]
    
    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]
    
    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")
    
    return cat_but_car , cat_cols, num_cols



help(grab_col_names)
grab_col_names(df)

# Bu fonksiyon, bir veri setindeki değişkenleri türlerine göre sınıflandırarak analiz öncesi sade bir yapı sunar. 
# Öncelikle metin, bool ya da az sayıda sınıfa sahip sayısal değişkenleri kategorik olarak tanımlar (cat_cols). 
# Ardından, gerçekten sayısal olan ve kategorik davranmayan değişkenleri ayırarak num_cols listesine ekler. 
# Eğer bir kategorik değişken çok fazla sınıfa sahipse, bu değişkenler kardinal olarak değerlendirilir ve 
# cat_but_car grubuna alınır. Fonksiyon ayrıca veri setinin kaç gözlem ve değişkenden oluştuğunu özetler. 
# Böylece değişkenlerin rolü netleşir ve sonraki analiz adımları için zemin hazırlanmış olur.

#* HEDEF DEĞİŞKEN ANALİZİ

import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
df = sns.load_dataset("titanic")
df.head()
df["survived"].value_counts()


df.groupby("sex")["survived"].mean()
# cinsiyet değişkenine göre hayatta kalan ve kalmayanların ortalamasını aldık

def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"target mean": dataframe.groupby(categorical_col)[target].mean()}))

target_summary_with_cat(df, "survived", "sex")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)


#* Sayısal değişkenler ile analiz

df.groupby("survived")["age"].mean()

# aynı işlem
df.groupby("survived").agg({"age": "mean"})


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}))

target_summary_with_num(df, "survived", "age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)

































