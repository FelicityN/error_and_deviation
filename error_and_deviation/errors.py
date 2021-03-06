"""
Understanding data error mathematics and analysis

This script contains...
Functions for calculating error and deviation between two or one data lists.
    All expressions use the standard Python library only, except rmse which also uses numpy.
Documentation attempting to illuminate the reasoning behind the math.
Standard Deviation can be calculated specifying form='rmse' and list2 == None

Written by Felicty Nielson, mostly for my own intituion, 
but if you find this useful, then I am happy to oblige.
"""

def print_outlim(val1, val2):
    """ Helper for printing outliers
    """
    print("Outlier found:  |{} - {}| = {}".format(val1, val2, abs(val1 - val2)))
    print("Outlier has been excluded from calculations")

def zero_chk(list1):
    """ Some of these formulas don't handle 0's in certain places well (e.g. diving by 0 in MAPE).
        For this reason, we raise an exception if any are found.
    """
    for x in list1:
        if x == 0:
            print("0 found in list1. MAPE can not divide by 0.")

def float_chk(list1):
    """ In python 2 versions, at least one of the lists will need to be in floats (not ints)
        to ensure correct calculation.
    """
    for i, j in enumerate(list1):
        list1[i] = float(j)
    return list1


def mean_list(list1, N):
    """ Helper function calculates mean and returns list of N means
    """
    ave = 0
    for i in list1:
        ave += i
    ave /= N
    lista = [ave for x in range(0,N)]
    return lista

def errors(form, list1, list2=None, deviation=False, outlim=0):
    """ Function for calculating error and deviation between two or one data lists. 
        Lists must be of same length and the elements of the first list corresponding 
        to the elements of the second.
        Args:
          form  (string): Mathematical formula for calculating error.
                          Availiable formulas are either 'mae', 'mape', 'mse', or 'rmse'
          deviation  (bool): default False. If specifying only one list, deviation is automatic.
                             If specifying two lists, deviation of the second list is measured off of 
                             the mean of the first.
          list1 (list of floats): The "true" values
          list2 (list of floats): The "observed" values. Default None. 
                                  If None, the deviation of list1 is calculated.
          outlim (float): default 0 equivalent to None. If the difference between two elements 
                          is greater than the outlier limit, print exception and exclude from 
                          error calculation.  
        Returns:
          err (int): The computed error or deviation.
    """
    import numpy as np
    
    list1 = float_chk(list1)

    outlim_count = 0
    error = 0
    N = len(list1)


    # Determine if calculating error or deviation. If calculating deviation, build mean list.
    if list2 != None and deviation == False:
        print("Calculating error...")
    else:
        print("Calculating deviation...")
        if list2 == None:
            list2 = mean_list(list1, N)
        elif deviation == True:
            list1 = mean_list(list1, N)
    
    for i in range(0, N):
        if form == 'mae':
            err = abs(list1[i]-list2[i])
            """ Mean Absolute Error (MAE)

            Sum(|y-y'|)/N

            The simpliest way to decide the error between measurements is to take the difference.
            Say you measure a mile and it was 4 inch off of a true mile. The 4 inch is your error.
            Whether this error is + or - often doesn't matter and can complicate analysis,
            so we take the absolute value. 
            That is the error between two values. If we have two lists and we want a single value
            to represent the error of all data, we can average them 
            (sum and divide by the total number of errors or data point comparisons).

            To calculate deviation, we modify the formula to subtract the mean of one list from the values
            of another list. This lets us know how far the observed values are deviating from the true average.
            Or we can subtract the values of one list from the mean of the same list. This measures how 
            much the data deviates from its own average.
            
            Standard deviation uses RMSE (or rather, RMSD...). See the 'rmse' condition below.
            """

            
        elif form  == 'mape':
            zero_chk(list1)    
            err = abs(list1[i]-list2[i])/list1[i]
            """ Mean Absolute Percent Error (MAPE)

            Sum(|y-y'|/y)/N*100

            We are looking at a percent on the original or true y value,
            rather than a value of the differences of the measurement (MAE),
            which can be meaningless to the user unless they understand the scale of their data.

            For example,
            say I measure the size of giant bacteria in cm I get
            y' = [1.59, 4.37, 10.95, 6.27, 8.04, 9.29, 3.48]
            And the true vales are
            y = [1.62, 4.10, 10.81, 6.28, 8.10, 9.50, 3.47]

            The MAE is 0.104285714285714

            Then I do the same thing but convert to mm first

            The MAE is 104.285714285714

            But if I use MAPE, I get the same value for both errors (1.828204390849)
            since the hard difference is taken as a percentage of the true measurement.
            Therefore if I use MAPE, I don't need to know what scale I'm working with, 
            at least for this purpose.
            """

            
        elif form == 'mse' or form == 'rmse':
            err = (list1[i] - list2[i])**2
            """ Mean Squared Error (MSE)

            Sum((y - y')^2)/N

            Another way of removing the negative from errors is to square them. 
            This will convert everything to positive values without having to take the
            absolute value.

            --------

            Root Mean Squared Error (RMSE)

            Sqrt(Sum((y - y')^2)/N)

            Specifying only one list will result in the Standard Deviation (SD).

            Warning: outliers will dramatically increase the error for MSE and RMSE. 
            Suggest specifying an outlim (outlier limit) value.
            """

            
        else:
            print("form should be 'mae', 'mape', 'mse', or 'rmse'")
        
        if outlim != 0 and abs(list1[i]-list2[i]) > outlim:
            print_outlim(list1[i], list2[i])
            outlim_count += 1
        else:
            error += err

    error /= (N - outlim_count)        
    if form == 'mape':
        error *= 100
    elif form == 'rmse':
        error = np.sqrt(error)
        
    
    return error
