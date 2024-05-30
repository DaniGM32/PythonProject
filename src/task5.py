import pandas as pd
import matplotlib.pyplot as plt

def task_5(data_set):
    intervals = [0, 20, 40, 60, data_set['Age'].max()]
    # indeces for each age category
    labels = [1, 2, 3, 4]

    # creating a new column to store the age category
    data_set['Age_Interval'] = pd.cut(data_set['Age'], bins=intervals, labels=labels, right=False, include_lowest=True)

    # calculating the number of passengers in each age category
    age_category_counts = data_set['Age_Interval'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    age_category_counts.plot(kind='bar')
    plt.title('Distribution of Passengers by Age Categories')
    plt.xlabel('Age Categories')
    plt.ylabel('Number of Passengers')
    plt.xticks(ticks=range(len(labels) + 1), labels=['0', '0-20', '21-40', '41-60', '61+'], rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

    return age_category_counts