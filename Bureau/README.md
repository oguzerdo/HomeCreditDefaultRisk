Yeni bir "Danger " sınıfı oluşturduk . Bu sınıfa Label Encoding uygulayarak elde ettiğimiz verileri yerleştireceğiz. 0,1,2,3

0=Gecikmis Borcu Olmayan

1=100.000' e kadar gecikmis baska kredi borcu olanlar

2=100.000'den 500.000'e kadar gecikmis baska kredi borcu olanlar

3=500.000'den fazla gecikmis kredi borcu olanlar

nan değerler borcu yok diye değerlendirildi. model sonucuna göre kontrol edilecek.

```python
bureau["AMT_CREDIT_MAX_OVERDUE"] = bureau["AMT_CREDIT_MAX_OVERDUE"].fillna(0) 
```

Gecikmiş borcu olmayanlar

```python
bureau.loc[((bureau["AMT_CREDIT_MAX_OVERDUE"] >= 0) | (bureau["AMT_CREDIT_SUM_OVERDUE"] >= 0)), "NEW_DANGER"] = 0
```

 100.000'e kadar gecikmiş (başka) kredi borcu olanlar

```python
bureau.loc[((bureau["AMT_CREDIT_MAX_OVERDUE"] >= 1) | (bureau["AMT_CREDIT_SUM_OVERDUE"] >= 1)), "NEW_DANGER"] = 1
```

100.000'den 500000'e kadar gecikmiş (başka) kredi borcu olanlar

```python
bureau.loc[((bureau["AMT_CREDIT_MAX_OVERDUE"] >= 100000) | (bureau["AMT_CREDIT_SUM_OVERDUE"] >= 100000)), "DANGER"] = 2 
```

500.000 den fazla gecikmiş borcu olup hayal kuranlar

```python
bureau.loc[((bureau["AMT_CREDIT_MAX_OVERDUE"] >= 500000) | (bureau["AMT_CREDIT_SUM_OVERDUE"] >= 500000)), "NEW_DANGER"] = 3 
```

Sonuclara etkisi düşük olduğundan çıkarıldı.