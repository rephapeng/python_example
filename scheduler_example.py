#scheduler every 5 seconds

import sched, time
s = sched.scheduler(time.time, time.sleep)
i = 0
def print_time(): print "From print_time", time.time()
def print_some_times():
    global i
    print time.time()
    print_time()
    i += 1
    print i
    if i==3:
        raise Exception("hae")
    s.enter(5, 1, print_some_times, ())

try :
    s.enter(5,1, print_some_times,())
    s.run()
except :
    print "error hae"
    i = 0
    s.enter(5,1, print_some_times,()) 
    s.run()
