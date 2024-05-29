import numpy as np

# Cerinta 1
def task_1(data_set):
    nr_of_columns = len(data_set.columns)
    data_types = tuple(data_set.dtypes)
    missing_values = data_set.isnull().sum()
    nr_of_lines = len(data_set)
    verify_dupe = data_set.duplicated().any()

    results = {
        'Number of columns': nr_of_columns,
        'Data types': data_types,
        'Number of missing values': missing_values,
        'Number of lines': nr_of_lines,
        'Verifying if duped lines exist': verify_dupe
    }
    return results