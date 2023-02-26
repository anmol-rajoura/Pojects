import random
import math


data = "0123456789"

otp= " "
for i in range(4):
    otp+=data[math.floor(random.random()*10)]
print("your otp is",otp)
 
 