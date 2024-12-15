import re
import sys
import threading
import time
from datetime import datetime, timedelta
from playsound import playsound


def play_alarm():
    while not alarm_stopped.is_set():
        try:
            playsound("alarm.mp3")
        except Exception as e:
            print(f"Could Not Play the Alarm:: {e}")
            break
        time.sleep(0.1)


while True:
    now = datetime.now()
    print(f"\nCurrent Time Is: {now.strftime('%I:%M:%S %p')}")

    print("\nSelect Time Unit:")
    print("1. Seconds")
    print("2. Minutes")
    print("3. Hours")
    print("4. Days\n")

    try:
        unit_choice = int(input("Enter Choice (1-4): "))
        if unit_choice not in [1, 2, 3, 4]:
            raise ValueError

        meridiem = input("Enter AM or PM: ").upper()
        if meridiem not in ["AM", "PM"]:
            raise ValueError

        amount = int(input("Enter Amount To Add: "))
        if amount < 0:
            raise ValueError

        if unit_choice == 1:
            delta = timedelta(seconds=amount)
            unit_name = "seconds"
        elif unit_choice == 2:
            delta = timedelta(minutes=amount)
            unit_name = "minutes"
        elif unit_choice == 3:
            delta = timedelta(hours=amount)
            unit_name = "hours"
        else:
            delta = timedelta(days=amount)
            unit_name = "days"

    except ValueError:
        print("Please Enter Valid Positive Numbers and AM/PM")
        continue

    target_time = now + delta
    # Adjust target time based on AM/PM selection
    current_hour = target_time.hour
    if meridiem == "AM" and current_hour >= 12:
        target_time = target_time.replace(hour=current_hour - 12)
    elif meridiem == "PM" and current_hour < 12:
        target_time = target_time.replace(hour=current_hour + 12)

    print(
        f"\nAlarm Will Ring In {amount} {unit_name} At: {target_time.strftime('%I:%M:%S %p')}"
    )

    confirm = input("Is This Correct? (Y/N): ").upper()
    if confirm == "Y":
        break
    print("Let's Try Again...")

print(f"\nAlarm Set For {target_time.strftime('%I:%M:%S %p')}")

alarm_stopped = threading.Event()

while True:
    now = datetime.now()

    if now >= target_time:
        print("\nWake Up! (Press Enter to Stop the Alarm)")

        alarm_thread = threading.Thread(target=play_alarm)
        alarm_thread.daemon = True
        alarm_thread.start()

        try:
            input()
        finally:
            alarm_stopped.set()
            alarm_thread.join(timeout=1)
            break

    time.sleep(0.1)
