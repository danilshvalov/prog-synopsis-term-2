SECONDS_IN_DAY = 24 * 3600


class Time:
    def __init__(self, hours=12, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __stringify_number(self, n):
        if n < 10:
            return "0" + str(n)
        return str(n)

    def as_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return ":".join(
            map(self.__stringify_number, [self.hours, self.minutes, self.seconds])
        )

    def __add__(self, other):
        seconds = (self.as_seconds() + other.as_seconds()) % SECONDS_IN_DAY
        return time_from_seconds(seconds)

    def print_time(self):
        print(self.__str__())


def time_from_seconds(seconds):
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 60
    return Time(hours, minutes, seconds)


t1 = Time(13, 30, 00)
t2 = Time(14, 15, 15)
t3 = Time()
t3 = t1 + t2
t3.print_time()  # 03:45:15
