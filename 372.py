import sys


for line in sys.stdin:
    line = line.strip()
    if line:  
        max_zeros = max(len(s) for s in line.split("1"))
        print(max_zeros)