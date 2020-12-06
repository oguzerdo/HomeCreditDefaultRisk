# Data Preprocessing

**DAYS_EMPLOYED** 

------

Değişkeni incelendiğinde "365243" degerinin bir çok fazla sayıda girildiğini gördük. Önce bunun gürültü olabileceğini sonrasında ise NaN değerler yerine yazıldığı kanısına vardık. Bu sebeple bu değeri NaN olarak değiştirildi.

```python
df['DAYS_EMPLOYED'].replace(365243, np.nan, inplace=True)
```

**OWN_CAR_AGE**  

------

Değişkenini incelediğimiz de NaN değerler gördük , bu değerlere sonucumuza etki etmeyeceğini düşünerek 0 atandı .

```python
df["OWN_CAR_AGE"] = df["OWN_CAR_AGE"].fillna(0)
```

**DAYS_BIRTH**  

------

Değiskeni yaş değerini gün cinsinden belirtiyordu bu değişkeni 365 ' e bölerek yıl

haline getirdik. Ve sonrasında oluşturduğumuz değişkenin tipini "integer" şeklinde düzenledi.

```python
df["NEW_AGE"] = round(-1 * (df["DAYS_BIRTH"] / 365), 0)
df["NEW_AGE"] = df["NEW_AGE"].astype("int")
```

**OCCUPATION_TYPE** 

------

Değişkeni müşterilerinin meslek bilgilerini içinde barındıyordu bu meslekler target'a göre sınıflandırıldı.

```python
df.loc[(df["OCCUPATION_TYPE"] == "Drivers"), "OCCUPATION_TYPE"] = 1
df.loc[(df["OCCUPATION_TYPE"] == "Waiters/barmen staff"), "OCCUPATION_TYPE"] = 1
df.loc[(df["OCCUPATION_TYPE"] == "Low-skill Laborers"), "OCCUPATION_TYPE"] = 1
df.loc[(df["OCCUPATION_TYPE"] == "Cleaning staff"), "OCCUPATION_TYPE"] = 2
df.loc[(df["OCCUPATION_TYPE"] == "Sales staff"), "OCCUPATION_TYPE"] = 2
df.loc[(df["OCCUPATION_TYPE"] == "Laborers"), "OCCUPATION_TYPE"] = 2
df.loc[(df["OCCUPATION_TYPE"] == "Security staff"), "OCCUPATION_TYPE"] = 2
df.loc[(df["OCCUPATION_TYPE"] == "Cooking staff"), "OCCUPATION_TYPE"] = 2
df.loc[(df["OCCUPATION_TYPE"] == "Medicine staff"), "OCCUPATION_TYPE"] = 3
df.loc[(df["OCCUPATION_TYPE"] == "Private service staff"), "OCCUPATION_TYPE"] = 3
df.loc[(df["OCCUPATION_TYPE"] == "Realty agents"), "OCCUPATION_TYPE"] = 3
df.loc[(df["OCCUPATION_TYPE"] == "Secretaries"), "OCCUPATION_TYPE"] = 3
df.loc[(df["OCCUPATION_TYPE"] == "Accountants"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "Core staff"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "HR staff"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "High skill tech staff"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "Managers"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "Medicine staff"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "Private service staff"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "Realty agents"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "Secretaries"), "OCCUPATION_TYPE"] = 4
df.loc[(df["OCCUPATION_TYPE"] == "IT staff"), "OCCUPATION_TYPE"] = 4
```

**NAME_EDUCATION_TYPE**

------

Değişkeni müşterilerin eğitim bilgilerini içeriyor bu değişkeni target'a bakılarak ve birbirine yakın olanlar seçilerek sınıflandırıldı.

```python
df.loc[(df["NAME_EDUCATION_TYPE"] == "Academic degree"), "NAME_EDUCATION_TYPE"] = "Higher education"
df.loc[(df["NAME_EDUCATION_TYPE"] == "Incomplete higher"), "NAME_EDUCATION_TYPE"] = "Secondary / secondary special"
df.loc[(df["NAME_EDUCATION_TYPE"] == "Lower secondary"), "NAME_EDUCATION_TYPE"] = "Secondary / secondary special"
```

# Feature Engineering

**New Features** : 

*Feature 1* : **DAYS_EMPLOYED_PERC**

------

Müşterinin çalıştığı gün sayısının yaşına oranıyla elde edilir.

```python
df['DAYS_EMPLOYED_PERC'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
```

*Feature 2* : **INCOME_CREDIT_PERC**

------

Müşterinin yıllık toplam gelirinin kredi miktarına oranıyla elde edilir.

```python
df['INCOME_CREDIT_PERC'] = df['AMT_INCOME_TOTAL'] / df['AMT_CREDIT']
```

*Feature 3* : **PAYMENT_RATE**

------

Kredinin yıllık ödemesinin kredinin tamamına oranıyla elde edilir.

```python
df['PAYMENT_RATE'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
```

*Feature 4* : **NEW_INC_PERS**

------

Ailede bulunan kişi sayısının yıllık toplam gelire oranıyla elde edilir.

```python
df['NEW_INC_PERS'] = df['AMT_INCOME_TOTAL'] / df['CNT_FAM_MEMBERS']
```

Bunun dışında bunun benzeri olarak ailede cocuk sayısına oranı denendi.

```python
df['NEW_INC_PER_CHLD'] = df['AMT_INCOME_TOTAL'] / (1 + df['CNT_CHILDREN'])
```

Ancak importance üzerinde etkisi görülmediğinden çıkarıldı.

*Feature 5* : **NEW_AMT/FAM**

------

Toplam kredi miktarının ailede bulunan kişi sayısına oranıyla elde edilir.

