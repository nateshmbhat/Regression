import pandas as pd ; 
import numpy as np ; 
from matplotlib import pyplot as plt ; 
import os , sys , subprocess , time  ; 

class fibonacci:

    def __init__(self):
        self.hypothesis = "log(y) = w1*x  + b"
        self.w1 =  np.random.uniform() ;
        self.w2 = np.random.uniform() ; 
        self.b = np.random.uniform() ; 
        self.data = np.genfromtxt('./data/exponential/fibonacciData' , delimiter=',' , dtype='int') ; 
        self.true_equation = "fib(n) = fib(n-1) + fib(n-2) " ; 
        self.features = self.data[2: , 0] ; 
        self.target = self.data[2: , 1]
        self.logtarget = np.log(self.target) ; 
        self.alpha = 0.00000324023423 ;
        self.__update_hyp__() ; 
    
    def __update_hyp__(self):
        self.hyp = self.get_hyp() ; 
        pass ;  

    def get_hyp(self):
        return self.w1*self.features + self.b ; 

    def choose_alpha(self , old_cost , old_params , new_cost):
        if(new_cost>=old_cost):
            self.w1  , self.b = old_params ; 
            self.alpha -= self.alpha*0.05 ;
        else:
            self.alpha += self.alpha*0.02 ; 
        
        
    def __main_event_loop__(self):
        dcost_dhyp = 0 ; 
        dhyp_dw1 = 0 ;
#         for row in range(self.features.shape[0]):
        dcost_dhyp = 2*(self.hyp - self.logtarget) ;
        dhyp_dw1 = self.features ;
#                 dhyp_dw2 = self.features[row] ; 

        self.w1 -= self.alpha *(dcost_dhyp * dhyp_dw1).mean() ;
#                 self.w2 -= self.alpha * dcost_dhyp * dhyp_dw2 ; 
        self.b -= self.alpha * dcost_dhyp.mean()  ; 

    
    def cost(self):
        return ((self.get_hyp()-self.logtarget)**2).mean() ; 
    
    def train(self):
        for counter in range(10000):
            
            self.__update_hyp__() ;

            old_cost = self.cost() ;             
            old_params = (self.w1 , self.b) ; 

            self.__main_event_loop__() ;
            
            new_cost = self.cost() ;

#             self.choose_alpha(old_cost , old_params , new_cost) ; 
             
            if not counter%300:
                print("(cost , alpha) = " , self.cost() , self.alpha ) ; 
                
    def show_params(self):
        print("(w1 , b ) = " , self.w1 , self.b) ; 
        
obj = fibonacci() ; 
obj.train() ; 