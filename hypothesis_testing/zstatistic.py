""" Statistics for Hypothesis testing using proportions
by Felicity Nielson
"""



def zstat(p0, N, samp_count):
    """ Calculates Z statistic 
        z = (phat-p0)/sqrt( ( p0(1-p0) )/N ), where phat = samp_count/N

        Args:
          p0 (foat): Null hypothesis proportion
          N (int): Sample size
          samp_count (int): Positive or negative counts out of the sample population
       
        Returns:
          Calculated z statistic 
    """
    import numpy as np
    
    phat = samp_count/N
    z = (phat-p0)/np.Sqrt( (p0(1-p0)) /N )

    return z

