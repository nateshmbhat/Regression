import os , sys , pandas as pd , numpy as np
from matplotlib import pyplot as plt

data = pd.DataFrame(columns=['n' , 'fibonacci']) ; 

print(data) ; 

a ,b = 0 , 1 ;
c = a+b ; 


fib = [] ; 
n = [i for i in range(100)]

for i in range(100):
    fib.append(i**2 + 4*i - 4) ; 

data = pd.DataFrame({'x' : n , 'y' : fib} , dtype=str) ; 
data = data[['x' , 'y']] ; 

print(data) ;
data.to_csv('fibonacci' , index=False) ; 





