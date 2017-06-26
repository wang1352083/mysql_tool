#!/usr/bin/env python
import sys
base31=pow(2,31)
base32=pow(2,32)
base=0xFFFFFFFF
'''
mysql 中processlist和mysql.log中记录的 threadid不一致.因此做一个转换
from :processlist.threadid -> mysql.log.threadid
'''
def long_to_short(pid):
    if pid <base31:
        return pid
    elif base31 <= pid < base32:
        return pid -base32
    else :
        return pid & base
def usage(filename):
    print "please use "+filename+ " process_thread"
    print "\teg:"+filename+ " 12345"
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pid =int(sys.argv[1])
        print long_to_short(pid)
    else:
        usage(sys.argv[0])
