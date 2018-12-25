import datetime

class Article:
    def __init__(self):
        self.number = 0
        self.title = ""
        self.name = ""
        self.date = datetime.datetime.now()

    def setData(self, number, title, date, name):
        self.number = number
        self.title  = title
        self.name = name

        if date.find(":") >= 0:
            t = date.split(":")
            self.date = datetime.datetime(self.date.year, self.date.month, self.date.day, int(t[0]), int(t[1]))
        else:
            t = date.split(".")
            self.date = datetime.datetime(int(t[0]), int(t[1]), int(t[2]), 0, 0)

    def toString(self):
        return "{0}\t{1}\t{2}\t{3}".format(self.number, self.title, self.name, self.date)