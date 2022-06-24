import sys
import os
import subprocess
import time
import hashlib

if os.name == 'nt':
    import ctypes
 
    # https://docs.microsoft.com/en-us/windows/console/setconsolemode?redirectedfrom=MSDN
    ENABLE_PROCESSED_OUTPUT = 0x0001
    ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING
 
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    kernel32.SetConsoleMode(handle, MODE)
#Set Colour Variables
red="\033[31m"
blue="\033[34m"
cyan="\033[36m"
yellow="\033[33m"
green="\033[32m"
purple="\033[35m"
bold="\033[1m"
end="\033[0m"
nextline = "\n"
"""
OTAKU executer ver 1.1
"""
filepath = sys.argv[1]
if filepath == "-v":
    print(green+"Language:OTAKU"+"\n"+"Executer:OTAKU executer"+end)
    sys.exit()

if filepath == "--version":
    print(green+"Language:OTAKU"+"\n"+"Executer:OTAKU executer"+end)
    sys.exit()

f = open(filepath, 'r', encoding='UTF-8')
datalist = f.read()
OTAKU_check = '#OTAKU' in datalist
if OTAKU_check == True:
    print(green+'OTAKU:True'+end)
else:
    try:
        raise ValueError(red+"NO_STATEMENT_FOUND:There is no OTAKU DECLARATION. Maybe forgot"+green+"#OTAKU"+"?"+end)
    except ValueError as no_statement:
        print(no_statement)
        sys.exit()


f = open(filepath, 'r', encoding='UTF-8')
datalist = f.read()

len_check = "otaku:says" in datalist
if len_check == True:
    print(green+"Found function."+end)
else:
    try:
        raise ValueError(red+"NO_FUNCTION_FOUND:No function found to execute. Maybe forgot"+end+green+"otaku:says"+end+red+"?"+end)
    except ValueError as no_func:
        print(no_func)
        sys.exit()

datalist = datalist.replace("otaku:says", "print")
datalist = datalist.replace("*", "#")
datalist2 = datalist
datalist2 =datalist2.replace('print("',"")
datalist2 =datalist2.replace('")',"")
def_file = str(time.time())
def_file=hashlib.md5(def_file.encode()).hexdigest()
def_file = def_file+".otk"
q = open(def_file, 'w', encoding='UTF-8')
q.write(datalist2)
q.close()

datalist2 = open(def_file, 'r', encoding='UTF-8')
datalist_lines = datalist2.readlines()
print_ok = "print" in datalist2
for data in datalist2:
    if print_ok == True:
        data_len = data.len()
        if data_len < 100:
            try:
                raise ValueError(red+"TOO_SHORT:OTAKU spoke too little. Add more words.")
            except ValueError as too_short:
                print(too_short)
                quit()
datalist2.close()
os.remove(def_file)

py_file = str(time.time())
py_file=hashlib.md5(def_file.encode()).hexdigest()
py_file = def_file+".py"

p = open(py_file, 'w', encoding='UTF-8')
p.write(datalist)
p.close()

pro = "py "+py_file
subprocess.call(pro, shell=True)

os.remove(py_file)



