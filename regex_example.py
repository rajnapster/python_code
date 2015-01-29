#!/usr/bin/python3.4

'''
Regex trial
'''

import re, os

regex = '(?:^$)'
obj = re.compile(regex, re.I)

print (os.getcwd())

fd = open(r'chat_history.txt', mode='r', encoding='utf-8')
for (no, line) in enumerate(fd):
    if obj.match(line):
        continue
    print (line.strip('\n'))
fd.close()