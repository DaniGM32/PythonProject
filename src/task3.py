import matplotlib.pyplot as plt

def task_3(data_set):
    # select the columns that are numeric
    numbers_columns = data_set.select_dtypes(include = ['int64', 'float64']).columns

    for column in numbers_columns:
        # verifying if I extract the correct columns
        print(f'Column: {column}')
        print(data_set[column].dropna())
        plt.figure(figsize = (10, 6))
        plt.title(f'Histogram for column {column}')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.hist(data_set[column].dropna(), bins=10, edgecolor='black')
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()

    return numbers_columns