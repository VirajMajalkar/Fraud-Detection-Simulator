#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import time

st.title("Credit Card Outliers")

uploaded_file = st.file_uploader("Upload card transaction file")

try :

    def cust_data_analysis(self):

        credit_card_df = pd.read_csv(uploaded_file, names=['AccountId', 'MerchantId', 'TransactionAmount', 'Extra'])

        credit_card_df['TransactionAmount'] = credit_card_df['TransactionAmount'].replace(['X'], 'NaN')

        credit_card_df['TransactionAmount'] = credit_card_df['TransactionAmount'].astype(float)

        cc_tran_df = credit_card_df[['AccountId', 'TransactionAmount']]

        st.write(cc_tran_df.groupby(['AccountId']).agg(['count', 'mean', 'std']).sort_values(by=('TransactionAmount', 'count'), ascending=False))
        
        return cc_tran_df

    if st.button("Read a File"):
        
        cust_data_analysis('self')


    def anamoly_detection(self):

        cc_tran_df = cust_data_analysis('self')
        st.write("Enter new transaction details")
        
        inp_acct = int(st.number_input("Enter an Account No : "))
        inp_amt = float(st.number_input("Enter an amount : "))
        
        acct_tran_count = float(cc_tran_df.groupby(['AccountId']).count().loc[inp_acct])
        lower_circuit = cc_tran_df.groupby(['AccountId']).mean() - 3 * cc_tran_df.groupby(['AccountId']).std()
        upper_circuit = cc_tran_df.groupby(['AccountId']).mean() + 3 * cc_tran_df.groupby(['AccountId']).std()

        if acct_tran_count > 5:

            st.write("Lower circuit transaction amount for Account Id",
                  inp_acct, "is = ", float(lower_circuit.loc[inp_acct]))
            st.write("Upper circuit transaction amount for Account Id",
                  inp_acct, "is = ", float(upper_circuit.loc[inp_acct]))

            if inp_amt < float(lower_circuit.loc[inp_acct]) or inp_amt > float(upper_circuit.loc[inp_acct]):

                st.write("Suspicious transaction detected")

            else:

                st.write("Transaction amount within normal range")

        else:

            st.write("No Historic data present")

    anamoly_detection('self')
    
except:

    pass