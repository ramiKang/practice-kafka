import time
from collections import deque

class SlidingWindow:
    def __init__(self, window_size):
        self.window_size = window_size
        self.window = deque()

    def add_event(self, event):
        current_time = time.time()
        self.window.append((current_time, event))
        
        # 오래된 이벤트 제거
        while self.window and self.window[0][0] < current_time - self.window_size:
            self.window.popleft()

    def get_events(self):
        return [event for _, event in self.window]

    def get_count(self):
        return len(self.window)