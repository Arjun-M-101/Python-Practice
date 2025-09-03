from datetime import datetime

with open("Main/time_log.txt","a") as f:
    f.write(f"Script ran at: {datetime.now()}\n")