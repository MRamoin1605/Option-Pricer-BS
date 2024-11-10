import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import math
import scipy.stats as sc



def pricing_call(S, K, T, r, sigma):
    # Calcul de d1 et d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    # Calcul du prix du call
    call_price = S * sc.norm.cdf(d1) - K * math.exp(-r * T) * sc.norm.cdf(d2)

    return call_price


def pricing_put(S, K, T, r, sigma):
    # Calcul de d1 et d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    # Calcul du prix du pu 
    put_price = K * math.exp(-r * T) * sc.norm.cdf(-d2) - S * sc.norm.cdf(-d1) 

    return put_price

