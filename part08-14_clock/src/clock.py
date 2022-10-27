import datetime

class Clock:
    def __init__(self, hrs: int, min: int, sec: int):
        self.seconds = sec
        self.minutes = min
        self.hours = hrs
        
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
        if self.hours == 24:
            self.hours = 0
            
    def set(self, hrs: int, min: int):
        self.hours = hrs
        self.minutes = min
        self.seconds = 0
        
    
    def __str__(self):
        time = datetime.time(self.hours, self.minutes, self.seconds)
        return time.strftime("%H:%M:%S")
        


if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)