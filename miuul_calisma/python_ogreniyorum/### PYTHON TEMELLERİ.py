### PYTHON TEMELLERİ
############################

print("Hello, AI Era")

type("hello")
type(33.44)

## * VERİ YAPILARI*
# Integer (sayı)
x = 33
type(x)

# Float (sayı)
y = 33.34
type(y)

# Complex (sayı)
z = 8j + 15
type(z)

# Boolean
b = True
type(b)

c = 23 < 22
print(c)
type(c)
# çıktısı true ya  da false olanlarda boolean

# * LİSTELER
l = [1,2,3,4, "string", 3.2, False]
type(l)

meyveler = ["elma", "muz", "kiraz"]
meyveler.append("mandalina") # * öğe ekleme
meyveler[0] = "çilek" # * öğe değiştirme
print(meyveler)

# ögeleri belirli bir sırada tutmak için kullanılır.
# veri ekleme, silme, değiştirme işlemlerinin yapıldığı durumlar
# alışveriş listesi, öğrenci notu gibi
# * sıralıdır, kapsayıcıdır , değiştirilebilir.


#* SÖZLÜK DİCTİONARY
d = {"name": "jake",
     "age": [27, 56],
     "adress": "downtown"}
type(d)

kisi = {"ad": "asli", "soyad": "su", "yas": 21}
kisi["sehir"] = "İzmir" #* yeni anahtar çifti ekleme
kisi["yas"] = 23 #* değer değiştirme
print(kisi["ad"]) 
print(kisi)
# verilerin anahtar-değer ilişkisi ile depolamak
# anahtarlar benzersiz olmalıdır. 
# her anahtar sadece 1 kere kullanılır.
# hızlı arama ve erişim için
# bir kişinin bilgileri(ad, soyad, yaş)
#* değiştirilebilr, kapsayıcı, sırasız, key değerleri farklıdır.

#*TUPLE
t = ("Machine learning", "Data Science")
type(t)
t
# sabit kalması gereken veri koleksiyonlarında, 
# fonk birden fazla değer döndürmek için 
# sözlük anahtarı olarak kullanılır değiştirelemediği için
# rengin rgb kodu, konum kordinatları gibi
#* değiştirilemez, kapsayıcı, sıralı

# *SET
s = {"PYTHON", "MACHİNE LEARNİNG", "DATA SCİENCE", "PYTHON"}
type(s)
print(s)

sayilar = {1,2,3,4,5,2}
print(sayilar) #* 2 tekrar etti ve kaldırıldı.
sayilar.add(6) #* eklendi
sayilar.remove(1) #*silindi
print(sayilar)
#bir koleksiyonda yinelenen ögeleri kaldırır
#belirli ögelerin varlıgını hızlıca kontrol etmemizi sağlar
#matematiksel küme işlemleri yapılabilir.
#bir filmdeki aktörler gibi
#* değiştirilebilir sırasız ve eşsiz kapsayıcı


#* KARAKTER DİZİLERİ (STRİNGS)

# *çok satırlı karakter dizileri

long_str = """ veri yapıları ve tipleri:
int, float, complex, -> sayılar
str -> karakter dizisi
list, tuple, set, dict -> kolaksiyonlar
bool -> mantıksal değer
"""
print(long_str)

long_str[1] #eleman seçimii

#* slice işlemi = 2. karakterden basla 7 'den öncekinde bitir.
# ! Pythonda her zaman 0 dan başlanır. !
long_str[2:7]

#* String içerisinde karakter sorgulamak
"veri" in long_str
"VERİ" in long_str
# büyük küçük harflere duyarlıdır.

#* STRİNG METODLARI

dir(str) #hangi metodların kullanıldıgı bir fonksiyondur
text = "Hello, AI Era!"

len(text) # stringin ne kadar uzun oldugunu

text.upper() # tüm karakterleri büyük harf
text.lower() # tüm karakterleri küçük harf yapar

text.replace("l", "k") # sağdaki harfle soldaki harfi dğeiştirir.
text.upper().replace("R", "C" ) # Metodlar arka arkaya kullanılabilir.

text.split() #stringi böler

text.capitalize() # ilk harfi büyük sonrakiler küçük
# eğer ilk harf yerine rakam varsa bütün harfler tekrardan küçük

text.title() # her kelimenin ilk harfi büyük.

###################################################################

#* LİSTELER ve METODLARI ***

lst = ["data science", 101, True, ["miuul"]]

len(lst) 

lst.append(33.34) # eleman eklemee
print(lst)

lst.pop(2) # indexe göre eleman silme işlemidir.

lst.insert(0 , "AI") # indexe göre eleman siler.

lst.upper() # ! error verir çünki string türünde ki verilere çalışır.

###########################################################################
## * FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSİONS
############################################################################

#* FONKSİYONLAR * 

def multiply_three(number):
    print(number * 3)

multiply_three(5)
multiply_three(12)
multiply_three(number = 16 )

# ön tanımlı argümanlar 
def hi(word = "selam"):
    print(word, "miuul!")

hi()
hi(word = "merhaba")

# iki argümanlı / parametreli bir fonksiyon tanımlayım.

def difference(num1, num2):
    result = num1 - num2
    print(result)

