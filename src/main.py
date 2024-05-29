#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import task1 as t1
matplotlib.use('Agg')
plt.switch_backend('TkAgg')

data_set = pd.read_csv('../data/train.csv')

# Task 1
print("Task 1: ")
results_task1 = t1.task_1(data_set)
for description, value in results_task1.items():
    print(description + ':', value)
    print('-' * 100)
