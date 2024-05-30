import pandas as pd
import matplotlib.pyplot as plt

def task_7(data_set):
    # defining the age groups
    data_set['Age_Group'] = data_set['Age'].apply(lambda x: 'Child' if x < 18 else 'Adult')

    # calculating the percentage of children
    total_children = data_set[data_set['Age_Group'] == 'Child'].shape[0]
    total_passengers = data_set.shape[0]
    percentage_children = (total_children / total_passengers) * 100

    # calculating the survival rates by age group
    survival_rates = data_set.groupby('Age_Group')['Survived'].mean() * 100

    # the graph
    plt.figure(figsize=(10, 6))
    survival_rates.plot(kind='bar', edgecolor='black', width=0.5)
    plt.title('Survival Rates by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Survival Rate (%)')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

    return percentage_children, survival_rates