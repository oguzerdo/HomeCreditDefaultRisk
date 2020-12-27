# Home Credit Default Risk

## Authors

**Oğuz Han Erdoğan** -  [oguzerdo](https://github.com/oguzerdo)

**Emre Gür** - [emregurr](https://github.com/emregurr)

---
This repo includes the scripts of a classification project created to predict the default risks of customers in the Home Credit Default Risk competition in Kaggle.
[Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk?rvi=1)
---
The space occupied by the data set on the disk is 2.5 GB and the content of the data set is as follows;

The data **consists of 7 different tables** and when each sub-table goes down, individual customer transactions are **multiplexed**. There is only one Unique ID belonging to a customer and these customers have more than one transactions in the sub-tables.

- **Application** table contains **307.511 observations**, besides it has **122** features.
- **Bureau** table contains **1.716.428** observations, while it has **17** features. 
- **Bureau & Balance** contains **27.299.925** observations, while it has **3** features. 
- **Previous** table contains **1.670.214** observations, besides it has **37** features.
- **POS Cash Balance** table contains **10.001.358** observations, and it has **8** features.
- **Installments Payments** table contains **13.605.401** observations, while it has **8** features.
- There are **3.840.312** observations and **23** feature in the **Credit Card Balance** table.



First of all, the variables were defined along with the detailed **EDA** outputs and all the steps within the scope of the project were reported on **github.**

The tables we mentioned above are combined with the Application table by looking at the **various characteristics** of their variables. The reason for doing this is that the **Application** table is the **main table**.

Throughout the project, **new variables** were tried to be produced as much as possible and the **effect** of the generated variables on the model estimation result was observed.

Due to the large number of observations, a **Debug** mode that can be controlled with **CLI** was developed and the errors that occurred were tried to be corrected.

After data pre-processing, the images of the train and test sets are taken from the **RAM** to the **Disk** environment and the future processes are **guaranteed**.

The project also includes the **Makefile** file. Using Makefile, frequently repeated operations **(model train, predict, tune, github commit, push, update, kaggle submit)** are made functional using a single command over the terminal.



---

## Hierarchy Table

![tables](./TablesAnalysisReport/Application/images/tables.png)



---



## Detailed EDA Reports of Tables

You can reach the **detailed EDA analysis** of the tables we think are the **most important** and the reports of the new variables created within the scope of the project from the links below.

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
numpy~=1.19.2
lightgbm~=2.0.3
scikit-learn~=0.24.0
seaborn~=0.11.1
matplotlib~=3.3.2
cowsay~=3.0
```

[requirements.txt](https://github.com/oguzerdo/HomeCreditDefaultRisk/blob/main/requirements.txt)



---

## Authors

**Oğuz Han Erdoğan** -  [oguzerdo](https://github.com/oguzerdo)

**Emre Gür** - [emregurr](https://github.com/emregurr)

---

## Special Thanks

Dear **Mustafa Vahit Keskin** - [mvahit](https://github.com/mvahit)

and to the owner of this reference notebook

```
Reference notebook : https://www.kaggle.com/jsaguiar/lightgbm-with-simple-features
```

