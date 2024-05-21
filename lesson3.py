

#Producer and consumers problems with the semaphore 


#Consider the case where we have two threads 

# One is producer and anoher one is consumer 

# Conside r a single buffer items :
# ---> Consumer can't consume an item until it has been produced

# --> producer can't place anoother item until consumer takes previous item.with

#Even if we used 10 items buffer it could eventually be filled 

# When it's full producer must wait .When it's empty consumer must wait also

# To actually solve this problem we can atcually use semaphore :

# There are two different types of semaphore----> 1.Binary 2.Counting

#Semmaphore operation:
# --> initialize(value)
#---> wait()
#-->signal()

#Semaphore in python  ...  

import threading 


initial_value=5


some_semaphore=threading.Semaphore(initial_value)

some_semaphore.acquire()
some_semaphore.release()


