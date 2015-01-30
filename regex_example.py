#!/usr/bin/python3.4

import os,re

def fileRead(fileName):
    '''
    line = '<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>'
    (.*) helps in getting exactly the content required.
    group(0) gives 1, group(1) gives Michael
    '''
    regex = r'<.*?><td>(.*)</td><td>(.*)</td><td>(.*)</td>'
    regexYear = r'<.*?>\w+\s\w+\s([0-9]{4})<.*>'
    matchObj = re.compile(regex, re.I)
    yearObj = re.compile(regexYear, re.I)
    fd = open(os.getcwd() + '\\babynames\\' + fileName, mode='r')
    for line in fd:
        z = matchObj.match(line.strip('\n'))
        y = yearObj.match(line.strip('\n'))
        if z and (len(z.groups()) == 3):
            yield (z.group(2) + ' ' + z.group(1), z.group(3) + ' ' + z.group(1))
        elif y and (len(y.groups()) == 1):
            yield y.group(1)
    fd.close()
if __name__=='__main__':
    baby1990 = []
    for line in fileRead('baby1990.html'):
        if len(line) == 2:
            baby1990.append(line[0])
            baby1990.append(line[1])
        else:
            baby1990.append(line)
    print (baby1990)
