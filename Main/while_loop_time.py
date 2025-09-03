from datetime import datetime
import time
import os

os.makedirs("Main", exist_ok=True)

def task():
    with open("Main/time_log_while_loop.txt","a") as f:
        f.write(f"Script ran at: {datetime.now()}\n")
    print(f"Task ran at: {datetime.now()}")
    
while True:
    task()
    print("Sleeping for 2 seconds... ")
    time.sleep(2)