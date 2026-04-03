import os
import psutil
from datetime import datetime

try:
	while True:
		cpu_usage = psutil.cpu_percent(interval=1)
		memory_usage = psutil.virtual_memory().percent

		if cpu_usage > 80:
			with open("alerts.log", "a") as f:
				f.write(f"Warning! High CPU: {cpu_usage} at {datetime.now().strftime('%H:%M:%S')}\n")

		print(f"\rCPU: {cpu_usage}% | RAM: {memory_usage}%", end='', flush=True)
except KeyboardInterrupt:
	print("\nGood bye sir!")
