# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:03:58 2018

@author: thejakeman
"""
import functools
## taco bell app dealie
iteration = 0
tprice = 0
minprice = 0
tprice = float(input("input money you want to spend: "))

print("\n",tprice)

class menuitem(object):
    instances=[]
    test=[]
    def __init__(self, price, calories, ratio, name):
        self.price = price
        self.calories = calories
        self.ratio = ratio
        self.name = name
        menuitem.instances.append(self)
        menuitem.test.append(self)
        

        
softtaco = menuitem(1,150,.1,"soft taco")
beanburrito = menuitem(1.5,150,.5,"bean burrito")
nachos = menuitem(2,100,.05,"Nachos")
crunchwrap = menuitem(3,300,1,"crunchwrap")


bestvalue = max(menuitem.test, key=lambda x: x.ratio)
minprice = min(menuitem.test, key=lambda x: x.price)


while(tprice > 0, tprice >= minprice.price): 
    
    while bestvalue.price > tprice:
        menuitem.test.remove(bestvalue)
        bestvalue = max(menuitem.test, key=lambda x: x.ratio)
    if tprice >=bestvalue.price:
        print (bestvalue.name)
    tprice = (tprice - bestvalue.price)
    if tprice < minprice.price:
        break
        
            
        
print ("\n","bump for testing")
bestvalue = max(menuitem.test, key=lambda x: x.ratio)
print (bestvalue.name)

ultimate = max(menuitem.instances, key=lambda x: x.ratio)
print (ultimate.name, " ", ultimate.ratio)



    