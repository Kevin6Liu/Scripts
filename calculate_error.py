import subprocess
import os
import matplotlib

Number = 11 # Start number of Problem
while Number < 20:
    TEST_FILE = 'test_read.txt' # test file
    FILE = 'Errors' + str(Number) + '.txt'
    if os.path.exists(FILE):
        Error_code = set()
        # with open('Error' + str(Number) + '.txt') as f:
        with open(FILE) as f:
            contents = f.readlines()
            for line in contents:
                if line[0] == "e":
                    code = line.split()[0].strip()
                    # print(code)
                    num = []
                    for i in range(len(code)):
                        if code[i] == '_':
                            num.append(code[i+1:])
                            # print(f"Found an error! The number is {num}")

                    if len(num) != 0:
                        Error_code.update(num)
                    # print("Errors found:")
                    print(f"Total number of errors found : {len(Error_code)}")
                    print(f"Current unique errors found : {Error_code}")

        with open("Errors" + str(Number) + "_sum.txt", "w") as f:
                f.write("Total number of errors found : \n")
                f.write(str(len(Error_code)) + '\n')
                f.write("Error codes : \n")
                f.write(str(Error_code))
                print("Finished writing to file: Errors"  + str(Number) + "_sum.txt")
        f.close()
        Number += 1
    else:
        print(FILE + 'doesn\'t exist!')
        Number += 1
