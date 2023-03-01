import time
import psutil

#while True:
    #print(psutil.cpu_percent())
    #print(psutil.virtual_memory().percent)
    #time.sleep(1)

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_utilization = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_utilization * bars) + '-' * (bars - int(cpu_utilization * bars))
    mem_utilization = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_utilization * bars) + '-' * (bars - int(mem_utilization * bars))
    
    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ", end="\r")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)
