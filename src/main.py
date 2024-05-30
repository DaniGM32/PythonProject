#!/usr/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5
import task6 as t6
import task7 as t7
import task8 as t8
import task9 as t9
import task10 as t10

matplotlib.use('Agg')
plt.switch_backend('TkAgg')

data_set = pd.read_csv('../data/train.csv')

while True:
        print("\nMenu:")
        print("1. Show information about the dataset columns")
        print("2. Show data about the passangers")
        print("3. Generate histograms based on the dataset")
        print("4. Show missing values in the dataset columns")
        print("5. Passengers distribution by age categories")
        print("6. Men survival rate by age interval")
        print("7. Percentage of children and survival rates by age group")
        print("8. Add missing values to the dataset")
        print("9. Show the number of titles coresponding to genders in the dataset")
        print("10. Show the number of passengers that survived and died based on being alone or with family")
        print("0. Exit")

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
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.legend(loc='upper right')
            plt.show()
        # Task 3
        elif option == 3:
            print("\n Task 3: ")
            results_task3 = t3.task_3(data_set)
        # Task 4
        elif option == 4:
            print("\n Task 4: ")
            results_task4 = t4.task_4(data_set)
            for column, details in results_task4.items():
                print(f"Column: {column}\n")
                for description, value in details.items():
                    if "Percentage" in description:
                        print(f"{description}: {value:.2%}")
                    else:
                        print(f"{description}: {value}")
                print('-' * 100)
        # Task 5
        elif option == 5:
            print("\n Task 5: ")
            age_category_counts = t5.task_5(data_set.copy())
        # Task 6
        elif option == 6:
            print("\n Task 6: ")
            t6.task_6(data_set.copy())
        # Task 7
        elif option == 7:
            print("\n Task 7: ")
            percentage_children, survival_rates = t7.task_7(data_set.copy())
            print(f"Percentage of children: {percentage_children:.2f}%")
            print("Survival rates by age group:")
            print(survival_rates)
        # Task 8
        elif option == 8:
            print("\n Task 8: ")
            # I am modifying a clone of the data-set
            results_task8 = t8.task_8(data_set.copy())
            results_task8.to_csv('/root/Facultate/Sem2/PCLP3/Proiect_Final_PCLP3/data/ModifiedDataSet.csv', index=False)
            print("New dataset with filled missing values has been saved.")
            print(results_task8.head())
        # Task 9
        elif option == 9:
            print("\n Task 9: ")
            title_count = t9.task_9(data_set.copy())
        # Task 10
        elif option == 10:
            print("\n Task 10: ")
            results_task10 = t10.task_10(data_set.copy())
        # Exit option
        elif option == 0:
            break
        else:
            print("You did not choose a valid option, please try again \n")