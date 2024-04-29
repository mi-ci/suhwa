import time 


start_time = time.time()

remaining = 20
while remaining > 0:
    print("{}초".format(int(remaining)))
    time.sleep(1)
    remaining = 20 - (time.time() - start_time)

