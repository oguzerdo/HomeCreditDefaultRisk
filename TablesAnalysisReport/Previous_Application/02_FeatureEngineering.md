# Data Preprocessing



DAYS_FIRST_DRAWING

------

Değişkeni incelendiğinde "365243" degerinin bir çok fazla sayıda girildiğini gördük. Önce bunun gürültü olabileceğini sonrasında ise NaN değerler yerine yazıldığı kanısına vardık. Bu sebeple bu değeri NaN olarak değiştirildi.

```python
prev['DAYS_FIRST_DRAWING'].replace(365243, np.nan, inplace= True)
```



DAYS_FIRST_DUE

------

Yine aynı durum geçerli "365243" değeri görülüyor bu değerler NaN olarak değiştirildi.

```python
prev['DAYS_FIRST_DUE'].replace(365243, np.nan, inplace= True)
```



DAYS_LAST_DUE_1ST_VERSION

------

Burada da benzer bir durum söz konusu aynı değeri görmekteyiz, bu değer NaN hale getirildi.

```python
 prev['DAYS_LAST_DUE_1ST_VERSION'].replace(365243, np.nan, inplace= True)
```



DAYS_LAST_DUE

------

Aynı değer NaN olarak değiştirildi.

```python
 prev['DAYS_LAST_DUE'].replace(365243, np.nan, inplace= True)
```



DAYS_TERMINATION

------

Aynı değer NaN olarak değiştirildi.

```python
prev['DAYS_TERMINATION'].replace(365243, np.nan, inplace= True)
```



### Atılmasına Karar Verilen Değişkenler 

- FLAG_LAST_APPL_PER_CONTRACK
- NFLAG_LAST_APPL_IN_DAY
- WEEKDAY_APPR_PROCESS_START
- NAME_TYPE_SUITE
- NFLAG_INSURED_ON_APPROVAL
- NAME_SELLER_INDUSTRY



```python
 prev = prev.drop(["FLAG_LAST_APPL_PER_CONTRACT"],axis=1)
 prev = prev.drop(["NFLAG_LAST_APPL_IN_DAY"],axis=1)
 prev = prev.drop(["WEEKDAY_APPR_PROCESS_START"],axis=1)
 prev = prev.drop(["NAME_TYPE_SUITE"],axis=1)
 prev = prev.drop(["NFLAG_INSURED_ON_APPROVAL"],axis=1)
 prev = prev.drop(["NAME_SELLER_INDUSTRY"],axis=1)
```



### Az Rastlanan Değişkenler Kendilerine Yakın Sınıflara Aktarıldılar

NAME_PAYMENT_TYPE

```python
                                               Ratio  TARGET_MEAN  

Cash through the bank                      61.881412     0.184313  
Cashless from the account of the employer   0.064962     0.198157  
Non-cash from your account                  0.490536     0.149152  
XNA                                        37.563091     0.661577  
```

```python
prev.loc[(prev["NAME_PAYMENT_TYPE"] == "Cashless from the account of the employer"), "NAME_PAYMENT_TYPE"] = "Cash through the bank "
```



CODE_REJECT_REASON

```python
CODE_REJECT_REASON    Count      Ratio  TARGET_MEAN
CLIENT               26436  1670214   1.582791     0.000000
HC                  175231  1670214  10.491530     1.000000
LIMIT                55680  1670214   3.333705     1.000000
SCO                  37467  1670214   2.243245     1.000000
SCOFR                12811  1670214   0.767027     1.000000
SYSTEM                 717  1670214   0.042929     1.000000
VERIF                 3535  1670214   0.211650     1.000000
XAP                1353093  1670214  81.013152     0.233776
XNA                   5244  1670214   0.313972     0.998474
```

```python
prev.loc[(prev["CODE_REJECT_REASON"] != "CLIENT") & (prev["CODE_REJECT_REASON"] != "XAP"), "CODE_REJECT_REASON"] = "HC"
```



CHANNEL_TYPE

```python
                            CHANNEL_TYPE    Count      Ratio  TARGET_MEAN
AP+ (Cash loan)                    57046  1670214   3.415490     0.452442
Car dealer                           452  1670214   0.027062     0.367257
Channel of corporate sales          6150  1670214   0.368216     0.569268
Contact center                     71297  1670214   4.268734     0.646268
Country-wide                      494690  1670214  29.618360     0.136538
Credit and cash offices           719968  1670214  43.106332     0.597836
Regional / Local                  108528  1670214   6.497850     0.105236
Stone      
```

```python
prev.loc[(prev["CHANNEL_TYPE"] == "Regional / Local"), "CHANNEL_TYPE"] = "Regional / Local / Stone"
    prev.loc[(prev["CHANNEL_TYPE"] == "Stone"), "CHANNEL_TYPE"] = "Regional / Local / Stone"   
    prev.loc[(prev["CHANNEL_TYPE"] == "Credit and cash offices"), "CHANNEL_TYPE"] = "Credit and cash offices / Channel"
    prev.loc[(prev["CHANNEL_TYPE"] == "Channel of corporate sales"), "CHANNEL_TYPE"] = "Credit and cash offices / Channel"
```



NAME_YIELD_GROUP

```python
            NAME_YIELD_GROUP    Count      Ratio  TARGET_MEAN
XNA                   517215  1670214  30.966990     0.761606
high                  353331  1670214  21.154834     0.153513
low_action             92041  1670214   5.510731     0.229952
low_normal            322095  1670214  19.284655     0.233987
middle                385532  1670214  23.082791     0.161623
```

