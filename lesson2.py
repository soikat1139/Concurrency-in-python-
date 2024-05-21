#Second lesson of concurrency 

#To actually guard the critical section area we have lock mechanism:

import threading


# To actualy get the lock we need to write the following lines of code 

my_lock=threading.Lock()

# Using of lock

# my_lock.acquire()
# some critical section which is accesed by multiple threads at atime 
# my_lock.release() 
## Other method of using lock is with keyword
# with my_locK:
#      #some critical section
#Lock will be released automatically in this case No need to maually release the lock 

#Other synchronization method which are suprerior this lock method :

#   rLOCKS
#  Semaphore 
# Barriers