```python
f['NEW_AMT/FAM'] = df['AMT_CREDIT'] / df['CNT_FAM_MEMBERS']
```

*Feature 6* : **NEW_ANNUITY_INCOME_PERC**

------

Kredinin yıllık ödemesinin müşterinin toplam gelirine oranıyla elde edilir.

```python
f['NEW_ANNUITY_INCOME_PERC'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
```

*Feature 7* : **NEW_AMT_STATUS**

```

```

Müşterinin almak istediği ürün ile çektiği kredi arasındaki farka göre bir derecelendirme yapıldı.

```python
df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] > 0), "NEW_AMT_STATUS"] = 1
df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] == 0), "NEW_AMT_STATUS"] = 2
df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] < 0), "NEW_AMT_STATUS"] = 3
```

*Feature 8*: **NEW_C-GP**

------

Çekilen kredi ile ürün arasında bulunan farkın yıllık toplam gelire oranıyla elde edilir.

```python
df["NEW_C-GP"] = (df["AMT_GOODS_PRICE"] - df["AMT_CREDIT"]) / df["AMT_INCOME_TOTAL"]
```

*Feature 9* : **CREDIT/NEW_AGE **

------

Müşterinin yaşının toplam kredi miktarına oranıyla elde edilir.

```python
df["CREDIT/NEW_AGE"] = df['AMT_CREDIT'] / df["NEW_AGE"]
```

*Feature 10* : **NEW_GOODS/CREDIT**

------

Alınmak istenin ürünün toplam kredi miktarına oranıyla elde edilir.

```python
df["NEW_GOODS/CREDIT"] = df["AMT_GOODS_PRICE"] / df["AMT_CREDIT"]
```

*Feature 11* : **NEW_AGE/CAR_AGE**

------

Müşterinin yaşının sahip olduğu arabanın yaşına oranıyla elde edilir .

```python
df["NEW_AGE/CAR_AGE"] = df["NEW_AGE"] / df["OWN_CAR_AGE"]
```

Veri seti incelendiginde en önemli değerler diğer kuruluşlardan alınan skorlardan oluşmaktadır.

*Feature 12* : **NEW_EXT_X**

------

Diğer kuruluşlardan alınan skorların çarpılmasıyla elde edilir.

```python
df["NEW_EXT_X"] = df["EXT_SOURCE_1"] * df["EXT_SOURCE_2"] * df["EXT_SOURCE_3"]
```

*Feature 13* : **NEW_EXT_MEAN**

------

Diğer kuruluşlardan alınan skorların ortalamasının alınmasıyla elde edilir.

```python
df["NEW_EXT_MEAN"] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
```

*Feature 14* : **NEW_SCORES_STD**

------

Diğer kuruluşlardan alınan skorların standart sapmasının alınmasıyla elde edilir.

```python
df['NEW_SCORES_STD'] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].std(axis=1)
```

Ürettiğimiz bu değişkende oluşacak boş değerleri yine bu değişkenin ortalamasıyla doldurdu.

```python
df['NEW_SCORES_STD'] = df['NEW_SCORES_STD'].fillna(df['NEW_SCORES_STD'].mean())
```

*Feature 15* : **NEW_BOMB**

------

Diğer kuruluşlardan alınan skorların en büyük fark yarattığı noktalar seçilerek temerrüt olması ya da olmaması durumunu açıklamak için 0 ve 1 atandı.

```python
df.loc[(df["EXT_SOURCE_1"] >= 0.5) | (df["EXT_SOURCE_2"] >= 0.55) | (df["EXT_SOURCE_3"] >= 0.45), "NEW_BOMB"] = 0
    df.loc[(df["EXT_SOURCE_1"] < 0.5) | (df["EXT_SOURCE_2"] < 0.55) | (df["EXT_SOURCE_3"] < 0.45), "NEW_BOMB"] = 1
```

*Feature 16* : **DOCUMENT_COUNT**  **New 

------

Dökümanların toplamı alındı.

```python
 docs = [f for f in df.columns if 'FLAG_DOC' in f]
 df['DOCUMENT_COUNT'] = df[docs].sum(axis=1)
 df.drop(docs, axis=1, inplace=True)
```

*Feature 17* : **NEW_AGE_RANK**

------

Yaş değişkeni 1:Young to 5:Older şeklinde sınıflandırıldı.

```python
df["NEW_AGE_RANK"] = pd.cut(x=df["NEW_AGE"], bins=[0, 27, 40, 50, 65, 99], labels=[1, 2, 3, 4, 5])
```

Oluşturalan değişken "integer" hale getirildi ve sonra eski değişken silindi.

```python
df["NEW_AGE_RANK"] = df["NEW_AGE_RANK"].astype("int")
df.drop("NEW_AGE", axis=1, inplace=True)
```

*Feature 18* : **NEW_PHONE_TO_BIRTH_RATIO**

------

Müşterinin son telefon değiştirdiği zamanın yaşına oranı ile elde edilir.

```python
df['NEW_PHONE_TO_BIRTH_RATIO'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_BIRTH']
```

*Feature 19* : **NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER**

------

Müşterinin son telefon değiştirdiği zamanın son çalıştığı işe başlama tarihine oranıyla elde edilir.

```python
df['NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_EMPLOYED']
```

*Feature 20* : **NEW_INC_ORG**

------

Müşterinin çalıştığı sekördeki maaş ortalamaları 

```python
INC_ORG =
df[['AMT_INCOME_TOTAL','ORGANIZATION_TYPE']].groupby('ORGANIZATION_TYPE').median()['AMT_INCOME_TOTAL']
df['NEW_INC_ORG'] = df['ORGANIZATION_TYPE'].map(INC_ORG)
```