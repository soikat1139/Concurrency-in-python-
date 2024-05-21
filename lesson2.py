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

#The acquire() method has  some parameters

#   some_lock.acquire(blocking=True ,timeout=-1)

#   blocking--> If set to false ,the call won't block . Even If the lock is unavailable 
#   When blocking is set to True a value os -1 causes indefinite waiting .Positive floating point values indicates a  number of seconds to wait ehilr Bloking 
#  this allows us to create code that doesn't wait indefinitely when trying to acquire a lock 


################## Another types of lock
 # Rlock objects are Re-entrant Locks .They work just like locks excepts:
    #-----> Allows the same thread to acquire the same lock mulltiple times 
    #------> Other threads will block on acquire()  but the same thread will not 
    #--->   The lock must be release the same number of times  it was acquired to return to being available state again 

# use cases : recursion -nested  calls that all must be executed while locking other threads until all have returned 












































