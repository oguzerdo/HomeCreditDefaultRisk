# FEATURE ANALYSIS

## CATEGORIC FEATURES

NAME_CONTRACT_TYPE  

Önceki başvurunun sözleşme ürün türü (Nakit kredi, tüketici kredisi [POS], ...)

```python
                    NAME_CONTRACT_TYPE    Count      Ratio  TARGET_MEAN
NAME_CONTRACT_TYPE                                                     
Cash loans                      747553  1670214  44.757917     0.581255
Consumer loans                  729151  1670214  43.656142     0.105251
Revolving loans                 193164  1670214  11.565225     0.493819
XNA                                346  1670214   0.020716     1.000000
```

*Çıkarımlar* : Consumer loans olanların temerrüte düşme oranlarının azlığı dikkat çekiyor.



WEEKDAY_APPR_PROCESS_START 

Müşteri önceki başvuru için haftanın hangi gününde başvurdu?

```python
     WEEKDAY_APPR_PROCESS_START    Count      Ratio  TARGET_MEAN
FRIDAY                         252048  1670214  15.090761     0.377579
MONDAY                         253557  1670214  15.181109     0.395386
SATURDAY                       240631  1670214  14.407196     0.304213
SUNDAY                         164751  1670214   9.864065     0.257777
THURSDAY                       249099  1670214  14.914197     0.386112
TUESDAY                        255118  1670214  15.274570     0.393496
WEDNESDAY                      255010  1670214  15.268103     0.389538
```

*Çıkarımlar* : Atılabilir



FLAG_LAST_APPL_PER_CONTRACT

Önceki sözleşme için son başvuru ise işaretleyin. Bazen müşterimizin veya katibimizin yanlışlıkla tek bir sözleşme için daha fazla başvuru olabilir.

```python
FLAG_LAST_APPL_PER_CONTRACT    Count     Ratio  TARGET_MEAN
N                         8475  1670214   0.50742     1.000000
Y                      1661739  1670214  99.49258     0.360178
```

*Çıkarımlar* :  Atılabilir.



NFLAG_LAST_APPL_IN_DAY

Uygulama, istemcinin günlük son uygulamasıysa işaretleyin. Bazen müşteriler günde daha fazla başvuru için başvurur. Nadiren sistemimizde bir uygulamanın veritabanında iki kez olması da hata olabilir

```
NFLAG_LAST_APPL_IN_DAY    Count      Ratio  TARGET_MEAN
0                    5900  1670214   0.353248     0.872881
1                 1664314  1670214  99.646752     0.361619
```

*Çıkarımlar* :  Atılabilir.



NAME_PAYMENT_TYPE 

Müşterinin önceki uygulama için ödemeyi seçtiği ödeme yöntemi

```python
NAME_PAYMENT_TYPE    Count  \
Cash through the bank                                1033552  1670214   
Cashless from the account of the employer               1085  1670214   
Non-cash from your account                              8193  1670214   
XNA                                                   627384  1670214   

                                               Ratio  TARGET_MEAN  
Cash through the bank                      61.881412     0.184313  
Cashless from the account of the employer   0.064962     0.198157  
Non-cash from your account                  0.490536     0.149152  
XNA                                        37.563091     0.661577  
```

*Çıkarımlar* : Ratiosu düşük iki değerin target değerleri birbirine yakın gruplandırılması değerlendirilebilir.



CODE_REJECT_REASON

Önceki başvuru neden reddedildi

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

*Çıkarımlar* : Temerrüte düşenler gruplanabilir. Feature importance tablosuna bakarak değerlendirilecek.



NAME_TPYE_SUITE

Önceki başvuru için başvururken müşteriye kim eşlik etti

```python
NAME_TYPE_SUITE : has 7 unique category 	- object

                 NAME_TYPE_SUITE    Count      Ratio  TARGET_MEAN
NaN                       820405  1670214        NaN          NaN
Unaccompanied             508970  1670214  30.473341     0.252675
Family                    213263  1670214  12.768603     0.155859
Spouse, partner            67069  1670214   4.015593     0.139081
Children                   31566  1670214   1.889937     0.130013
Other_B                    17624  1670214   1.055194     0.154335
Other_A                     9077  1670214   0.543463     0.153795
Group of people             2240  1670214   0.134115     0.214732
```

*Çıkarımlar* :  önemsiz gözüküyor.



NAME_CLIENT_TYPE

Önceki uygulama için başvururken müşteri eski mi yoksa yeni müşteri miydi

```python
NAME_CLIENT_TYPE : has 4 unique category 	- object

           NAME_CLIENT_TYPE    Count      Ratio  TARGET_MEAN
New                  301363  1670214  18.043376     0.059659
Refreshed            135649  1670214   8.121654     0.255041
Repeater            1231261  1670214  73.718757     0.449208
XNA                    1941  1670214   0.116213     0.685214
```

*Çıkarımlar* :  Yeni müşterilerin temerrüte düşme oranı düşük.



