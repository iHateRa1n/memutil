import os, subprocess, sys
x = open(open('.x', 'r').read()[:-1], 'r')
def y():
    for item in x.read().split('\n'):
        if 'write' in item:
            lol = 0
            os.system("./write write " + item.split()[1] + " " + item.split()[2])
        elif 'read' in item:
            lol = 1
            os.system("./write read " + item.split()[1])
y()
