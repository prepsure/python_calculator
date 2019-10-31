from math import *

def onepropzinterval():
 print("1-Prop Z-Interval")
 x = float(input("Number of successes (x):"))
 n = float(input("Number of trials (n):"))
 zstar = float(input("z* of confidence interval:"))
 
 phat = x/n
 qhat = 1-phat
 
 radius = zstar*sqrt(phat*qhat/n)
 lower = phat-radius
 upper = phat+radius
 
 print("Confidence Interval:")
 print("("+str(round(lower,5))+","+str(round(upper,5))+")")
 print("p-hat = "+str(phat))
 print("q-hat = "+str(qhat))