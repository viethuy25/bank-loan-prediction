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

print ("\n")
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

loan_approval = len (loan_df)
print ("Approved loans:",loan_approval)

print ("\n")
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

loan_denied = len (rj_loan_df)
print ("Denied loans:",loan_denied)

print ("\n")
#Re-engineer ranking loanee
over_view_df = loan_df.groupby("grade").id.nunique()
print ("Approved loanee")
print (over_view_df)

#Draw overview, as seen the majority of loanee are A,B and C with over 70% loans in estimation
over_view_df.plot.bar()

#Grade A group
A_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#A_loan_df = pd.DataFrame({'Occupation':A_loan_series.index, 'mean':A_loan_series.values})
print(A_loan_series)

print ("\n")
#Grade B group
B_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'B'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#B_loan_df = pd.DataFrame({'Occupation':B_loan_series.index, 'count':B_loan_series.values})
print(B_loan_series)

print ("\n")
#Grade C group
C_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'C'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#C_loan_df = pd.DataFrame({'Occupation':C_loan_series.index, 'count':C_loan_series.values})
#print(C_loan_df.sort_values(by='count',ascending = False).head(10)['Occupation'])
print (C_loan_series)
print ("\n")
#Grade D group
D_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'D'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#D_loan_df = pd.DataFrame({'Occupation':D_loan_series.index, 'count':D_loan_series.values})
#print(D_loan_df.sort_values(by='count',ascending = False).head(10)['Occupation'])
print(D_loan_series)
print ("\n")
#Grade E group
E_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'E'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#E_loan_df = pd.DataFrame({'Occupation':E_loan_series.index, 'count':E_loan_series.values})
#print(E_loan_df.sort_values(by='count',ascending = False).head(10)['Occupation'])
print(E_loan_series)
print ("\n")
#Grade F group
F_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'F'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#F_loan_df = pd.DataFrame({'Occupation':F_loan_series.index, 'count':F_loan_series.values})
#print(F_loan_df.sort_values(by='count',ascending = False).head(10)['Occupation'])
print(F_loan_series)
print ("\n")
#Grade G group
G_loan_series = loan_df.loc[loan_df["grade"] == 'A'].loc[loan_df["emp_title"] == "Manager"]["loan_amnt"].mean()/loan_df.loc[loan_df["grade"] == 'G'].loc[loan_df["emp_title"] == "Manager"]["annual_inc"].mean()
#G_loan_df = pd.DataFrame({'Occupation':G_loan_series.index, 'count':G_loan_series.values})
#print(G_loan_df.sort_values(by='count',ascending = False).head(10)['Occupation'])
print(G_loan_series)
print ("\n")


#Prediction analysis
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X = loan_df[['annual_inc', 'loan_amnt', 'emp_length']]
print (X.dtypes)
y = loan_df['grade']
X_train, X_test, y_train, y_test = train_test_split (X,y, test_size = 0.2)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)