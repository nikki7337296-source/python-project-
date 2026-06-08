from datetime import datetime
import time
import winsound

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = datetime.now().strftime("%H:%M:%S")

    if current_time == alarm_time:
        print("Wake up! Alarm ringing...")
        winsound.Beep(1000, 1000)  # Frequency, Duration
        break

    time.sleep(1)