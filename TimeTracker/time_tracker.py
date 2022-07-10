from threading import Thread
import time


class TimeTracker:
    seconds = 0
    is_running = False

    def __init__(self, update_time):
        self.update_time = update_time

    def start_tracker(self):
        self.seconds = 0
        self.is_running = True
        self.t = Thread(target=self.count_up, daemon=True)
        self.t.start()

    def count_up(self):
        while self.is_running:
            time.sleep(1)
            self.seconds += 1
            self.update_time()

    def stop_tracker(self):
        self.is_running = False

    def get_hours(self):
        return self.seconds/3600

    def get_seconds(self):
        return self.seconds
