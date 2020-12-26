# Home Credit Default Risk

Bu repoda Kaggle’daki Home Credit Default Risk yarışmasında, müşterilerin temerrüt risklerini tahmin etmek amacıyla oluşturulmuş bir classification projesinin scriptleri yer almaktadır.

Veri Setinin diskteki boyutu 2.5gb olmak üzere genel hatları şu şekildedir;

Veriler **7 farklı tablodan** oluşmakta ve her bir alt tabloya inildiğinde tekil müşteri işlemleri **çoklanmış** şekildedir. Bir müşteriye ait tek bir Unique ID olmakta ve alt tablolarda bu müşterilerin birden fazla işlemleri bulunmakta.

- Application tablosunda: **307.511** gözlem ile birlikte **122** feature

- Bureau tablosunda **1.716.428** gözlem ve **17** feature 

- Bureau & Balance tablosunda **27299925** gözlem ve **3** feature 

- Previous tablosunda **1.670.214** gözlem ve **37** feature

- POS Cash Balance tablosunda **10001358** gözlem ve **8** feature

- Installments Payments tablosunda **13605401** gözlem ve **8** feature

- Credit Card Balance tablosunda **3840312** gözlem ve **23** feature bulunmaktadır. 



İlk olarak detaylı EDA çıktıları ile birlikte değişkenler tanınıp proje kapsamınca bütün adımları github üzerinde raporlanmıştır.

Bu tablolar en üst tablo olan Application tablosu ile, değişkenlerinin çeşitli karakteristik özellikleriyle birlikte birleştirilmiştir. 

Proje kapsamında olabildiğince yeni değişkenler türetilmeye çalışılıp, türetilen değişkenlerin model tahmin sonucuna etkisi gözlemlenmeye çalışılmıştır.

Gözlem sayısının çokluğundan dolayı **CLI** ile kontrol edilebilen bir **Debug** modu geliştirilmiş ve hatalar düzeltilmeye çalışılmıştır.

Veri ön işleme sonrasında RAM üzerinden Disk ortamına inerek train ve test setlerinin imageları alınarak ve ileriki süreçler garantiye alınmıştır.

Proje **Makefile** dosyası da içermektedir. Makefile sayesinde sık tekrarlanan işlemler (model train, predict, tune, github commit, push, update, kaggle submit) işlemleri terminal üzerinden tek komuta indirgenmiştir.



---

## Tablo Hiyerarşisi

![tables](./TablesAnalysisReport/Application/images/tables.png)



---



## Tabloların Detaylı EDA Raporları

Aşağıdaki bağlantılardan en önemli olduğunu düşündüğümüz tabloların detaylı EDA analizlerine ve proje kapsamınca oluşturulan yeni değişkenlerin raporlarına ulaşabilirsiniz.

**Application**

- [Rapor](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Application/README.md)

- [EDA](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Application/01_ApplicationEDA.ipynb)

- [Feature Engineering](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Application/02_FeatureEngineering.md)

**Bureau** 

- [Rapor](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Bureau/README.md)

- [EDA](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Bureau/01_BureauEDA.ipynb)

- [Feature Engineering](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Bureau/02_FeatureEngineering.md)

**Previous Application**

- [Rapor](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Previous_Application/README.md)

- [EDA](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Previous_Application/01_PreviousEDA.ipynb)

- [Feature Engineering](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/TablesAnalysisReport/Previous_Application/02_FeatureEngineering.md)



---

## Installation

1. Install Python 3 with pip
2. Clone repository and install requirements

```
pip3 install -r requirements.txt
```

Run the main file

```
python main.py
```



---

## Requirements

```
pandas~=1.1.5
cowsay~=3.0
numpy~=1.19.2
lightgbm~=2.0.3
scikit-learn~=0.24.0
seaborn~=0.11.1
matplotlib~=3.3.2
```

[requirements.txt](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/requirements.txt)



---

## Authors

**Oğuz Han Erdoğan** -  [oguzerdo](https://github.com/oguzerdo)

**Emre Gür** - [emregurr](https://github.com/emregurr)