NAME_PORTFOLIO

Önceki NAKİT, POS, ARAÇ,… uygulamasıydı.

```python
NAME_PORTFOLIO : has 5 unique category 	- object

       NAME_PORTFOLIO    Count      Ratio  TARGET_MEAN
Cards          144985  1670214   8.680624     0.325634
Cars              425  1670214   0.025446     0.381176
Cash           461563  1670214  27.634962     0.322875
POS            691011  1670214  41.372603     0.092465
XNA            372230  1670214  22.286366     0.931419
```

*Çıkarımlar* : Target mean değerleri birbirine yakın olan cards/cars/cash degerleri bir araya getirilebilir.



NAME_PRODUCT_TYPE

Önceki uygulama x-sell o walk-in miydi

```python
NAME_PRODUCT_TYPE : has 3 unique category 	- object

         NAME_PRODUCT_TYPE    Count      Ratio  TARGET_MEAN
XNA                1063666  1670214  63.684414     0.386172
walk-in             150261  1670214   8.996512     0.516455
x-sell              456287  1670214  27.319074     0.260003
```

*Çıkarımlar* : Na değerlerin fazla olduğu görülüyor.



CHANNEL_TYPE

Önceki uygulamanın müşterisinin satış alanı

```python
CHANNEL_TYPE : has 8 unique category 	- object

                            CHANNEL_TYPE    Count      Ratio  TARGET_MEAN
AP+ (Cash loan)                    57046  1670214   3.415490     0.452442
Car dealer                           452  1670214   0.027062     0.367257
Channel of corporate sales          6150  1670214   0.368216     0.569268
Contact center                     71297  1670214   4.268734     0.646268
Country-wide                      494690  1670214  29.618360     0.136538
Credit and cash offices           719968  1670214  43.106332     0.597836
Regional / Local                  108528  1670214   6.497850     0.105236
Stone                             212083  1670214  12.697954     0.103992
```

*Çıkarımlar* :  Birbirine yakın degiskenler gruplanabilir.



NAME_YIELD_GROUP

Faiz oranı, önceki uygulamanın küçük orta ve yüksek olarak gruplandırılması

```python
NAME_YIELD_GROUP : has 5 unique category 	- object

            NAME_YIELD_GROUP    Count      Ratio  TARGET_MEAN
XNA                   517215  1670214  30.966990     0.761606
high                  353331  1670214  21.154834     0.153513
low_action             92041  1670214   5.510731     0.229952
low_normal            322095  1670214  19.284655     0.233987
middle                385532  1670214  23.082791     0.161623
```

*Çıkarımlar* :  low ve mid-high olarak iki parça haline getirilebilir.



NFLAG_INSURED_ON_APPROVAL

Müşteri önceki başvuru sırasında sigorta talep etti mi?

```python
NFLAG_INSURED_ON_APPROVAL : has 2 unique category 	- float64

     NFLAG_INSURED_ON_APPROVAL    Count     Ratio  TARGET_MEAN
0.0                     665527  1670214  39.84681          0.0
1.0                     331622  1670214  19.85506          0.0
NaN                     673065  1670214       NaN          NaN
```

*Çıkarımlar* : Atılabilir.



## NUMERICAL FEATURES



DAYS_DECİSİON

![](.\images\days_desicion.png)

*Çıkarımlar* : -500 den büyük değerlerin temerrüte düşme oranları yüksek .



CNT_PAYMENT

![](.\images\cnt_payment.png)

*Çıkarımlar* : 5 ila 15 değerleri arasında temerrüte düşmeme durumunda ki olumlu farklılık gözlemlendi.



DAYS_FIRST_DRAWING

![](.\images\days_first_drawing.png)

*Çıkarımlar* :  365.000 civarında'  ki değerlerin gün olarak bakıldığında anlamsiz olduğu görülüyor bu değerlere nan atamak mantıklı olacaktır.



DAYS_FIRST_DUE

![](.\images\days_fırst_due.png)

*Çıkarımlar* : 365.000 civarında'  ki değerlerin gün olarak bakıldığında anlamsiz olduğu görülüyor bu değerlere nan atamak mantıklı olacaktır.



DAYS_LAST_DUE_1ST_VERSION

![](.\images\days_last_due_1st_version.png)

*Çıkarımlar* : 365.000 civarında'  ki değerlerin gün olarak bakıldığında anlamsiz olduğu görülüyor bu değerlere nan atamak mantıklı olacaktır.



DAYS_LAST_DUE

![](.\images\days_last_due.png)

*Çıkarımlar* : 365.000 civarında'  ki değerlerin gün olarak bakıldığında anlamsiz olduğu görülüyor bu değerlere nan atamak mantıklı olacaktır.



DAYS_TERMINATION

![](.\images\days_termination.png)

*Çıkarımlar* : 365.000 civarında'  ki değerlerin gün olarak bakıldığında anlamsiz olduğu görülüyor bu değerlere nan atamak mantıklı olacaktır.

