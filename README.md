A self-project to practice and have a deeper understanding of cleaning excel data source and analysis data.

**This dataset belongs to 2018 quater 2, obtaining from online**

Based on the following numbers abstraact from the dataset, it can be seen that the main there are several main differences between the two sides:
  _ Accepted loanees usually have higher income and stable jobs than rejected ones.
  _ Loan amount does not varies between both sides, hence jobs stability and income are the two main factors.
  _ Cannot dropna from the beginnning as there are many records with missing some features. Hence, we will fillna() with previous record.

**Result from analysis**

==========Approve loan========= <br />
Top jobs to qualify for a loan, regardless of emp_length:
1)	Teacher
2) 	Manager
3)	Owner
4)	Driver
5)	Register Nurse
6) 	RN

Interestingly, after check mean emp_length, it does not seem to have heavy impact on ranking as: <br/>
_ Highest mean emp_length belongs to rank B,D and E for top 6 jobs

Instead, annual_inc is what seems to affect ranking the most: <br/>
_ Except for rank D and E with some of the times peak, most jobs annual income will affect their ranking from A to F in descending order <br/>
_ For jobs with average salary below 70k likes Teacher, there seems to have no peak at D and E likes high income jobs like Owner or Register Nurse<br/>

==========Reject loan========= <br />
Average reject loan amount: 12,515.383107916085 <br />
Average reject employment length: 0.11361334536236832 years <br />
Average reject debt-to-income ratio: 1.1929799359893136 <br /><br />


_ For people with the same job title, their loan classification does not correlate with annual income as grade C has the highest annual income while grade E has the lowest one.
_ The same is for debt-to-income ratio. Hence, the grade is not based on one category only.

---------------------------------------------------------------------------------------------
_ There are 2 loan with no interest rate (init_rate) in approved loan. With further look, it seems to be empty rows, which is likely due to data entry mistakes.
<br />

## Result 
_ The Naive Bayes approach based on 'loan_amnt','grade','home_ownership', 'annual_inc','verification_status' featuers has an accuracy score of only 0.2956199914357374, which is not very accurate.
_ The K-means clustering perform even worses with an accuracy score of only 0.20119442702677903 on the same features.
_ 

