def task_3(data_set):
    # select the columns that are numeric
    numbers_columns = data_set.select_dtypes(include = ['int64', 'float64']).columns
    return numbers_columns