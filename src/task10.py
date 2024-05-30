import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_10(data_set):
    data_set['No relatives'] = (data_set['SibSp'] + data_set['Parch'] == 0).astype(int)
    
    no_relatives_count = data_set.groupby(['No relatives', 'Survived']).size().unstack(fill_value=0)
    
    # creating graphs for each category
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # titles for the graphs
    titles = ['Not Alone', 'Alone']
    
    # creating the pie charts
    for i, (title, ax) in enumerate(zip(titles, axes)):
        data = no_relatives_count.loc[i]
        ax.pie(data, labels=['Did not survive', 'Survived'], autopct = '%1.1f%%', startangle = 90, colors = ['blue', 'orange'])
        ax.set_title(f'Survival Status - {title}')
    plt.suptitle('Survival Status Based on Being Alone or Not')
    plt.show()

    subset = data_set.head(100)
    sns.catplot(x='Pclass', y='Fare', hue='Survived', data=subset, kind='swarm')
    plt.title('Corelation between Fare, Class and Survival Status')
    plt.xlabel('Passenger Class')
    plt.ylabel('Fare')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()

    return data_set['No relatives'].value_counts()