```python
prev.loc[(prev["NAME_YIELD_GROUP"] == "low_action"), "NAME_YIELD_GROUP" ] = "low"
prev.loc[(prev["NAME_YIELD_GROUP"] == "low_normal"), "NAME_YIELD_GROUP"] = "low"
prev.loc[(prev["NAME_YIELD_GROUP"] == "high"), "NAME_YIELD_GROUP"] = "mid/high"
prev.loc[(prev["NAME_YIELD_GROUP"] == "middle"), "NAME_YIELD_GROUP"] = "mid/high"
```



NAME_PORTFOLIO

```python
NAME_PORTFOLIO    Count      Ratio  TARGET_MEAN
Cards          144985  1670214   8.680624     0.325634
Cars              425  1670214   0.025446     0.381176
Cash           461563  1670214  27.634962     0.322875
POS            691011  1670214  41.372603     0.092465
XNA            372230  1670214  22.286366     0.931419
```

```python
 prev.loc[(prev["NAME_PORTFOLIO"] == "Cards"), "NAME_PORTFOLIO"] = "Cards/Car/Cash"
 prev.loc[(prev["NAME_PORTFOLIO"] == "Cars"), "NAME_PORTFOLIO"] = "Cards/Car/Cash"
 prev.loc[(prev["NAME_PORTFOLIO"] == "Cash"), "NAME_PORTFOLIO"] = "Cards/Car/Cash"
```



###### Kabul Edilme ya da Edilmeme durumuna göre "NAME_CONTRACT_STATUS" degiskeni ikiye ayrıldı ve verisetini değerlendirmek amacıyla target olarak kullanıldı.

```python
prev.loc[(prev["NAME_CONTRACT_STATUS"] == "Approved"),"NAME_CONTRACT_STATUS"] = 0
prev.loc[(prev["NAME_CONTRACT_STATUS"] == "Unused offer"),"NAME_CONTRACT_STATUS"] = 0
prev.loc[(prev["NAME_CONTRACT_STATUS"] == "Canceled"),"NAME_CONTRACT_STATUS"] = 1
prev.loc[(prev["NAME_CONTRACT_STATUS"] == "Refused"),"NAME_CONTRACT_STATUS"] = 1
prev["NAME_CONTRACT_STATUS"] = prev["NAME_CONTRACT_STATUS"].astype("int")
```





# Feature Engineering

**New Features** : 

*Feature 1* : **NEW_APP_CREDIT_PERC**

------

Müşterinin istediği kredinin aldığı krediye oranı ile elde edilir.

```python
prev['NEW_APP_CREDIT_PERC'] = prev['AMT_APPLICATION'] / prev['AMT_CREDIT']
```

*Feature 2* : **NEW_CREDIBILITY**

------

Müşterinin cevap alma hızı ve onay durumlarının beraber değerlendirilmesi sonucunda elde edilir.

```python
prev["DAYS_DECISION2"] = prev["DAYS_DECISION"] * -1
prev['ANS_SPEED'] = pd.cut(x = prev['DAYS_DECISION2'], bins = [0,100, 700, 3000], labels = ["Fast", "Normal", "Late"])
del prev["DAYS_DECISION2"]

prev.loc[((prev["NAME_CONTRACT_STATUS"] == "Approved" ) & (prev['ANS_SPEED'] == "Fast")),"NEW_CREDIBILITY"] = 5 #hızlı ve olumlu onay alanlar 
prev.loc[((prev["NAME_CONTRACT_STATUS"] == "Approved" ) & (prev['ANS_SPEED'] == "Normal")),"NEW_CREDIBILITY"] = 4 #normal ve olumlu onay alanlar 
prev.loc[((prev["NAME_CONTRACT_STATUS"] == "Approved" ) & (prev['ANS_SPEED'] == "Late")),"NEW_CREDIBILITY"] = 3 #yavaş ve olumlu onay alanlar 
prev.loc[((prev["NAME_CONTRACT_STATUS"] == "Refused" ) & (prev['ANS_SPEED'] == "Late")),"NEW_CREDIBILITY"] = 2  #yavaş ve olumsuz onay alanlar 
prev.loc[((prev["NAME_CONTRACT_STATUS"] == "Refused" ) & (prev['ANS_SPEED'] == "Normal")),"NEW_CREDIBILITY"] = 1  #normal ve olumsuz onay alanlar 
prev.loc[((prev["NAME_CONTRACT_STATUS"] == "Refused" ) & (prev['ANS_SPEED'] == "Fast")),"NEW_CREDIBILITY"] = 0  #hızlı ve olumsuz onay alanlar 
```

*Feature 3* : **NEW_ANN/CDT**

------

Müşterinin maaşının kredi tutarına oranı ile elde edilir.

```python
prev["NEW_ANN/CDT_PERC"] = prev["AMT_ANNUITY"] / prev["AMT_CREDIT"]
```

*Feature 4* : **NEW_CDT/PAY**

------

Kredinin tam tutarının vadesine bölümü ile elde edilir.

```python
prev["NEW_CDT/PAY"] = prev["AMT_CREDIT"] / prev["CNT_PAYMENT"]
```

*Feature 5* : **NEW_PAY_ABILITY**

------

Müşterinin geçmiş aylık kredi tutarının maaşına oranı     ***

```python
prev["NEW_PAY_ABILITY_PERC"] = prev["NEW_CDT/PAY"] / prev["AMT_ANNUITY"] 
```

*Feature 6* : **NEW_ABILITY**

------

Peşinatın maaşa oranı ile elde edilir.

```python
prev["NEW_PAY_ANN/DOWN_PERC"] = prev["AMT_ANNUITY"] / prev["AMT_DOWN_PAYMENT"]
```

