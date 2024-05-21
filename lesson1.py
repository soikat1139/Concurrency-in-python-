#Python Concurrency lession

# https://www.youtube.com/watch?v=oc_St1mN-is&list=PLfYzdSbqf4Cb34O5SyLuzy8COfG86_IR1&index=3

#Youtube link for the lecture 


import threading


# General syntax thread1=threading.Thread(target=<function name> ,args=<tuple of arguments>)

# starting the thread in the main thread :  thread.start()

# Waiting for the thread to finish thread1.join()

NUM_PEOPLE=1000000
count=0

def enter_gate():
    global count
    for i in range(NUM_PEOPLE):
        count+=1

def exit_gate():
    global count
    
    for i in range(NUM_PEOPLE):
        print(count)
        count-=1


t1=threading.Thread(target=enter_gate)
t2=threading.Thread(target=exit_gate)


t1.start()
t2.start()


print("Threads are noe running")
print("Waiting for them to complete now ")


t1.join()

t2.join()

print("Thread running done")

print("The remaining people in the garden:",count)













