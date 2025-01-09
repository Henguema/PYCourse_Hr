class Staff:
    def __init__(self, fname, lname, position,  hourly_rate):
                self.fname = fname
                self.lname = lname
                self.position = position
                self.hourly_rate = hourly_rate

    def weekly_pay(self):
        return self.hourly_rate * 40