difference(7, 8)
difference(8, 7)

difference(num1= 8, num2= 7)

# Return: fonksiyon çıktılarını girdi olarak kullanmak
def difference(num1, num2 = 4):
    result = num1 - num2
    return result

difference(10)
difference(10, 2)

res = difference(10, 2)
res


# Örnek: Öğrencilerin vize notlarının %40'ını, 
# final notlarının %60'ını ağırlık olarak alan bir fonksiyon yaz
# Öğrenci1: vize:40, final:70
# Öğrenci2: vize:80, final:20

def note_calc(vize, final):
    return (vize*0.4) + (final * 0.60)

ogr1 = note_calc(40 , 70)
ogr1

#* KOŞULLAR *

name = "aslı"

if name == "aslı" or name == "aslısu":
     print("isim aslısu ve aslı içermekte!") 

# and or ve not kullanılarak daha güçlü hale getirilebilir.


# if elif else condition 
name = "aslisu"

if name == "Asli": 
    print("İsim Asli!") # eğer isim Asli ise çıktı "İsim Asli!"
elif name == "Miuul":
    print("İsim Miuul!") # eğer isim miullsa çıktı "İsim Miuul!"
else:
    print("İsim Asli ve ya Miuul değil!")


# fonksiyonla birleştirilsin

def name_control(name):
    if name == "Asli": 
          print("İsim Asli!") # eğer isim Asli ise çıktı "İsim Asli!"
    elif name == "Miuul":
          print("İsim Miuul!") # eğer isim miullsa çıktı "İsim Miuul!"
    else:
          print("İsim Asli ve ya Miuul değil!")

name_control("lenova")


#* LAMBDA FONKSİYONU
# Lambda fonksiyon yapar ve bunu tek satır da kullan at seklinde yapar

summer = lambda a, b : a + b
summer(8,9)

#* MAP FONKSİYONU
# Döngü yazmaktan kurtulmak için kullanılır.
def multiply_three(number):
    print(number * 3)

sayilar = [33,4,3,6,7,34,9,66]
list(map(multiply_three, sayilar))

# lamda & map kullanımı
list(map(lambda x: x**2, sayilar))

#* FILTER
# filtreleme işlemi sorgu işlemidir
list(filter(lambda x: x % 2 == 0, sayilar))

#* REDUCE
# bir işlevi listedeki diğer ögelere ardışık olarak uygular, önceki ile sonrakini
# birleştirme işlemidir.
from functools import reduce
list_store = [1,2,3,4]
reduce(lambda a, b: a + b, list_store)

#* DÖNGÜLER

#* for loop
bootcamps = ["Data Science", "Data Analytics", "AWS Cloud Engineering"]
bootcamps[0]
bootcamps[1]

for bc in bootcamps:
     print(bc)

# bu dongüde ki bc bootcamps'in içindeki her adımda bir ögeyi temsil eder.

for bc in bootcamps:
     print(bc.upper())

notes = [30, 50, 85]
for note in notes:
     print(int(1.5*(note + 10)))
# bu döngüdeki int yazmamızın sebebi cevapların float olacağından kaynaklı.
# daha temiz bir görüntü, dönüşüm için.

def extra(note, extra_point):
    new = int(1.5 * (note + extra_point))
    if new > 100:
        new = 100
    return new

extra(30, 20)

for note in notes:
     print("eski not:", note)
     print("yeni not:", extra(note, 10))
     print("---------------")

#* while - loop

num = 5
while num < 10 :
     print(num)
     num = num + 1

# +1 unutulmamı sonsuz loop eğer unutursan CTRL + C

idx = 0 # sıra numarası tanımlanıyo
while idx < len(notes):
     note = notes[idx]
     print("eski not:", note)
     print("yeni not:", extra(note, 10))
     print("---------------")
     idx += 1 # bu satır sayesinde index 1 artıyor ve sıradaki not işleniyor.


#* COMPREHENSİONS

# Comprehension, Python’da bir koleksiyonu (liste, set, sözlük) 
# kısa ve okunabilir bir şekilde oluşturma yöntemidir. 
# Genellikle for döngüsü ve if koşulu içerir.

#* LİST COMPRHENSİONS
salaries = [1000, 2000, 3000, 4000, 5000]

[salary * 2 for salary in salaries if salary < 3000]

# ! EĞER TEK BAsINA İF KULLANIYORSAN İF SAĞDA OLUR YUKARIDAKİ GİBİ, ELSE VAR İSE:

[salary * 2 if salary< 3000 else salary * 0 for salary in salaries]

# ! ELSE OLDUGU İÇİN DE SAĞA FOR DÖNGÜSÜNÜ ALDIK.

students = ["John", "Mark", "Venessa", "Mariam"]

no_students = ["John", "Venessa"]

[student.lower() if student in no_students else student.upper() for student in students]
# istenmeyen öğrencileri harflerini küçültüyoruz .

#* DİCT COMPREHENSİONS

dictinary = {"a": 1, 
             "b": 2,
             "c": 3,
             "d": 4}

{k: v ** 2 for (k, v) in dictinary.items()}

{k.upper(): v*2 for(k,v) in dictinary.items()}

