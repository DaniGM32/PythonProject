def task_4(data_set):
    all_values = data_set.isnull().sum()
    missing_values = all_values[all_values > 0]

    results = {}
    for column in missing_values.index:
        total_missing = missing_values[column]
        percentage = total_missing / len(data_set)
        
        survivors_rows = data_set[data_set['Survived'] == 1]
        survivors_column = survivors_rows[column]
        survivors_missing = survivors_column.isnull().sum()

        dead_rows = data_set[data_set['Survived'] == 0]
        dead_column = dead_rows[column]
        dead_missing = dead_column.isnull().sum()
        
        # calculez procentajele de valori care lipsesc pt fiecare categorie
        survivors_percentage = survivors_missing / len(data_set[data_set['Survived'] == 1])
        dead_percentage = dead_missing / len(data_set['Survived'] == 0)

        results[column] = {
            'Number of missing values': total_missing,
            'Percentage of missing values': percentage,
            'Number of missing values for survivors': survivors_missing,
            'Percentage of missing values for survivors': survivors_percentage,
            'Number of missing values for dead people': dead_missing,
            'Percentage of missing values for dead peole': dead_percentage
        }
    return results