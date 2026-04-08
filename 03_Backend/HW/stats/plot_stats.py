import pandas as pd
import matplotlib.pyplot as plt
import re

def clean_mem(mem_str):
    match = re.search(r"([0-9.]+)(MiB|GiB|B|KB|MB|GB)", mem_str)
    if not match:
        return 0.0
    val, unit = match.groups()
    val = float(val)
    if unit == "GiB" or unit == "GB":
        return val * 1024
    if unit == "KB":
        return val / 1024
    if unit == "B":
        return val / (1024**2)
    return val

df = pd.read_csv("03_Backend\HW\stats\stats.csv")
df['cpu'] = df['cpu'].str.replace('%', '').astype(float)
df['mem_mib'] = df['mem'].apply(clean_mem)
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:red'
ax1.set_xlabel('Время (HH:MM:SS)')
ax1.set_ylabel('Загрузка CPU (%)', color=color)
ax1.plot(df['timestamp'], df['cpu'], color=color, label='CPU (%)', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Память (MiB)', color=color)
ax2.plot(df['timestamp'], df['mem_mib'], color=color, label='Memory (MiB)', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color)

plt.xticks(df['timestamp'][::max(1, len(df)//10)], rotation=45)

plt.title('Потребление ресурсов Inference Service (rubert-mini-frida)')
fig.tight_layout()
plt.show()