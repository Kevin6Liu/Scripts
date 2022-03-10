#! /usr/bin/python

import sys
import os
import subprocess
import datetime
# Problem number
Number = 14
# Lib
library = 'export LD_LIBRARY_PATH=/home/str/klee/build/lib/:$LD_LIBRARY_PATH'
# Output directory
directory = 'compiled/klee-out-4/'
# library = ["export","LD_LIBRARY_PATH=//home//str//klee//build//lib//:$LD_LIBRARY_PATH"]
# Change the number of the problem
Problem = 'clang-6.0 -I /home/str/klee/include -L /home/str/klee/build/lib Problem' + str(Number) + '.c -o Problem' + str(Number) + '.bc -lkleeRuntest'

#  os.system('export LD_LIBRARY_PATH=/home/str/klee/build/lib/:$LD_LIBRARY_PATH')
# subprocess.Popen(library,shell=True)
# subprocess.Popen(Problem,shell=True)
os.system(Problem)
start_time = datetime.datetime.now()
# Find .ktest files
file_list = [] 
for file in  os.listdir(directory):
    if file.endswith(".ktest"):
        file_list.append(file)

commands = []
for fname in file_list:
    commands.append('KTEST_FILE=' + directory + fname +' ./Problem' + str(Number) + '.bc')

for i in range(len(commands)):
    if i%1000 == 0: 
        end_time = datetime.datetime.now()
        print("time Lapsed: " + str((end_time - start_time).seconds/60) + "minutes")
    print("input command: ",commands[i])
    print("Finished: ", i, "Remaining: ", len(commands) - i, "Progress: %.3f" %(i*100/len(commands)),"%")
    command = commands[i]
    process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate(input=command,timeout=None)
    # print("Process out: ", out)
    # print("Process err: ", err)
    status,output = subprocess.getstatusoutput(command)  
    # print("Output: ", output)
    with open("Errors" + str(Number) + ".txt", "a") as f:
        f.write("\nInput: " + command + "\n")
        for line in output:
            line = line.strip('\r')
            # print("line:", line)
            f.write(line)

f.close()

end_time = datetime.datetime.now()
print("Finished, total time consumed: " + str((end_time - start_time).seconds/60) + "minutes")
# command = 'KTEST_FILE=compiled/klee-out-1/test000121.ktest ./Problem11.bc' 
# test_command = 'ls -l'




# r = os.popen(test_command) 
# r = os.popen(command) 
# print("data:",r.read())
# info = r.read() 
# print("info:",info)
# with open("Errors.txt", "w") as f:
#     for line in info:  
#         line = line.strip()
#         print ("line: ",line)
#         f.write(line)
# f.close()

# file_path = '/home/str/klee/Errors.txt'
# command = 'KTEST_FILE=compiled/klee-out-1/test000121.ktest ./Problem11.bc'
# split_command= ["KTEST_FILE=compiled/klee-out-1/test000121.ktest","./Problem11.bc"]
# command1 = 'export LD_LIBRARY_PATH=/home/str/klee/build/lib/:$LD_LIBRARY_PATH'
# # print(subprocess.check_output([command]))
# r = subprocess.Popen(split_command,stdout=subprocess.PIPE, stderr=None, shell=True)
# output = r.communicate()
# print("This is the output: ",output)

# info = r.readlines()
# print(info)
# with open("Errors.txt", "w") as f:
#     for line in info:
#         print("Output line:")
#         print(line)
#         f.write(line)

# f.close()


# sys.stdout = open(file_path, "a")
# print(r)

# info = r.readlines()
# f = open("Errors.txt","w")
# # with open("Errors.txt", "w") as f:
# for line in info:
#     line = line.strip('\r\n')
#     sys.stdout = open(file_path, "a")
    #print(line)
    #print("Output line")
        

# f.close()