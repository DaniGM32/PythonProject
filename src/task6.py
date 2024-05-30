import pandas as pd
import matplotlib.pyplot as plt

def task_6(data_set):
    intervals = [0, 20, 40, 60, data_set['Age'].max()]
    labels = [1, 2, 3, 4]

    # creating a new column to store the age category
    data_set['Age_Interval'] = pd.cut(data_set['Age'], bins=intervals, labels=labels, right=False, include_lowest=True)
    male_passengers = data_set[data_set['Sex'] == 'male']

    survivors = male_passengers.groupby('Age_Interval')['Survived'].sum()
    total = male_passengers.groupby('Age_Interval')['Survived'].count()
    survival_data = (survivors / total) * 100

    survival_data = survival_data.reset_index(name='Survival_Rate')

    # the graph
    plt.figure(figsize=(10, 6))
    plt.bar(survival_data['Age_Interval'], survival_data['Survival_Rate'], edgecolor='black', width=0.5)
    plt.title('Survival Rate of Male Passengers by Age Interval')
    plt.xlabel('Age Interval')
    plt.ylabel('Survival Rate (%)')
    plt.xticks(ticks=range(len(labels) + 1), labels=['0', '0-20', '21-40', '41-60', '61+'])
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

    return survival_data