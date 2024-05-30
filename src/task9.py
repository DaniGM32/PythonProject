import pandas as pd
import matplotlib.pyplot as plt

def task_9(data_set):
    titles = []
    # going through each row in the dataset
    for index, row in data_set.iterrows():
        # extracting the title from the name
        name_parts = row['Name'].split(',')
        title_part = name_parts[1].split('.')[0].strip()
        titles.append(title_part)
    
    # adding the column title to the dataset
    data_set['Title'] = titles
    
    # making of a new dataframe
    title_ds = data_set[['Title', 'Sex']]
    
    # counting the number of persons for each title
    title_count = {}
    for index, row in title_ds.iterrows():
        key = (row['Title'], row['Sex'])
        if key in title_count:
            title_count[key] += 1
        else:
            title_count[key] = 1
            
    plt.figure(figsize=(14, 6))
    title_counts = pd.Series([title for title in titles])
    title_counts.value_counts().plot(kind='bar', edgecolor='black', width=0.5)
    plt.title('Number of Persons for each title')
    plt.xlabel('Title')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.show()
    
    return title_count