


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



barrier_1=threading.Barrier(number_to_wait_upon)

#Optional parameters :
   #action = None # A function that can be called upon release 

   # timeout =None  # hOW LONG TO WAIT BEFORE GIVE UP

   barrier_1.wait()  # wait for the count to be met 

   barrier_1.abort()    # breaks barrier .All wait calls will fail with an exception BrokeBarrierError 
   barrier_1.broken    #Attribute that is true or false 

   barrier_1.parties  #Waiting thread count needed

   barrier_1.n_waiting   # Number of thread currently waiting

   barrier_1.reset() # Reset the barrier to the originnal state 



   # Barrier can be used to synchronize along a chain of events


   #Ensures all player players completed level 1  before proceeding to level 2 
   


   # Timer object in threading  :


 #  Timer object allow a thread to be activated only after a specified amount of timme has passed 

 #By default the function specified willl only be executed after interval seconds have passed 

  t1=threading.Timer(intervaI,function,args=None,kwargs=None)


  import threaading 


  def time_up():
      print("Time Up)




  timer1=threading.Timer(30,time_up)






































































































