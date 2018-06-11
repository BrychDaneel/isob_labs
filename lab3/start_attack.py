import subprocess
import time

for i in range(100):
    subprocess.Popen(["python3", "attack.py"])


time.sleep(60)
