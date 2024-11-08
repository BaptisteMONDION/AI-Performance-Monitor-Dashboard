import psutil
import subprocess

# Surveillance de l'utilisation du CPU
cpu_usage = psutil.cpu_percent(interval=1)
print(f"Usage CPU: {cpu_usage}%")

# Surveillance de l'utilisation du GPU (via nvidia-smi)
gpu_usage = subprocess.check_output(['nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'])
gpu_usage = gpu_usage.decode('utf-8').strip()
print(f"Usage GPU: {gpu_usage}%")
