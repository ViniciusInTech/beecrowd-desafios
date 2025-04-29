import sys


def calculate_delay(wake_time):
    hour, minute = map(int, wake_time.split(":"))

    if hour < 7:
        return 0
    elif hour == 7:
        return minute
    else:
        return (hour - 7) * 60 + minute


for line in sys.stdin:
    wake_time = line.strip()
    if wake_time:
        delay = calculate_delay(wake_time)
        print(f"Atraso maximo: {delay}")
