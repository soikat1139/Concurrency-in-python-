


# Conditition object is another synchronization mechanism

# Condition object in python is similiar to the condition variable in python


# Even:: an event is a simple synchronization / communication mechanism that acts like a Flag 

# The flag is a Boolean value that can be either set or cleared 


# The flag value is stored inside an Even() object instances 

# The flag value can't be touched directly insted to interact with the flag there are several methods available


# Creating :


# import threading 

 #event_1=threading.Event()  # value initially set to False 


#Methods are :

 #   event_1.set()  # Set the value to true 

#    event1.clear() # set the value to False

 #   event_1.is_set() #returns the value

#    event_1.wait(timeout=None)  #Block while the value is False 



# The waiting variable will proceed as soon as the events value becomes True




import threading


event_go=threading.Event()


def player():
    event_go.wait()
    while True:
        #p1 game Loop  
        pass

def player2():
    event_go.wait()
    while True:
        pass



t1=threading.Thread(target=player)

t2=threading.Thread(target=player2)

t1.start()

t2.start()

# Set Up THe game this one set will start the  both player 


event_go.set()

while True:
    pass


t1.join()

t2.join()



#Another types of synchronization method is a Barriers 


# A bvarrier is a synchronization object that will wait until a number of threads reach the barrier 



# once the number is reached , all threads are unlocked simultaneously 


# Note that with Barriers :
  # No signal() or set() is required 
# All that matter is the number of waiting threads becomes greater than or equal to the barriers count

































































