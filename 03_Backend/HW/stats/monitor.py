import subprocess
import time

CONTAINER_NAME = "my_app" 
LOG_FILE = "03_Backend\HW\stats\stats.csv"

with open(LOG_FILE, "w") as f:
    f.write("timestamp,cpu,mem\n")
    while True:
        try:
            res = subprocess.check_output(
                ["docker", "stats", CONTAINER_NAME, "--no-stream", "--format", "{{.CPUPerc}},{{.MemUsage}}"],
                stderr=subprocess.DEVNULL 
            ).decode("utf-8").strip()
            
            timestamp = time.strftime("%H:%M:%S")
            f.write(f"{timestamp},{res}\n")
            f.flush()
            print(f"[{timestamp}] Данные записываются...")
            
        except subprocess.CalledProcessError:
            print(f"Ожидаю запуск контейнера '{CONTAINER_NAME}'...")
            
        except KeyboardInterrupt:
            print("\nМониторинг остановлен.")
            break
        
        time.sleep(1)