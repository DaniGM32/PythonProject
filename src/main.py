#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
matplotlib.use('Agg')
plt.switch_backend('TkAgg')

data_set = pd.read_csv('../data/train.csv')

while True:
        print("\nMeniu:")
        print("1. Show information about the dataset coloumns")
        print("2. Show data about the passangers")
        print("3. Generate histograms based on the dataset")
        print("4. Show missing values in the dataset coloumns")
        print("5. Optiunea 5")
        print("6. Optiunea 6")
        print("7. Optiunea 7")
        print("8. Optiunea 8")
        print("9. Optiunea 9")
        print("10. Optiunea 10")
        print("0. Iesire")

        option = int(input("Pick an option: "))

        # Task 1
        if option == 1:
            print("\n Task 1: ")
            results_task1 = t1.task_1(data_set)
            for description, value in results_task1.items():
                print(description + ':', value)
                print('-' * 100)
        # Task 2
        elif option == 2:
            print("\n Task 2: ")
            results_task2 = t2.task_2(data_set)
            for description, value in results_task2.items():
                print(description + ':', value)
                print('-' * 100)

            p_men = list(results_task2.values())[5]
            p_women = list(results_task2.values())[6]

            labels = ['Men', 'Women']
            sizes = [p_men, p_women]

            fig, ax = plt.subplots()
            ax.pie(sizes, labels = labels)
            plt.show()
        # Task 3
        elif option == 3:
            print("\n Task 3: ")
            results_task3 = t3.task_3(data_set)
            for column in results_task3:
                # verific daca extrag bine coloanele numerice
                print(f'Coloana: {column}')
                print(data_set[column].dropna())
                plt.title(f'Histograma pentru pentru coloana {column}')
                plt.figure(figsize = (14, 6))
                plt.xlabel(column)
                plt.ylabel('Frecventa')
                plt.hist(data_set[column].dropna())
                plt.show()
        # Exit option
        elif option == 0:
            break
        else:
            print("You did not choose a valid option, please try again")