"""
Created on Mon Jul  8 12:07:07 2019

@author: vieth
"""
import os
import sys

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LogisticRegression

loan_df = pd.read_csv('data/LoanStats_2018Q2.csv', skiprows=1, skipfooter = 2)
# Normalize data
loan_df = loan_df.fillna(0)

rj_loan_df = pd.read_csv('data/RejectStats_2018Q2.csv', skiprows=1, skipfooter = 2)
#Normalize data
rj_loan_df = rj_loan_df.fillna(0)

loan_df = loan_df.drop(columns = "term")

print ("==========Approve loan=========")

avg_loan_amt = loan_df.loc[:, "loan_amnt"].mean()
print("Average loan amount:", avg_loan_amt)

avg_length_amt = loan_df.loc[:, "term_months"].mean()
print("Average length:", avg_length_amt, "months")

avg_annual_inc_amt = loan_df.loc[:, "annual_inc"].mean()
print("Average annual incom amount:", avg_annual_inc_amt)

# Transform employment length into a clear structure
# Assume all n/a is 0, and all length less then 1 years is 0
loan_df['emp_length'] = loan_df['emp_length'].replace("< 1 year", '0 year')
loan_df['emp_length'] = loan_df['emp_length'].replace(0, '0 year')

#remove "years" out of column emp_length
loan_df['emp_length'] = loan_df['emp_length'].apply(lambda x: int(x[0]))

avg_emp_length_amt = loan_df.loc[:, "emp_length"].mean()
print("Average employment length:", avg_emp_length_amt, "years")

avg_debt_inc_ratio = avg_loan_amt/avg_annual_inc_amt
print("Average debt-to-income ratio:", avg_debt_inc_ratio)


# Do the same manupilation for reject
print ("==========Reject loan=========")
avg_rj_loan_amt = rj_loan_df.loc[:, "Amount Requested"].mean()
print("Average reject loan amount:", avg_rj_loan_amt)

# Transform employment length into a clear structure
# Assume all n/a is 0, and all length less then 1 years is 0
rj_loan_df['Employment Length'] = rj_loan_df['Employment Length'].replace("< 1 year", '0 year')
rj_loan_df['Employment Length'] = rj_loan_df['Employment Length'].replace(0, '0 year')

#remove "years" out of column emp_length
rj_loan_df['Employment Length'] = rj_loan_df['Employment Length'].apply(lambda x: int(x[0]))

avg_rj_emp_length_amt = rj_loan_df.loc[:, "Employment Length"].apply(lambda x: int(x)).mean()
print("Average reject employment length:", avg_rj_emp_length_amt, "years")

avg_rj_debt_inc_ratio = rj_loan_df.loc[:, "debt-to-inc ratio"].mean()
print("Average reject debt-to-income ratio:", avg_rj_debt_inc_ratio)


# A surface look of data
print ("==========Approve loan data=========")
min_len_emp = loan_df.sort_values('emp_length')
min_loan_amt = loan_df.sort_values('loan_amnt')

loan_df['dti'] = loan_df.apply(lambda row: float(row[1])/float(row[12]) if row[12] > 0 else 0, axis = 1)
min_debt_to_income_ratio = loan_df.sort_values('dti')

#Logistic regression model
lite_loan_df = loan_df[['loan_amnt','emp_length','dti']]
lite_rj_loan_df = rj_loan_df[['Amount Requested', 'Employment Length', 'debt-to-inc ratio', ]]

lite_loan_df['loan_amnt'] = lite_loan_df['loan_amnt'].astype(int)
lite_loan_df['dti'] = lite_loan_df['dti'].map('{:,.4f}'.format)

Y = lite_rj_loan_df.head(1)
print (lite_loan_df)
print(Y)

logreg = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')
logreg.fit(lite_loan_df, Y)