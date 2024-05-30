import pandas as pd

def task_5(data_set):
    intervals = [0, 20, 40, 60, data_set['Age'].max()]
    # indeces for each age category
    labels = [1, 2, 3, 4]

    # adding a new column to the data set
    data_set['Age_Category'] = pd.cut(data_set['Age'], bins=intervals, labels=labels, right=False, include_lowest=True)

    # calculating the number of passengers in each age category
    age_category_counts = data_set['Age_Category'].value_counts().sort_index()

    return age_category_counts