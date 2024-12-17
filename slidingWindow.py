import time
from collections import deque

class SlidingWindow:
    def __init__(self, window_size):
        self.window_size = window_size # window 사이즈 정의 (초 단위) => window_size 만큼의 범위 설정
        self.window = deque() # 이벤트를 저장할 deque (선입선출 구조)

    def add_event(self, event):
        current_time = time.time() # 현재 시간 (단위:초)
        self.window.append((current_time, event)) # (시간,이벤트) 형태로 저장 : timestamp 기반의 window sliding 구현
        
        # 오래된 이벤트 제거
        # window[0][0] : deque의 가장 맨 앞에 있는 데이터의 시간 : 가장 오래된 데이터의 저장 시간
        while self.window and self.window[0][0] < current_time - self.window_size:
            # 현재 시간 - 윈도우 사이즈(초)보다 작을 경우, 오래된 데이터 => deque에서 제거
            self.window.popleft()

    def get_events(self):
        # 현재 윈도우 범위 내의 아이템 확인
        return [event for _, event in self.window]

    def get_count(self):
        # 개수 확인
        return len(self.window)