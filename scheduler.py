# design:
# Takes in a list of dates people CAN do
# randomly draws, assigns them duty

class Person():
        def __init__(self, filename):
            count = 0
            file = open(filename)
            self.dateslist = []

            # populating person
            for line in file:
                if count == 0:
                    self.name = line.rstrip()
                else:
                    self.dateslist.append(line.rstrip())
                count += 1

        def __str__(self):
            return self.name

class Scheduler():

    def __init__(self, dates):
        self.people = []
        datefile = open (dates)
        self.dates = []
        for line in datesfile:
            self.dates.append(line.rstrip())

    def add(self, filename):
        self.people.append(Person(filename))

def main():
    scheduler = Scheduler()
    scheduler.add('staff.txt')
    print scheduler.people[0]

main()