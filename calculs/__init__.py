import pandas as pd
import numpy as np 
import math
import scipy.stats as sc
import matplotlib.pyplot as plt 



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

def payoff_call(S,K,prix_call): 
    pay_off = np.maximum(S-K, 0)- prix_call
    return pay_off

def payoff_put(S,K,prix_put): 
    pay_off = np.maximum(K-S, 0) - prix_put
    return pay_off

def plot_payoff(S,K,payoff,sens): 

    fig, ax = plt.subplots()
    ax.plot(S, payoff, label=f"Payoff {sens.capitalize()}", color="blue")
    ax.axhline(0, color="black", linestyle="--", linewidth=0.7)
    ax.axvline(K, color="red", linestyle="--", label="Prix d'exercice (K)")
    ax.set_title(f"Payoff du {sens.capitalize()} calculé ")
    ax.set_xlabel("Prix du sous-jacent (S)")
    ax.set_ylabel("Payoff")
    ax.legend()
    ax.grid()
    return fig

