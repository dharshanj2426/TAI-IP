import tkinter as tk
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, master, end_time):
        self.master = master
        self.end_time = end_time
        self.time_left = end_time - datetime.now()
        
        self.label = tk.Label(master, font=('Helvetica', 48), fg='red')
        self.label.pack()

        self.update_timer()

    def update_timer(self):
        self.time_left = self.end_time - datetime.now()
        
        if self.time_left > timedelta(0):
            self.label.config(text=str(self.time_left).split('.')[0])
            self.master.after(1000, self.update_timer)
        else:
            self.label.config(text="Time's up!")

def main():
    root = tk.Tk()
    root.title("Countdown Timer")

    end_time = datetime.now() + timedelta(minutes=1)  # Set the countdown time (e.g., 1 minute from now)
    countdown_timer = CountdownTimer(root, end_time)

    root.mainloop()

if __name__ == "__main__":
    main()
