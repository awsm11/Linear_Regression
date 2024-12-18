import numpy as np
import pandas as pd

excel_set = pd.read_excel(r'\Excel Data\quiz.xlsx')

x_axis = []

y_axis = []


for i in range(97):
    x_axis.append(excel_set["Population"][i])

    y_axis.append(excel_set["Profit"][i])


n = len(x_axis)

x_axis = np.array(x_axis)

y_axis = np.array(y_axis)




