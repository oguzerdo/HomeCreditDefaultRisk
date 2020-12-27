# Data Preprocessing

**DAYS_EMPLOYED** 

------

When the variable was examined, we saw that the value **"365243"** was entered in too many numbers. We first came to the conclusion that it might be **noise** and then it was written instead of NaN values. For this reason, this value has been changed to **NaN**.

```python
df['DAYS_EMPLOYED'].replace(365243, np.nan, inplace=True)
```

**CODE_GENDER**

------

4 observation values entered as **XNA** were recovered from this situation.

```python
df = df[df['CODE_GENDER'] != 'XNA']  
```

**OWN_CAR_AGE**  

------

When we examined the variable, we saw **NaN** values, and these values were assigned 0, considering that it would not affect our result.

```python
df["OWN_CAR_AGE"] = df["OWN_CAR_AGE"].fillna(0)
```

**DAYS_BIRTH**  T

he variable was specifying its age value in days. By dividing this variable by **365**, the year

we made it. And then he arranged the type of the variable we created as **"integer".**

```python
df["NEW_AGE"] = round(-1 * (df["DAYS_BIRTH"] / 365), 0)
df["NEW_AGE"] = df["NEW_AGE"].astype("int")
```

**OCCUPATION_TYPE** 

------

The variable contained the occupational information of the customers. These occupations were classified according to the **target**.

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

The variable contains the training information of the customers. This variable is classified by looking at the **target** and selecting those that are close to each other.

```python
df.loc[(df["NAME_EDUCATION_TYPE"] == "Academic degree"), "NAME_EDUCATION_TYPE"] = "Higher education"
df.loc[(df["NAME_EDUCATION_TYPE"] == "Incomplete higher"), "NAME_EDUCATION_TYPE"] = "Secondary / secondary special"
df.loc[(df["NAME_EDUCATION_TYPE"] == "Lower secondary"), "NAME_EDUCATION_TYPE"] = "Secondary / secondary special"
```

# Feature Engineering

**New Features** : 

*Feature 1* : **DAYS_EMPLOYED_PERC**

------

It is obtained by the ratio of the number of working days of the customer to the age of the customer.

```python
df['DAYS_EMPLOYED_PERC'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']
```



*Feature 2* : **INCOME_CREDIT_PERC**

------

It is obtained by the ratio of the total annual income of the customer to the loan amount.

```python
df['INCOME_CREDIT_PERC'] = df['AMT_INCOME_TOTAL'] / df['AMT_CREDIT']
```



*Feature 3* : **PAYMENT_RATE**

------

Obtained by the ratio of the annual payment of the customer's loan to the entire loan.

```python
df['PAYMENT_RATE'] = df['AMT_ANNUITY'] / df['AMT_CREDIT']
```



*Feature 4* : **NEW_INC_PERS**

------

It is obtained by the ratio of the number of family members to the total annual income.

```python
df['NEW_INC_PERS'] = df['AMT_INCOME_TOTAL'] / df['CNT_FAM_MEMBERS']
```

Apart from this, similarly, the ratio of the number of children in the family was tried.

```python
df['NEW_INC_PER_CHLD'] = df['AMT_INCOME_TOTAL'] / (1 + df['CNT_CHILDREN'])
```

However, it has been removed because it has no effect on importance.



*Feature 5* : **NEW_AMT/FAM**

------

It is obtained by the ratio of the total loan amount to the number of people in the family.

```python
f['NEW_AMT/FAM'] = df['AMT_CREDIT'] / df['CNT_FAM_MEMBERS']
```



*Feature 6* : **NEW_ANNUITY_INCOME_PERC**

------

It is obtained by the ratio of the annual payment of the loan to the total income of the customer.

```python
f['NEW_ANNUITY_INCOME_PERC'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
```



*Feature 7* : **NEW_AMT_STATUS**

------

A rating was made according to the difference between the product the customer wants to buy and the credit the customer received.

```python
df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] > 0), "NEW_AMT_STATUS"] = 1
df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] == 0), "NEW_AMT_STATUS"] = 2
df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] < 0), "NEW_AMT_STATUS"] = 3
```

In the Importance table, its effect was almost negligible and removed.



*Feature 8*: **NEW_C-GP**

------

It is obtained by the ratio of the difference between the loan and the product to the total annual income.

```python
df["NEW_C-GP"] = (df["AMT_GOODS_PRICE"] - df["AMT_CREDIT"]) / df["AMT_INCOME_TOTAL"]
```



*Feature 9* : **CREDIT/NEW_AGE **

------

It is obtained by the ratio of the age of the customer to the total loan amount.

```python
df["CREDIT/NEW_AGE"] = df['AMT_CREDIT'] / df["NEW_AGE"]
```



*Feature 10* : **NEW_GOODS/CREDIT**

------

It is obtained by the ratio of the product to be purchased to the total loan amount.

```python
df["NEW_GOODS/CREDIT"] = df["AMT_GOODS_PRICE"] / df["AMT_CREDIT"]
```



*Feature 11* : **NEW_AGE/CAR_AGE**

------

It is the ratio of the age of the customer to the age of the car owned by the customer.

```python
df["NEW_AGE/CAR_AGE"] = df["NEW_AGE"] / df["OWN_CAR_AGE"]
```

------

**When the data set is examined, the most important values are the scores obtained from other organizations.**



*Feature 12* : **NEW_EXT_X**

------

