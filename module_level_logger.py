#!/usr/local/bin/python3.4

import re
import logging

'''
Module level logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(funcName)s '
                    '- %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
'''

formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s '
                              '- %(levelname)s - %(message)s')
lh = logging.StreamHandler()
lh.setLevel(logging.INFO)
lh.setFormatter(formatter)

fh = logging.FileHandler('/tmp/debug.log', mode='a')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

log = logging.getLogger(__name__)
log.addHandler(lh)
log.addHandler(fh)
log.setLevel(logging.DEBUG)


class myClass(object):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.log = logging.getLogger(__name__ + '.' + 'myClass')
    def my_function_1(self):
        self.log.debug('name: {0} surname: {1}'.format(self.name,
                                                       self.surname))
    def my_function_2(self):
        self.log.info(self.name)
        self.log.info(self.surname)

class myDriveStatus(object):
    def __init__(self):
        self.log = logging.getLogger(__name__ + '.' + 'myDriveStatus')
    def my_drive_status(self):
        regex = re.compile(r'\scurrent\s+: (ONLINE)')
        for line in open('drive_status', mode='r'):
            m = re.match(regex, line)
            if m:
                self.log.debug(line)
                return m.group(1)

def function_read_file(file_input):
    log.debug('entering: function')
    return [ line for line in open(file_input, mode='r') ]


if __name__ == '__main__':
    output = function_read_file('/etc/resolv.conf')
    log.info('this is raj singh')
    log.info('this command is not running')
    log.debug(output)
    myclass_obj1 = myClass('raj', 'singh')
    myclass_obj1.my_function_2()
    myclass_obj1.my_function_1()
    drive_object = myDriveStatus()
    output = drive_object.my_drive_status()
    log.info(output)
