getcommand = ['lpstat', '-a'] #os command
# getcommand = ['wmic', 'printer', 'list', 'brief'] #window command
# data = subprocess.check_output(getcommand).decode('utf-8').split('\n')
# for line in data:
#     for printername in line.split(" "):
#         if printername!="":
#             print(printername)
# print(data)
# lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
# print(lpr)
import os
os.system("lpr -P myprint printMe.txt")