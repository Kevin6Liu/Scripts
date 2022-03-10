import subprocess
import os
import datetime
from threading import Timer
import time
import multiprocessing

number = 15
command = 'build/bin/klee compiled/Problem'
directory = 'compiled/'
file_list = [] 
TIMEOUT = 600 # seconds 600 is 10 minutes
Initial_time = datetime.datetime.now()



def run(number):
    start_time = datetime.datetime.now()
    print(f"Runing Problem {number+11} starts at {start_time}")
    os.system(command + str(number+11) + '.bc' )
    # os.system('ls -l compiled/klee-out-0')
    # time.sleep(30)
    # hello(number,start_time)



# def hello(number, start_time):
#     end_time = datetime.datetime.now()
#     os.system('clear')
#     total_time = (end_time-start_time)/60
#     print(f"Finished Problem {number}, starts at: {start_time}, laspsed: {total_time}")
#     print("*************************")
#     print("*************************")
#     print(f"    Problem {number}    ")
#     print("*************************")
#     print("*************************")
#     print("         Stopped!        ")
#     print("*************************")
#     print("*************************")
#     print("*************************")
#     time.sleep(10)


for file in  os.listdir(directory):
    if file.endswith(".bc"):
        file_list.append(file)
    file_list.sort()

for i in range(len(file_list)):
    if file_list[i] > 'Problem14.bc':
        if __name__ == '__main__':
            p = multiprocessing.Process(target = run, args=([i]),name = "process")
            p.start()
            p.join(TIMEOUT)

            if p.is_alive():
                print('function terminated')
                p.terminate
                # p.join()
                # run((i+11))
                start_time = datetime.datetime.now()
                print(f"Finished Problem {i}, starts at: {Initial_time}, laspsed: {}")





        # os.system('ls -l compiled/klee-out-0')


print("============================")
print("       All Finished!        ")
print("============================")