import numpy as np

def task_2(data_set):
    # with groupby() you can group data by the values of a column
    # calculating the nnumber of valous 0 and 1 in the 'Survived' column
    people = data_set.groupby(data_set.columns[1]).size()
    dead = people.get(0, 0)
    survivors = people.get(1, 0)
    
    classes = data_set.groupby(data_set.columns[2]).size()
    first_class = classes.get(1, 0)
    second_class = classes.get(2, 0)
    third_class = classes.get(3, 0)
    people = dead + survivors

    p1 = round(first_class / people * 100, 3)
    p2 = round(second_class / people * 100, 3)
    p3 = round(third_class / people * 100, 3)

    genders = data_set.groupby(data_set.columns[4]).size()
    men = genders.get('male', 0)
    women = genders.get('female', 0)
    p4 = round(men / people * 100, 3)
    p5 = round(women / people * 100, 3)
    results = {
        'People who died': dead,
        'People who survived': survivors,
        'Percentage of people with a first class ticket': p1,
        'Percentage of people with a second class ticket': p2,
        'Percentage of people with a third class ticket': p3,
        'Percentage of men': p4,
        'Percentage of women': p5
    }
    return results