import pandas as pd

def task_8(data_set):
    # Extracting the numeric and categorical columns
    numeric_columns = data_set.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_columns = data_set.select_dtypes(exclude=['int64', 'float64']).columns.tolist()

    # Processing numeric columns
    for column in numeric_columns:
        is_null = data_set[column].isnull().sum()
        if is_null > 0:
            i = 0
            while i <= 1:
                # Selecting the rows that correspond to the survival class and have missing values
                false_survivors = (data_set['Survived'] == i) & (data_set[column].isnull())
                mean_val = data_set[data_set['Survived'] == i][column].mean()
                data_set.loc[false_survivors, column] = mean_val
                i += 1

    # Processing categorical columns
    for column in categorical_columns:
        is_null = data_set[column].isnull().sum()
        if is_null > 0:
            j = 0
            while j <= 1:
                # Selecting the rows that correspond to the survival class and have missing values
                false_survivors = (data_set['Survived'] == j) & (data_set[column].isnull())
                mode_val = data_set[data_set['Survived'] == j][column].mode()[0] if not data_set[data_set['Survived'] == j][column].mode().empty else None
                data_set.loc[false_survivors, column] = mode_val
                j += 1
    return data_set