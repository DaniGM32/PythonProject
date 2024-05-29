def task_3(data_set):
    # selectez toate coloanele care contin valori numerice si le prelucrez in main
    numbers_columns = data_set.select_dtypes(include = ['int64', 'float64']).columns
    return numbers_columns