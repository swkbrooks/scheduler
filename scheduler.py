# design:
# Takes in a list of dates people CAN do
# randomly draws, assigns them duty

class Scheduler():

    def __init__(self, folder_name):
        self.foler = folder_name

    class Person():

        def __init__(self, filename):
            count = 0
            file = open(filename)
            self.dateslist = []
            for line in file:
                if count == 0:
                    self.name = line
                else:
                    self.dateslist[count-1] = line
                count += 1
