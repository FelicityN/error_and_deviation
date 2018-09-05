"""
Understanding data error mathematics and analysis

This script contains...
Functions for calculating error and deviation between two data lists.
    All use the standard Python library only, excpet RMSE which uses numpy.
Documentation attempting to illuminate the reasoning behind the math.

Written by Felicty Nielson, mostly for my own intituion, 
but if you find this useful, then I am happy to oblige.
"""

def print_outlim(val1, val2):
    """ Helper for printing outliers
    """
    print("Outlier found:  {} - {} = {}".format(val1, val2, abs(val1 - val2)))
    print("Outlier has been excluded from calculations")

def zero_chk(list1):
    """ Some of these formulas don't handle 0's in certain places well (e.g. diving by 0 in MAPE).
        For this reason, we raise an exception if any are found.
    """
    for x in list1:
        if x == 0:
            print("0 found in list1. MAPE can not divide by 0.")

def float_chk(list1):
    """In python 2 versions, at least one of the lists will need to be in floats (not ints)
       to ensure correct calculation.
    """
    for i, j in enumerate(list1):
        list1[i] = float(j)
    return list1

def MAE(list1, list2, outlim=None):
    """ Mean Absolute Error

    Sum(|y-y'|)/N
    
    
    The simpliest way to decide the error between measurements is to take the difference.
    Say you measure a mile and it was 4 inch off of a true mile. The 4 inch is your error.
    Whether this error is + or - often doesn't matter and can complicate analysis,
    so we take the absolute value. 
    That is the error between two values. If we have two lists and we want a single value
    to represent the error of all data, we can average them 
    (sum and divide by the total number of errors or data point comparisons).

    Args:
       list1 (list of floats) The "true" values
       list2 (list of floats) The "observed" values
       outlim (float): default None. If the difference between two elements 
         is greater than the outlier limit, print exception and exclude from error calculation. 
    """

    outlim_count = 0
    N = len(list1)
    mae = 0
    
    for i in range(0, N):
        mae += abs(list1[i]-list2[i])
        if outlim != None and mae > outlim:
            print_outlim(list1[i], list2[i])
            outlim_count += 1
    mae /= N
    
    return mae


def MAPE(list1, list2, outlim=None):
    """ Mean Absolute Percent Error

    Sum(|y-y'|/y)/N*100


    We are looking at a percent on the original or true y value,
    rather than a value of the differences of the measurement (MAE),
    which can be meaningless to the user unless they understand the scale of their data.

    For example,
    say I measure the size of giant bacteria in cm I get
    y' = [1.59, 4.37, 10.95, 6.27, 8.04, 9.29, 3.48]
    And the true vales are
    y = [1.62, 4.10, 10.81, 6.28, 8.10, 9.50, 3.47]

    The MAE is 

    Then I do the same thing but convert to mm first

    The MAE is 

    But if I use MAPE, I should get the same value for both errors 
    since the hard difference is taken as a percentage of the true measurement.
    Therefore if I use MAPE, I don't need to know what scale I'm working with.
    (Though maybe I should anway.)
    """

    zero_chk(list1)
    list1 = float_chk(list1)
    
    outlim_count = 0
    N = len(list1)
    mae = 0    
    for i in range(0, N):
        mae += abs(list1[i]-list2[i])/list1[i]
        if outlim != None and mae > outlim:
            print_outlim(list1[i], list2[i])
            outlim_count += 1
    mae = mae/N*100
    
    return mae


def MSE(list1, list2, outlim=None):
    """ Mean Squared error

    Sum((y - y')^2)/N
    
    Another way of removing the negative from errors is to square them. 
    This will convert everything to positive values without having to take the
    absolute value.

    Warning: outliers will dramatically increase the error. 
    Suggest specifying an outlim (outlier limit) value.
    """
    
    outlim_count = 0
    N = len(list1)
    mse = 0
    for i in range(0, N):
        mse += (list1[i] - list2[i])**2
        print(list1[i] - list2[i])
        if outlim != None and mae > outlim:
            print_outlim(list1[i], list2[i])
            outlim_count += 1
    mse /= N

    return mse


def RMSE(list1, list2, outlim=None):
    """ Root Mean Squared Error

    Sqrt(Sum((y - y')^2)/N)

    Warning: outliers will dramatically increase the error. 
    Suggest specifying an outlim (outlier limit) value.


    """
    
    import numpy as np 

    outlim_count = 0
    N = len(list1)
    rmse = 0
    for i in range(0, N):
        rmse += (list1[i] - list2[i])**2
        if outlim != None and mae > outlim:
            print_outlim(list1[i], list2[i])
            outlim_count += 1

    rmse = np.sqrt(rmse/N)

    return rmse
