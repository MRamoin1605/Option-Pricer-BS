import pandas as pd
import numpy as np 
import math 
import streamlit as st 
import datetime 
from calculs import *

st.title("Pricing d'une option en utilisant Black-Scholes")

with st.form("Variables"):
     st.write("Veuillez insérer les variables pour le calcul de l'option :")
     sens = st.radio("Choisissez le sens de l'option pricé: ", ("Call 📈", "Put 📉"))
     S = st.number_input("Prix du sous-jacent: ", value=None, placeholder="Type a number...")
     k = st.number_input("Strike: ", value=None, placeholder="Type a number...")
     date_echeance = st.date_input("Date d'échéance de l'option", value=datetime.datetime.today())
     T = ((date_echeance - datetime.datetime.today().date()).days)/ 365
    
     r = st.number_input("Taux sans risque: ", value=0.00, placeholder="En pourcentage...")/100
     vol = st.number_input("Volatilité annuelle du sous-jacent ", value=0.00, placeholder="En pourcentage...")/100
     quantite =st.number_input("Quantité ", value= 1 ,placeholder="En pourcentage...")

     
     submitted = st.form_submit_button("Calculer le prix de l'option")
     if submitted:
        if sens == "Call 📈":
            prix_call = pricing_call(S, k, T, r, vol) * quantite
            st.write(f"Le prix du call pour les variables données est de : **{prix_call:.2f}  €**")
        if sens == "Put 📉":
            prix_put = pricing_put(S, k, T, r, vol) *quantite
            st.write(f"Le prix du call pour les variables données est de : **{prix_put:.2f}  €**")
    
st.subheader("Payoff de l'option pricé :")

if submitted:
    S_payoff = np.linspace(0, k*2, 100)

    if sens == "Call 📈":
        sens = "Call"
        payoff = payoff_call(S_payoff,k,prix_call)  
        st.pyplot(plot_payoff(S_payoff,k,payoff,sens))         
    if sens == "Put 📉":
        sens = "Put"
        payoff = payoff_put(S_payoff,k,prix_put)  
        st.pyplot(plot_payoff(S_payoff,k,payoff,sens))
    
