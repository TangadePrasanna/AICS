import pandas as pd 

dataset = pd.read_csv("Salary_Data.csv")
# # print(dataset)

# data = dataset.iloc[:,0:1].values
# # print(data)

data = dataset.iloc[:,1:2].values
print(data)
