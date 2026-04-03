import psutil
import shutil
import time
from datetime import datetime

def get_size(bytes):
	return f"{bytes / (1024**3):.2f} GB"

def monitor():
	print("\n--- Monitoring started. Enter Ctrl+C to quit ---\n")

	while True:
		now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		cpu = psutil.cpu_percent(interval=1)
		ram = psutil.virtual_memory().percent

		total, used, free = shutil.disk_usage("/")
		disk_info = get_size(free)
		free_gb = free / 1024**3

		status = f"CPU: {cpu}% | RAM: {ram}% | Disk free: {disk_info}"
		print(f"\r{status}", end='', flush=True)

		if cpu > 80 or ram > 90 or free_gb < 2:
			with open("alerts.log", "a") as f:
				f.write(f"ALERT! {status} - {now}\n")

		time.sleep(5)
try:
	monitor()
except KeyboardInterrupt:
	print("\nMonitoring has stopped!")
