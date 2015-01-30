#!/usr/bin/python3.4

import os,re

def fileRead(fileName):
    '''
    line = '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>'
    (.*) helps in getting exactly the content required.
    group(0) gives 1, group(1) gives Michael
    '''
    regex = r'<.*?><td>(.*)</td><td>(.*)</td><td>(.*)</td>'
    matchObj = re.compile(regex, re.I)
    fd = open(os.getcwd() + '\\babynames\\' + fileName, mode='r')
    for line in fd:
        z = matchObj.match(line.strip('\n'))
        if z:
            yield (z.group(2) + ' ' + z.group(1), z.group(3) + ' ' + z.group(1))
    fd.close()
if __name__=='__main__':
    baby1990 = []
    for line in fileRead('baby1990.html'):
        baby1990.append(line[0])
        baby1990.append(line[1])
    print (baby1990)