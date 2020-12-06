import numpy as np
import pandas as pd
import seaborn as sns
import time
from contextlib import contextmanager
import warnings
from lightgbm import LGBMClassifier
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)

pd.pandas.set_option('display.max_rows', None)
pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{} - done in {:.0f}s".format(title, time.time() - t0))


# One-hot encoding for categorical columns with get_dummies
def one_hot_encoder(df, nan_as_category=True):
    original_columns = list(df.columns)
    categorical_columns = [col for col in df.columns if df[col].dtype == 'object']
    df = pd.get_dummies(df, columns=categorical_columns, dummy_na=nan_as_category)
    new_columns = [c for c in df.columns if c not in original_columns]
    return df, new_columns


def application_train_test(num_rows=None, nan_as_category=False):
    # Read data and merge
    df = pd.read_csv(r'data\application_train.csv', nrows=None)
    test_df = pd.read_csv(r'data\application_test.csv', nrows=None)
    print("Train samples: {}, test samples: {}".format(len(df), len(test_df)))
    df = df.append(test_df).reset_index()

    # DATA PREPROCESSING
    df = df[df['CODE_GENDER'] != 'XNA']  # 4 gözlem değeri XNA olarak girilmiş bundan kurtarıldı.
    df['DAYS_EMPLOYED'].replace(365243, np.nan, inplace=True)  # NaN değerleri 365243 olarak girilmiş, onlar düzeltildi
    df["OWN_CAR_AGE"] = df["OWN_CAR_AGE"].fillna(0)  # Araba yaş değeri boş olan gözlemler 0 olarak atandı

    # FEATURE ENGINEERING
    # AGE gün cinsinden belirtilmiş bu normal yaşa çevrildi.
    df["NEW_AGE"] = round(-1 * (df["DAYS_BIRTH"] / 365), 0)
    df["NEW_AGE"] = df["NEW_AGE"].astype("int")

    # NEW FEATURES
    df['DAYS_EMPLOYED_PERC'] = df['DAYS_EMPLOYED'] / df['DAYS_BIRTH']  # Müşterinin çalıştığı gün sayısının yaşına oranı
    df['INCOME_CREDIT_PERC'] = df['AMT_INCOME_TOTAL'] / df[
        'AMT_CREDIT']  # Müşterinin yıllık toplam gelirinin kredi miktarına oranı
    df['PAYMENT_RATE'] = df['AMT_ANNUITY'] / df['AMT_CREDIT'] # Kredinin yıllık ödemesinin, kredinin tamamına oranı

    # FEATURE 1 - MAAŞ / AİLEDEKİ KİŞİ SAYISI
    df['NEW_INC_PERS'] = df['AMT_INCOME_TOTAL'] / df['CNT_FAM_MEMBERS']
    # FEATURE 2 - KREDİ MİKTARI / AİLEDEKİ KİŞİ SAYISI
    df['NEW_AMT/FAM'] = df['AMT_CREDIT'] / df['CNT_FAM_MEMBERS']
    # FEATURE 3 - KREDİNİN YILLIK ÖDEMESİ / GELİR
    df['NEW_ANNUITY_INCOME_PERC'] = df['AMT_ANNUITY'] / df['AMT_INCOME_TOTAL']
    # FEATURE 4 - GELİR / YILLIK KREDİ * FAMILYSIZE #MODEL SONUCUNA GÖRE DEĞERLENDİR
    df["NEW_FAMILY_EFFECT"] = df['NEW_AMT/FAM'] / df['CNT_FAM_MEMBERS']
    # # FEATURE 5 - ALMAK İSTEDİĞİ MAL VE ÇEKTİĞİ KREDİ ARASINDAKİ FARKA GÖRE DERECELENDİRME
    # df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] > 0), "NEW_AMT_STATUS"] = 1
    # df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] == 0), "NEW_AMT_STATUS"] = 2
    # df.loc[(df["AMT_CREDIT"] - df["AMT_GOODS_PRICE"] < 0), "NEW_AMT_STATUS"] = 3
    # FEATURE 6 - ÇEKİLEN KREDİ İLE ÜRÜN ARASINDAKİ FARKIN GELİRE ORANI ***
    df["NEW_C-GP"] = (df["AMT_GOODS_PRICE"] - df["AMT_CREDIT"]) / df["AMT_INCOME_TOTAL"]
    # FEATURE 7 - YAŞ / KREDİ MİKTARI
    df["NEW_CREDIT/NEW_AGE"] = df['AMT_CREDIT'] / df["NEW_AGE"]
    # FEATURE 8 - ÜRÜN / KREDİ MİKTARI ***
    df["NEW_GOODS/CREDIT"] = df["AMT_GOODS_PRICE"] / df["AMT_CREDIT"]
    # FEATURE 9 - AGE / OWN_CAR_AGE
    df["NEW_AGE/CAR_AGE"] = df["NEW_AGE"] / df["OWN_CAR_AGE"]
    # FEATURE 10 - EXT AĞIRLIKLI ÇARPIM
    df['NEW_EXT_WEIGHTED'] = df.EXT_SOURCE_1 * 2 + df.EXT_SOURCE_2 * 1 + df.EXT_SOURCE_3 * 3
    #df["NEW_EXT_X"] = df["EXT_SOURCE_1"] * df["EXT_SOURCE_2"] * df["EXT_SOURCE_3"]
    # FEATURE 11 - EXT MEAN
    df["NEW_EXT_MEAN"] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].mean(axis=1)
    # FEATURE 12 - EXT STD
    df['NEW_SCORES_STD'] = df[['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']].std(axis=1)
    df['NEW_SCORES_STD'] = df['NEW_SCORES_STD'].fillna(df['NEW_SCORES_STD'].mean())
    # FEATURE 13 - NEW EXT PROCESS
    df.loc[(df["EXT_SOURCE_1"] >= 0.5) | (df["EXT_SOURCE_2"] >= 0.55) | (df["EXT_SOURCE_3"] >= 0.45), "NEW_BOMB"] = 0
    df.loc[(df["EXT_SOURCE_1"] < 0.5) | (df["EXT_SOURCE_2"] < 0.55) | (df["EXT_SOURCE_3"] < 0.45), "NEW_BOMB"] = 1
    # FEATURE 14 - DOKUMANLARIN TOPLAMI / DOCS ATILDI
    docs = [f for f in df.columns if 'FLAG_DOC' in f]
    df['NEW_DOCUMENT_COUNT'] = df[docs].sum(axis=1)
    df.drop(docs, axis=1, inplace=True)
    # FEATURE 15 - AGE RANK 1: YOUNG 5: OLDER
    # df["NEW_AGE_RANK"] = pd.cut(x=df["NEW_AGE"], bins=[0, 27, 40, 50, 65, 99], labels=[1, 2, 3, 4, 5])
    # df["NEW_AGE_RANK"] = df["NEW_AGE_RANK"].astype("int")
    #df.loc[(df["DAYS_BIRTH"] >= -15000),"NEW_YOUNG_FLAG"] = 1
    df.drop("NEW_AGE", axis=1, inplace=True)
    # FEATURE 16 NEW_PHONE_TO_BIRTH_RATIO
    df['NEW_PHONE_TO_BIRTH_RATIO'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_BIRTH']
    # FEATURE 17 NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER
    df['NEW_PHONE_TO_BIRTH_RATIO_EMPLOYER'] = df['DAYS_LAST_PHONE_CHANGE'] / df['DAYS_EMPLOYED']
    # FEATURE 18 - NEW_INC_ORG : Sektöründeki maaş ortalamaları
    INC_ORG = df[['AMT_INCOME_TOTAL', 'ORGANIZATION_TYPE']].groupby('ORGANIZATION_TYPE').median()['AMT_INCOME_TOTAL']
    df['NEW_INC_ORG'] = df['ORGANIZATION_TYPE'].map(INC_ORG)
    # CLEAN CLASSES & LABEL ENCODING PART

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

    def cols(dataframe, target, noc=10, ID=True):
        """
        noc : number of classes to threshold
        ID : if your data has ID, index etc
        """
        vars_more_classes = []
        if ID:
            ID = dataframe.columns[0]
        else:
            ID = "x"

        cat_cols = [col for col in dataframe.columns if dataframe[col].nunique() < noc
                    and col not in target]

        num_cols = [col for col in dataframe.columns if dataframe[col].nunique() > noc
                    and dataframe[col].dtypes != "O"
                    and col not in target
                    and col not in cat_cols and col not in ID]

        other_cols = [col for col in dataframe.columns if col not in cat_cols
                      and col not in num_cols and col not in ID
                      and col not in target]
        return cat_cols, num_cols, other_cols

    drop_list = [
        'FLAG_EMP_PHONE', 'FLAG_MOBIL', 'FLAG_CONT_MOBILE',
        'LIVE_REGION_NOT_WORK_REGION', 'FLAG_EMAIL', 'FLAG_PHONE',
        'FLAG_OWN_REALTY', 'NAME_TYPE_SUITE',
        'AMT_REQ_CREDIT_BUREAU_HOUR', 'AMT_REQ_CREDIT_BUREAU_WEEK',
        'COMMONAREA_MODE', 'FLOORSMAX_MODE', 'FLOORSMIN_MODE',
        'LIVINGAPARTMENTS_MODE', 'LIVINGAREA_MODE', 'NONLIVINGAPARTMENTS_MODE',
        'NONLIVINGAREA_MODE', 'ELEVATORS_MEDI', 'EMERGENCYSTATE_MODE',
        'FONDKAPREMONT_MODE', 'HOUSETYPE_MODE', 'WALLSMATERIAL_MODE'
    ]

    df.drop(drop_list, axis=1, inplace=True)

    cat_cols, num_cols, other_cols = cols(df, "TARGET")

    def label_encoder(dataframe, categorical_columns):
        """
        2 sınıflı kategorik değişkeni 0-1 yapma
        :param dataframe: İşlem yapılacak dataframe
        :param categorical_columns: Label encode yapılacak kategorik değişken adları
        :return:
        """
        labelencoder = preprocessing.LabelEncoder()

        for col in categorical_columns:
            if dataframe[col].nunique() == 2:
                dataframe[col] = labelencoder.fit_transform(dataframe[col])
        return dataframe

    df = label_encoder(df, cat_cols)

    df, app_cols = one_hot_encoder(df, True)

    return df

df = application_train_test(num_rows=None, nan_as_category=True)
df.shape
X = df.loc[:307510, :].drop(["TARGET","index"], axis=1)
y = df.loc[:307510, "TARGET"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=46)


models = [("LightGBM", LGBMClassifier())]
# evaluate each model in turn
results = []
names = []

lgbm = LGBMClassifier(random_state=42).fit(X_train, y_train)
y_pred = lgbm .predict(X_test)
print(accuracy_score(y_test,y_pred))
# Feature Importance
Importance = pd.DataFrame({'Importance': lgbm.feature_importances_ * 100,
                           'Feature': X_train.columns})

plt.figure(figsize=(10, 30))
sns.barplot(x="Importance", y="Feature", data=Importance.sort_values(by="Importance", ascending=False))
plt.title('Feature Importance ')
plt.tight_layout()
plt.savefig('LGBM_importances.png')
plt.show()
