import pandas as pd
import numpy as np

# Your excel file location
excel_set = pd.read_excel(r'\Excel Data\data.xlsx')

# Result of your input, this is the target
target_data = []
# range could be changed with respect to your data count in your excel file
for i in range(20):
    target_data.append(excel_set["Sales"][i])

target_data = np.array(target_data)

# Value you want to predict its result
data = []
# range could be changed with respect to your data count in your excel file

for i in range(20):
    data.append(excel_set["Total Premium"][i])

data = np.array(data)