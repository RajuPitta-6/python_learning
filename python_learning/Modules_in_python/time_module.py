import time


# time.time() current time stamp (since jan 1 1970 (eooch time))
print(time.time())

# time.ctime() --> Human readlbe time
print(time.ctime())

# time.sleep(seconds) --> Delay program
print("start.....")
time.sleep(2)
print("Ends after 2 seconds")

# time.localtime() --> structed time
t = time.localtime()
print(t)

# time.strftime() --> format time
t = time.localtime()
print(time.strftime("%y-%m-%d %H:%M:%S", t))

# time.gmtime() --> UTC time
print(time.gmtime())

# performance measurement
start = time.time()
for i in range(100000):
    pass
end = time.time()
print("Excution time :", end - start)

# time.perf_counter() --> used for highly precision timing(better than time.time())
start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()
print("Accuurate delay time :", end - start)

# setting timer 
seconds = 10
while seconds > 0:
    print(f"Remaining time :{seconds}")
    time.sleep(1)
    seconds -= 1

# output :
'''
1759636433.4144228
Sun Oct  5 09:23:53 2025
start.....
Ends after 2 seconds
time.struct_time(tm_year=2025, tm_mon=10, tm_mday=5, tm_hour=9, tm_min=23, tm_sec=55, tm_wday=6, tm_yday=278, tm_isdst=0)
25-10-05 09:23:55
time.struct_time(tm_year=2025, tm_mon=10, tm_mday=5, tm_hour=3, tm_min=53, tm_sec=55, tm_wday=6, tm_yday=278, tm_isdst=0)
Excution time : 0.00832676887512207
Accuurate delay time : 1.000202199909836
Remaining time :10
Remaining time :9
Remaining time :8
Remaining time :7
Remaining time :6
Remaining time :5
Remaining time :4
Remaining time :3
Remaining time :2
Remaining time :1
'''
