import os , sys , pandas as pd , numpy as np
from matplotlib import pyplot as plt

data = pd.DataFrame(columns=['n' , 'fibonacci']) ; 

print(data) ; 

a ,b = 0 , 1 ;
c = a+b ; 


fib = [] ; 
n = [i for i in range(100)]

for i in range(100):
    fib.append(a) ; 
    a , b  = b , c ; 
    c = a+b ; 

data = pd.DataFrame({'n' : n , 'fib' : fib} , dtype=str) ; 
data = data[['n' , 'fib']]

print(data) ;
data.to_csv('fibonacci' , index=False) ; 





