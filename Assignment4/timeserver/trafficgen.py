# import sys

# import time
# from time import sleep
# import random
# import urllib2

# url = sys.argv[1]
# rps = int(sys.argv[2])
# jitter = float(sys.argv[3])

# if jitter <

# minRate = rps * (1.0 - jitter) 
# maxRate = rps * (1.0 + jitter)

# actual_rate = randint(minRate, maxRate)

import sys
import time
from time import sleep
import random
import urllib2

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

if jitter < 0:
    jitter = 0.1
elif jitter > 1:
    jitter = 1.0

lower = int(rps * (1.0 - jitter))
upper = int(rps * (1.0 + jitter))
while True:
    actual = random.randint(lower, upper)
    start = time.time()
    for i in range(actual):
        chance = random.randint(0, 100)
        try:
            if chance in range(0, 6):
                urllib2.urlopen(url + '/arglebargle')
            elif chance in range(6, 11):
                urllib2.urlopen(url + '/fail')
            else:
                urllib2.urlopen(url)
        except urllib2.HTTPError:
            continue
    end = time.time()
    if(1-(end-start)) > 0:
        sleep(1-(end-start))
    else:
        continue