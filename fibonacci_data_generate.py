import os , sys , pandas as pd , numpy as np
from matplotlib import pyplot as plt

data = pd.DataFrame(columns=['n' , 'fibonacci']) ; 

print(data) ; 

a ,b = 0 , 1 ;
c = a+b ; 


fib = [] ; 
n = [i for i in range(30)]

for i in range(30):
    fib.append(a) ; 
    a, b= b , c ;
    c = a+b ; 

data = pd.DataFrame({'x' : n , 'y' : fib} , dtype=str) ; 
data = data[['x' , 'y']] ; 

print(data) ;
data.to_csv('fibonacciData' , index=False) ; 