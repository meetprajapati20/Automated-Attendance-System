import pandas as pd
import numpy as np

arr=['A','P','P','A']
arr=np.array(arr)
file=('temp.xlsx')
df=pd.read_excel(file)
df.insert(-1,"Attendance",np)
df.to_excel('temp.xlsx')