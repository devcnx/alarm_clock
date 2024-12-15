# Python Alarm Clock

A simple command-line alarm clock application that allows users to set alarms with customizable time intervals. It features real-time time display, audio notifications, and the ability to stop the alarm with a key press.

## Features

- Set alarms using different time units:
  - Seconds
  - Minutes
  - Hours
  - Days
- Real-time display of current time
- Audio alarm notification
- Simple command-line interface
- Ability to stop alarm with Enter key
- AM/PM time format support
- Confirmation prompt before setting alarm
- Continuous alarm sound until stopped

## Requirements

- Python 3.x
- playsound==1.2.2
- An audio file named "alarm.mp3" in the same directory

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install playsound==1.2.2
```

3. Create an audio file named "alarm.mp3" in the same directory as the script.

## Usage

Run the script:

```bash
python app.py
```

Follow the prompts to set alarms and control the alarm clock.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
