
import multiprocessing
import subprocess

someGlobal=0

def myprocess():
    global someGlobal

    someGlobal+=1

    print("I am a child process")
    print(someGlobal)


if __name__ == "__main__":
    process_list=[]

    for i in range(10):
        p1=multiprocessing.Process(target=myprocess)

        process_list.append(p1)
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()

    print(someGlobal)
    print(multiprocessing.cpu_count())

    # For cpu bpound operation multiprocessing is a blessing 

    # multiprocessing make copmpletely new process which doesn't relaly depend on the main process 



