import os
import time

print "lets wait for 15 s"

time.sleep(15)
print "create new process"

pid = os.fork()

if pid == 0:
    # print "we are in child process"
    while True:
        time.sleep(2)
        print "my child process"
else:
    print "we are in parent process"
    print "child pid is %s" % (pid)
    while True:
        time.sleep(2)
        print "parent process"