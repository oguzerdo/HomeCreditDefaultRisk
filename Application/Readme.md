Yeni oluşturulan değişkenler ve fayda sağlanamayanlar

**NEW_AMT_STATUS**

```
# # FEATURE 5 - ALMAK İSTEDİĞİ MAL VE ÇEKTİĞİ KREDİ ARASINDAKİ FARKA GÖRE DERECELENDİRME
# df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] > 0), "NEW_AMT_STATUS"] = 1
# df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] == 0), "NEW_AMT_STATUS"] = 2
# df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] < 0), "NEW_AMT_STATUS"] = 3
```

**NEW_EXT_X**

Farklı kaynaklardan alınan puanların çarpımı ile oluşturuldu.

```
#df["NEW_EXT_X"] = df["EXT_SOURCE_1"] * df["EXT_SOURCE_2"] * df["EXT_SOURCE_3"]
```

Her bir kaynağın ağırlığı belirtilerek oluşturulan yeni değişkende daha çok fayda sağlandığı için bu değişken çıkartıldı.

```
# FEATURE 10 - EXT AĞIRLIKLI ÇARPIM
df['NEW_EXT_WEIGHTED'] = df.EXT_SOURCE_1 * 2 + df.EXT_SOURCE_2 * 1 + df.EXT_SOURCE_3 * 3
```

