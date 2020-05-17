import pandas as pd

from sklearn.linear_model import LinearRegression 


emp = pd.read_csv(r'C:\Users\DELL\Desktop\employee.csv')

print(emp)
print(emp.info())
print(emp.describe())

print(emp.corr())
'''
               eid       exp    salary  skillset
eid       1.000000  0.282574  0.295132  0.336670
exp       0.282574  1.000000  0.990589  0.885479
salary    0.295132  0.990589  1.000000  0.874573
skillset  0.336670  0.885479  0.874573  1.000000

-1               : negative correlation

     > -.40   between <.40   :  no correlation
0      : no corelation
1      : positive corelation

'''

da = emp[['exp','skillset','salary']]
print(da.corr())


###split data : x, y
## x  = exp, skillset  (input or independnet column)
## y  = salary ( response, dependent column)

da = da.values
print(da)
print(da[:,0:2])



print(da[:,2])

import numpy as np
x = np.array(da[:,0:2],dtype=float)
y = np.array(da[:,2],dtype=float)



#LinearRegression :  sklearn (is module)
#pip install sklearn

o = LinearRegression()
o.fit(x,y)#

##prediction :
new_exp = []
new_skill = []
nd = []

for i in range(3):
    e = float(input('enter exp :'))
    s = float(input('enter skill level :'))
    #new_exp.append(e)
    #new_skill.append(s)
    nd.append([e,s])

nd = np.array(nd)


##predict
print(o.predict(nd))








    

    
    

    























