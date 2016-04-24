#!/usr/local/bin/python3.4

from subprocess import Popen, PIPE
import shlex
import logging

class MyFilter(logging.Filter):
    def filter(self, record):
        if record.msg.startswith('eth0'):
            return True


def run_linux_command(command_string):
    temp_cmd_string = shlex.split(command_string)
    cmd_object = Popen(temp_cmd_string, stdout=PIPE, stderr=PIPE)
    stdout, stderr = cmd_object.communicate()
    if len(stderr.decode()) != 0:
        return [ l for l in stderr.decode().split('\n') ]
    else:
        return [ l for l in stdout.decode().split('\n') ]


myfilter = MyFilter()
myformatter = logging.Formatter("MY HANDLER: %(name)s - %(message)s")
myhandler = logging.StreamHandler()
myhandler.setFormatter(myformatter)
log = logging.getLogger(__name__)
log.addHandler(myhandler)
log.addFilter(myfilter)
log.setLevel(logging.DEBUG)


if __name__ == '__main__':
    output = run_linux_command('ifconfig -a')
    for line in output:
        log.info(line)
