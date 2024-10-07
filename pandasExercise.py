import pandas as pd
import numpy as np


# Write a function that will read in the breast cancer dataset and print out the classification column, which is the left-most column.
def view_classifications(data) :
    table = pd.read_csv(data)
    print(table['no-recurrence-events'])

# Write a function that computes ZeroR (the most common classification) for the breast cancer data. (either 'recurrence-events' or 'no-recurrence-events')
def compute_zeroR(data) :
    table = pd.read_csv(data)
    print(table['no-recurrence-events'].value_counts().idxmax())

# Write a function that determines the most common value for age and menopause for patients with recurrences.
def compute_common_age_menopause(data) :
    table = pd.read_csv(data)
    data_frame = pd.DataFrame(table)
    filtered_table = data_frame[data_frame['no-recurrence-events'] == 'recurrence-events']
    print("Out of all the patients with recurrences...")
    print(filtered_table['30-39'].value_counts().idxmax(), "is the most common age")
    print(filtered_table['premeno'].value_counts().idxmax(), "is TECHNICALLY the most common menopause value")
    print("If we exclude premenopause patients...")
    filtered_table = filtered_table[filtered_table['premeno'] != "premeno"]
    print(filtered_table['premeno'].value_counts().idxmax(), "is the most common menopause")

# Write a function that plots the number of recurrences for each age group.
def plot_age_recurrences(data):
    table = pd.read_csv(data)
    data_frame = pd.DataFrame(table)
    filtered_table = data_frame[data_frame['no-recurrence-events'] == 'recurrence-events']
    print("The following is the amount of age groups that have recurrences:")
    print(filtered_table['30-39'].value_counts())

view_classifications('breast-cancer.data')
print("-----------------------------")
compute_zeroR('breast-cancer.data')
print("-----------------------------")
compute_common_age_menopause('breast-cancer.data')
print("-----------------------------")
plot_age_recurrences('breast-cancer.data')
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
