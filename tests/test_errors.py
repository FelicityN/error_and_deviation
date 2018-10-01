""" Tests error and deviation
"""

import pytest
import numpy as np

def test_errors():
    import errors as er
    list1 = [0.5, 3, 4, 5, 6, 7, 10, 3, 0.6, 5.2]
    list2 = [1, 0, 2, 16, 5.5, 6.7, 11, 3.5, .5, 18]

    out = 10

    # test errors
    mae = er.errors('mae', list1, list2=list2, outlim=out)
    assert mae == pytest.approx(0.9875)

    mape = er.errors('mape', list1, list2=list2, outlim=out)
    assert mape == pytest.approx(38.244, 0.00001)

    mse = er.errors('mse', list1, list2=list2, outlim=out)
    assert mse == 1.85625

    rmse = er.errors('rmse', list1, list2=list2, outlim=out)
    assert rmse == pytest.approx(1.36244, 0.00001)

    
    # test deviation of one list
    

    # test deviation of two lists    
