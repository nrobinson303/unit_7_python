class Time:
    def __init__(self, hour, minute, seconds):
        self.hour = hour
        self.minute = minute
        self.second = seconds
        def __str__(self):
            return (f"(self.hour) : (self.minute) : (self.second) am" ) 


time_1 = Time(5, 32, 00)
time_2 = Time (23, 11, 11)
print(time_1)
print(time_2)