It is obtained by multiplying scores from other institutions.

```python
df["NEW_EXT_X"] = df["EXT_SOURCE_1"] * df["EXT_SOURCE_2"] * df["EXT_SOURCE_3"]
```

* The effect on score  has been checked and removed



*Feature 13* : **NEW_EXT_MEAN**

------

It is obtained by taking the average of scores from other organizations.

```python
df["NEW_EXT_MEAN"] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
```



*Feature 14* : **NEW_SCORES_STD**

------

It is obtained by taking the standard deviation of the scores from other institutions.

```python
df['NEW_SCORES_STD'] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].std(axis=1)
```

It filled the empty values that will occur in this variable that we produced with the average of this variable.

```python
df['NEW_SCORES_STD'] = df['NEW_SCORES_STD'].fillna(df['NEW_SCORES_STD'].mean())
```



*Feature 15* : **NEW_BOMB**

------

The points where scores from other institutions make the greatest difference were selected and 0 and 1 were assigned to explain whether there is a default or not.

```python
df.loc[(df["EXT_SOURCE_1"] >= 0.5) | (df["EXT_SOURCE_2"] >= 0.55) | (df["EXT_SOURCE_3"] >= 0.45), "NEW_BOMB"] = 0
    df.loc[(df["EXT_SOURCE_1"] < 0.5) | (df["EXT_SOURCE_2"] < 0.55) | (df["EXT_SOURCE_3"] < 0.45), "NEW_BOMB"] = 1
```

* Removed after the controls were done.



*Feature 16* : **NEW_DOCUMENT_COUNT**  

------

The total of the documents has been received.

```python
 docs = [f for f in df.columns if 'FLAG_DOC' in f]
 df['DOCUMENT_COUNT'] = df[docs].sum(axis=1)
 df.drop(docs, axis=1, inplace=True)
```



*Feature 17* : **NEW_AGE_RANK**

------

The age variable was classified as 1: Young to 5: Older.

```python
df["NEW_AGE_RANK"] = pd.cut(x=df["NEW_AGE"], bins=[0, 27, 40, 50, 65, 99], labels=[1, 2, 3, 4, 5])
```

The variable that created was made "integer" and then the old variable was deleted.

```python
df["NEW_AGE_RANK"] = df["NEW_AGE_RANK"].astype("int")
df.drop("NEW_AGE", axis=1, inplace=True)
```

* The effects of this variable were also not liked and removed.



*Feature 18* : **NEW_PHONE_TO_BIRTH_RATIO**

------

It is obtained by the ratio of the age of the last phone replacement of the customer.

```python
df['NEW_PHONE_TO_BIRTH_RATIO'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_BIRTH']
```



*Feature 19* : **NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER**

------

It is obtained by the ratio of the last time the customer changed the phone to the last working date.

```python
df['NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_EMPLOYED']
```



*Feature 20* : **NEW_INC_ORG**

------

Average salary in the sector where the client works

```python
INC_ORG =
df[['AMT_INCOME_TOTAL','ORGANIZATION_TYPE']].groupby('ORGANIZATION_TYPE').median()['AMT_INCOME_TOTAL']
df['NEW_INC_ORG'] = df['ORGANIZATION_TYPE'].map(INC_ORG)
```



*Feature 21* : **NEW_EXT_WEIGHTED**

------

Shaping credit ratings according to their **target effects.**

```python
df['NEW_EXT_WEIGHTED'] = df.EXT_SOURCE_1 * 2 + df.EXT_SOURCE_2 * 1 + df.EXT_SOURCE_3 * 3
```



*Feature 22* : **NEW_PHONE_TO_BIRTH_RATIO**

------

Obtained by the ratio of the age of the last phone replacement date.

```python
df['NEW_PHONE_TO_BIRTH_RATIO'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_BIRTH']
```



*Feature 23* : **NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER**

------

It is obtained by the ratio of the phone replacement date to the date of commencement.

```python
df['NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_EMPLOYED']
```



*Feature 24* : **NEW_PHO/ANNU**

------

It is obtained by the ratio of the phone replacement date to the annual loan payment.

```python
df['NEW_PHO/ANNU'] = df['DAYS_LAST_PHONE_CHANGE'] / df['AMT_ANNUITY']
```



*Feature 25* : **NEW_PHO/REG**

------

It is obtained by the ratio of the phone replacement date to the change date.

```python
df["NEW_PHO/REG"] = df['DAYS_LAST_PHONE_CHANGE'] * df["DAYS_REGISTRATION"]
```



*Feature 26* : **NEW_FRAUD**

------

It is obtained by the product of the variable we produce and the address mismatches.

```python
f["NEW_FRAUD_1"] = df["REG_CITY_NOT_LIVE_CITY"] + df["REG_CITY_NOT_WORK_CITY"] + df["LIVE_CITY_NOT_WORK_CITY"]
```

```python
df["NEW_FRAUD"] = (df["NEW_FRAUD_1"] + 1) * df["DAYS_ID_PUBLISH"]
```

```python
del df["NEW_FRAUD_1"]
```



*Feature 27* : **NEW_FRAUD_STD**

------

The standard deviation of the variable we are trying to find fraud with is taken.

```python
df["NEW_FRAUD_std"] = (df[["REG_CITY_NOT_LIVE_CITY", "REG_CITY_NOT_WORK_CITY", "LIVE_CITY_NOT_WORK_CITY"]]).std(axis=1)
```

# 