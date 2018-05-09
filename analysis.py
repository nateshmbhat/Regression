import pandas as pd ; 
import numpy as np ; 
from matplotlib import pyplot as plt ; 
import os , sys , subprocess , time  ; 


class fibonacii:

    def __init__(self):
        self.hypothesis = "fib(n) = w1 * x1^2  + w2 * x1 + b"
        self.w1 =  np.random.uniform() ;
        self.w2 = np.random.uniform() ; 
        self.b = np.random.uniform() ; 
        self.data = np.genfromtxt('./quadraticData' , delimiter=',' , dtype='int') ; 
        self.features = self.data[: , 0] ; 
        self.target = self.data[: , 1]
        self.alpha = 0.00000000032389329 ;
    
    def __update_hyp__(self):
        self.hyp = self.get_hyp() ; 
        pass ;  

    def get_hyp(self):
        return self.w1 * self.features**2 + self.w2 * self.features + self.b  ;

    
    def cost(self):
        return ((self.hyp-self.target)**2).mean() ; 
    
    def train(self):
        for counter in range(100000):
            self.__update_hyp__() ;

            old_cost = self.cost() ; 
            

            for row in range(self.features.shape[0]):
                dcost_dhyp = 2*(self.hyp[row] - self.target[row]) ;
                dhyp_dw1 = self.features[row]**2  ;
                dhyp_dw2 = self.features[row] ; 
                
                self.w1 -= self.alpha * dcost_dhyp * dhyp_dw1 ;
                self.w2 -= self.alpha * dcost_dhyp * dhyp_dw2 ; 
                self.b -= self.alpha * dcost_dhyp * 1 ; 
            
            new_cost = self.cost() ; 

            if not counter%1000:
                print(self.cost()) ;
        
        
obj = fibonacii() ; 
obj.train() ; 