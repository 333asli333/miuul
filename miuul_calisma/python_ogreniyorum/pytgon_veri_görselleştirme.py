#########################################################
#* VERİ GÖRSELLEŞTİRME: MATPLOTLIB & SEABORN
#########################################################

#* MATPLOTLIB

# Kategorik değişken: sütun grafiği, countplot bar
# sayısal değişken: histogram, boxplot

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind = "bar")
plt.show()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

#######################################################

#* plot özelliği
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show() 

#! görselleri kapatmadan üst üste çalıstırırsan üstüne ekler!

# marker

y = np.array([13, 28, 11, 100])
plt.plot(y, marker = "o")
plt.show()

markers = [ "o", "*",".","x", "X", "+", "P", "s", "D", "d", "p","H", "h"]
# bunlar grafikte kullanılabilecek markerlar 

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle = "dotted") # noktalı çizgi
plt.show()

plt.plot(y, linestyle = "dashdot")
plt.show() # hem kesikli hem noktalı

plt.plot(y, linestyle = "dashed")
plt.show() # kesikli çizgi

#* BAŞLIK

plt.title("bu ana başlık")

plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("y ekseni isimlendirmesi")

plt.grid()
plt.show()

#* subplots

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.subplot(1,2,1)
plt.title("1")
plt.plot(x,y)



x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([24, 25, 26, 27, 280, 290, 300, 310, 320, 330])

plt.subplot(1,2,2)
plt.title("2")
plt.plot(x,y)

plt.show()


x = np.array([8, 8, 9, 5, 10, 15, 110, 115, 120, 125])
y = np.array([24, 25, 26, 27, 280, 290, 300, 310, 320, 330])

plt.subplot(1,3,3)
plt.title("3")
plt.plot(x,y)

plt.show()

#* SEABORN

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x = df["sex"], data = df)
plt.show()

sns.boxplot(x = df["total_bill"])
plt.show()

df["total_bill"].hist() # bu pandasa ait bir görselleştirme
plt.show()






































