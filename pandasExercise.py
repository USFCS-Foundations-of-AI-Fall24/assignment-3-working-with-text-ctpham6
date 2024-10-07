import numpy as np

import pandas as pd


# Write a function that will read in the breast cancer dataset and print out the classification column, which is the left-most column.
def view_classifications(data) :
    table = pd.read_csv(data)
    print(table['no-recurrence-events'])

# Write a function that computes ZeroR (the most common classification) for the breast cancer data. (either 'recurrence-events' or 'no-recurrence-events')
def compute_zeroR(data) :
    table = pd.read_csv(data)
    print(table['no-recurrence-events'].value_counts().idxmax())

# Write a function that determines the most common value for age and menopause for patients with recurrences.

# Write a function that plots the number of recurrences for each age group.

view_classifications('breast-cancer.data')
print("-----------------------------")
compute_zeroR('breast-cancer.data')