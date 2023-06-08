import time

def count_down(time_str):
    try:
        time_int = int(time_str)
        if time_int < 1:
            print("Warning: Set time is less than 1 minute.")
            return
        start_time = time.time()
        end_time = start_time + (time_int * 60)
        time_left = time_int * 60
        while time_left > 0:
            time_left = int(end_time - time.time())
            mins = time_left // 60
            secs = time_left % 60
            print("Time left: {:02d}:{:02d}".format(mins, secs), end="\r")
            if time_left <= (time_int * 60 * 0.2) and time_left > (time_int * 60 * 0.19):
                print("Warning: Less than 20% remaining.")
            time.sleep(1)
        print("Completed")
    except ValueError:
        print("Wrong input. Only integer data type is allowed.")

count_down('45') # example usage, countdown for 45 minutes
