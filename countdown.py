import time


def cdown(hrs:int, mins:int, secs:int):
    global times_up
    times_up = False
    print("[TIMER STARTING ON THREAD TIMER]")
    time_in_secs = ((hrs*60) + mins)*60 + secs
    time_left = time_in_secs
    for i in range(time_in_secs):
        time.sleep(1)
        
        time_left = time_left - 1

    if time_left == 0:
        times_up = True



