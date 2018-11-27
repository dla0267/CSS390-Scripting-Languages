import urllib2
import sys
import os.path
from time import sleep

interval = 10.0
outpath = 'data.txt'
for num, val in enumerate(sys.argv, start=1):
    if num == len(sys.argv):
        break
    print(str(num) +" " + val)
    if val == '--interval':
        print(num + 100000)
        print(len(sys.argv))
        interval = float(sys.argv[num])
        print(interval)

address = sys.argv[1] + '/stats'

print(address)
if os.path.isfile(outpath):
    results = open(outpath, 'a')
else:
    results = open(outpath, 'w')
while True:
    response = urllib2.urlopen(address)
    line = response.read().split("\n")
    del line[len(line) - 1]
    for stuff in line:
        digit = stuff.split(": ")
        results.write(digit[1] + "\t")  # grab the value, not the string saying what it is.
    results.write("\n")
    sleep(interval)
