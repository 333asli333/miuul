
#* KORELASYON ANALİZİ
import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
df = pd.read_csv(r"C:\Users\TORUN\OneDrive\Desktop\breast_cancer.csv")
df = df.iloc[:, 1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

# korelasyon ilişkilerin yönüdür.
corr = df[num_cols].corr()
corr

# heatmap
sns.set(rc={"figure.figsize" : (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

#################################################################################
#* YÜKSEK KORELASYONLU DEĞİŞKENLERİN SİLİNMESİ

cor_matrix = df.select_dtypes(include="number").corr().abs()

print(cor_matrix)

upper_triangle = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k = 1).astype(np.bool_))
upper_triangle

# Korelasyon matrisinin alt tarafı zaten üst tarafın aynası.
# O yüzden sadece üst tarafı alalım, tekrarları silelim.

# eğer sütunlarda %90 dan büyük varsa bunun silinmesi gerekir.

drop_list = [col for col in upper_triangle.columns if any(upper_triangle[col]>0.90)]
drop_list
cor_matrix[drop_list]

df.drop(drop_list, axis=1)

def high_correlated_cols(dataframe, plot = False, corr_th = 0.90):
    corr = dataframe.corr()
    cor_matrix= corr.abs()
    upper_triangle = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k = 1).astype(np.bool_))
    drop_list = [col for col in upper_triangle.columns if any(upper_triangle[col]>0.90)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={"figure.figsize": (15,15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df.select_dtypes(include="number"))
drop_list = high_correlated_cols(df.select_dtypes(include="number"), plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1).select_dtypes(include="number"), plot=True)









