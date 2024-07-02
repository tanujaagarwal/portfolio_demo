import time
import tkinter as tk
from threading import Thread

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.clock_label = tk.Label(root, font=('times', 60, 'bold'), bg='white')
        self.clock_label.pack(fill='both', expand=1)
        self.alarm_label = tk.Label(root, font=('times', 35), bg='white')
        self.alarm_label.pack(fill='both', expand=1)
        self.stopwatch_label = tk.Label(root, font=('times', 35), bg='white')
        self.stopwatch_label.pack(fill='both', expand=1)
        self.alarm_time = ""
        self.stopwatch_running = False
        self.stopwatch_time = 0
        self.create_widgets()

    def create_widgets(self):
        self.alarm_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.alarm_button.pack(fill='x', expand=1)
        self.stopwatch_button = tk.Button(self.root, text="Start Stopwatch", command=self.start_stopwatch)
        self.stopwatch_button.pack(fill='x', expand=1)
        self.update_time()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        if self.alarm_time and current_time == self.alarm_time:
            self.alarm_label.config(text="ALARM!")
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        self.alarm_time = input("Enter alarm time (HH:MM:SS): ")
        self.alarm_label.config(text=f"Alarm set for {self.alarm_time}")

    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.stopwatch_thread = Thread(target=self.update_stopwatch)
            self.stopwatch_thread.start()
            self.stopwatch_button.config(text="Stop Stopwatch")
        else:
            self.stopwatch_running = False
            self.stopwatch_button.config(text="Start Stopwatch")

    def update_stopwatch(self):
        while self.stopwatch_running:
            time.sleep(1)
            self.stopwatch_time += 1
            self.stopwatch_label.config(text=f"Stopwatch: {self.stopwatch_time} seconds")

root = tk.Tk()
digital_clock = DigitalClock(root)
root.mainloop()