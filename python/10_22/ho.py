import random
from time import sleep
import time
import platform

# 30% "*" 
# 70% " "
# 20 karakter hosszan

while(True):
    for i in range(50):
        if random.random()<0.3:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    sleep(0.1)