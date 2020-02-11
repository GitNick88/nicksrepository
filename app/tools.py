import numpy as np
from sklearn.model_selection import train_test_split

def test():
    print('hello')


def train_val_test_split(df):
    """
    train/val/test split function
    """
    train, test = train_test_split(df, test_size=0.2)
    train, val = train_test_split(df, test_size=0.2)
    print('Train:', train.shape)
    print('Val:', val.shape)
    print('Test:', test.shape)
    return train, val, test


def null_sum(df):
    """
    function to check for sum of null values
    """
    sum_total = df.isnull().sum()
    if sum_total.sum() == 0:
      print('You have no nulls to worry about!')
    if sum_total.sum() <= 200 and sum_total.sum() > 1:
      print('You have some data cleaning to do! ')
    if sum_total.sum() >= 201:
      print('This is one dirty dataset...')
    print('Total nulls per column:\n', sum_total)
