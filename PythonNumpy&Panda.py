
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# PART 1
#1Use the pandas library to read data files: part1.csv and part2.json.to create 2 data frames.  
part1 = pd.read_csv('./part1.csv')
part1

part2 = pd.read_json('./part2.json')
part2
#2 Display the first 5 rows and the last 3 rows of both data frames.  
RowColumns1 = pd.concat([part1.head(5), part1.tail(3)])
RowColumns1
#Or part1.head(5)
     # part1.tail(3)
RowColumns2 = pd.concat([part2.head(5), part2.tail(3)])
RowColumns2
#Or part2.head(5)
   # part2.tail(3)




#3 Combine both data frames into a single one: Columns in the second data frame to the RIGHT of the first data frame.
part2 = part2.reset_index(drop=True)

#drop=True option avoids adding new index column with old index values

sidebyside = pd.concat([part1, part2], axis=1)
sidebyside

#4 Export your results as a CSV and make sure it reads back into Python properly.  

combineddf = sidebyside.to_csv('combineddf.csv', index=True)
combineddf

#Opening combined file named combineddf
combineddf = pd.read_csv('./combineddf.csv', keep_default_na=False, na_values=[""])
combineddf

#Getting rid of 'unnamed: 0' column
combineddf.drop(combineddf.filter(regex="Unnamed: 0"),axis=1, inplace=True)

#5 Show the list of columns in your data frame.  
ColumnsList = list(combineddf)
ColumnsList

#6 Do you find any duplicated columns? Display the first 5 rows of your data, is your data accurate?  
duplicateColumnNames = combineddf.columns.duplicated()
duplicateColumnNames

NewRows = combineddf.head()
NewRows

#7 Use merge from the pandas package to make an inner join.
merged_innerjoin = pd.merge(part1, part2, on='species_id', how = "inner")
merged_innerjoin

#8 Fill the missing value for the column weight by the mean  
merged_innerjoin.fillna(merged_innerjoin.mean(),inplace =True)
merged_innerjoin.head()

#PART2
#9 Plot the distribution of taxa by plot

merged_innerjoin[['taxa','plot_id']].groupby(["plot_id"]).nunique().plot(kind = 'bar')

plt.legend(loc = 'best',bbox_to_anchor=(0.4, 1.2))
plt.show()


#10 Plot the distribution of taxa by sex by plot 
merged_innerjoin['sex'].isna().sum()
merged_innerjoin['sex'].value_counts()
merged_innerjoin['sex'] = merged_innerjoin['sex'].fillna('M')
group_tax_sex = merged_innerjoin [['plot_id','taxa','sex']].groupby(["plot_id", "sex"]).nunique()
tax_by_sex = group_tax_sex .pivot_table(values='taxa',columns = 'sex', index = 'plot_id')
tax_by_sex.plot(kind = 'bar')
plt.legend(loc = 'best',bbox_to_anchor=(0.2, 1.2))
plt.show()

#11
#Asnwer In the document