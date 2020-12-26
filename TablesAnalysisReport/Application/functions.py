# !/usr/bin/env python
# coding: utf-8
""""
All functions
Date: 6.12.2020
"""

# Catch Features
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
import warnings
from sklearn.exceptions import ConvergenceWarning

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter("ignore", category=ConvergenceWarning)

# Catch Features

def cols(dataframe, target, noc=10, ID=True):
    """
    noc : number of classes to threshold
    ID : if your data has ID, index etc in first column
    """
    vars_more_classes = []
    if ID:
        ID = dataframe.columns[0]
    else:
        ID = "x"

    cat_cols = [col for col in dataframe.columns if dataframe[col].nunique() < noc
                and col not in target]
    print("Number of Categorical Columns:", len(cat_cols))
    print(cat_cols)
    print("--" * 25)
    num_cols = [col for col in dataframe.columns if dataframe[col].nunique() > noc
                and dataframe[col].dtypes != "O"
                and col not in target
                and col not in cat_cols and col not in ID]
    print("Number of Numerical Columns:", len(num_cols))
    print(num_cols)
    print("--" * 25)
    other_cols = [col for col in dataframe.columns if col not in cat_cols
                  and col not in num_cols and col not in ID
                  and col not in target]
    print(other_cols)
    print("--" * 25)
    return cat_cols, num_cols, other_cols


def cols_n(c, n, o):
    """
    Print cateoric,numeric and other columns
    """
    print("Number of Categorical Columns:", len(c))
    print(c)
    print("--" * 25)
    print("Number of Numerical Columns:", len(n))
    print(n)
    print("--" * 25)
    print("More than Thresholds Category Columns", len(o))
    print(o)
    print("--" * 25)


def graphs(dataframe, col, target, cat_analyze=True):
    if cat_analyze == True:
        fig, axarr = plt.subplots(1, 2, figsize=(10, 6))
        a = sns.countplot(x=dataframe[col], hue=dataframe[target], data=dataframe, ax=axarr[0]).set_title(
            'Count by class')
        axarr[0].set_xticklabels(axarr[0].get_xticklabels(), rotation=45);
        axarr[1].set_title('Rate by class')
        b = sns.barplot(x=dataframe[col], y=dataframe[target], data=dataframe, ax=axarr[1]).set_ylabel('Rate')
        axarr[1].set_xticklabels(axarr[1].get_xticklabels(), rotation=45);
        plt.show()

    else:
        fig, axarr = plt.subplots(1, 2, figsize=(15, 6))
        axarr[0].set_title('Distribution')
        f = sns.distplot(dataframe[col], color='g', bins=40, ax=axarr[0])
        axarr[1].set_title('Distribution for the two subpopulations')
        g = sns.kdeplot(dataframe[col].loc[dataframe[target] == 1],
                        shade=True, ax=axarr[1], label='Risk').set_xlabel(col)
        g = sns.kdeplot(dataframe[col].loc[dataframe[target] == 0],
                        shade=True, ax=axarr[1], label='Good', legend=True)
        plt.legend();


def cat_summary(dataframe,categorical_cols, target, noc=10):
    print("CATEGORICAL FEATURE ANALYSIS", end="\n\n")
    var_count = 0
    vars_more_classes = []
    for var in categorical_cols:
        if dataframe[var].nunique() <= noc:  # sınıf sayısına göre seç
            print(var, ": has", dataframe[var].nunique(), "unique category", "\t-", str(dataframe[var].dtypes),
                  end="\n\n")
            print(pd.DataFrame({var: dataframe[var].value_counts(dropna=False),
                                "Count": len(dataframe[var]),
                                "Ratio": 100 * dataframe[var].value_counts() / len(dataframe),
                                "TARGET_MEAN": dataframe.groupby(var)[target].mean()}), end="\n\n\n")
            var_count += 1
            graphs(dataframe, var, target, True)
            print("\n\n")
        else:
            vars_more_classes.append(dataframe[var].name)
    print('%d categorical variables have been described' % var_count, end="\n\n")
    print('There are', len(vars_more_classes), "variables have more than", noc, "classes", end="\n\n")
    print('Variable names have more than %d classes:' % noc, end="\n\n")
    print(vars_more_classes)

def cat_summary2(dataframe,target,target2):
    print("CATEGORICAL FEATURE ANALYSIS",end="\n\n")
    print(target2, ": has",dataframe[target2].nunique(), "unique category","\t-",str(dataframe[target2].dtypes),end="\n\n")
    print(pd.DataFrame({target2: dataframe[target2].value_counts(),
                        "Ratio": 100 * dataframe[target2].value_counts() / len(dataframe),
                        "TARGET_MEAN": dataframe.groupby(target2)[target].mean()}),end="\n\n\n")


def num_summary(dataframe, num_cols, target):
    for col in num_cols:
        graphs(dataframe, col, target, False)

def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
                                                              "There are " + str(
        mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns


def target(dataframe, target):
    temp = pd.DataFrame({"Good Ratio": 100 * dataframe[target].value_counts()[0] / len(dataframe),
                         "Bad Ratio": 100 * dataframe[target].value_counts()[1] / len(dataframe)}, index=["%"])

    sns.countplot(dataframe[target])
    plt.show()
    return temp


def label_encoder(dataframe):
    le = preprocessing.LabelEncoder()

    categoric_df = [col for col in dataframe.columns if dataframe[col].dtypes == "O"
                    and dataframe[col].nunique() == 2]

    for col in categoric_df:
        dataframe[col] = le.fit_transform(dataframe[col])
    return dataframe


def one_hot_encoder(dataframe, category_freq=10, nan_as_category=False):
    categorical_cols = [col for col in dataframe.columns if len(dataframe[col].value_counts()) < category_freq
                        and dataframe[col].dtypes == 'O']

    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, dummy_na=nan_as_category, drop_first=True)

    return dataframe

