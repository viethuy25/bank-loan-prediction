# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:07:07 2019

@author: vieth
"""
import os
import sys

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

loan_df = pd.read_csv('data/LoanStats_2018Q2.csv', skiprows=1)

rj_loan_df = pd.read_csv('data/RejectStats_2018Q2.csv', skiprows=1)

loan_df = loan_df.drop(columns = "term")

avg_loan_amt = loan_df.loc[:, "loan_amnt"].mean()
print("Average loan amount:", avg_loan_amt)

avg_loan_amt = loan_df.loc[:, "loan_amnt"].mean()
print("Average loan amount:", avg_loan_amt)