from datetime import datetime

class Timer:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration  # in minutes
        self.started_at = datetime.now()

    def __str__(self):
        return f"Timer '{self.name}' set for {self.duration} minutes (started at: {self.started_at.strftime('%H:%M:%S')})"

    def __repr__(self):
        return f"Timer(name='{self.name}', duration={self.duration})"

    def __del__(self):
        print(f"Goodbye Timer '{self.name}'")


t1 = Timer("Workout", 25)
t1.paused = False
print("Paused added:", hasattr(t1, 'paused'))
del t1.paused
print("Paused removed:", hasattr(t1, 'paused'))


timers = [
    Timer("Study", 40),
    Timer("Meditation", 5),
    Timer("Workout", 25)
]

print("Timers list:")
for timer in timers:
    print(timer)