import datetime

class Record:
    def Openfile(self):
        file = open('file.csv', 'a')
        Record.Currenttime(file)

    def Currenttime(file):
        current = datetime.datetime.now()
        file.write('\n' + str(current.strftime("%Y-%m-%d %H:%M")))
        current = current.minute
        Record.Netid(file, current)

    def Netid(file, current):
        user = input('Enter your netid: ')
        file.write(', ' + user)
        Record.Left(file, current)

    def Left(file, current):
        leave = False
        while leave == False:
            ans = (input('Are you ready to leave, yes or no?: '))
            if ans == 'yes':
                leave = True
        left = datetime.datetime.now()
        file.write(', ' + str(left.strftime("%m/%d/%Y %H:%M")))
        left = left.minute
        Record.Timeusage(file, current, left)

    def Timeusage(file, current, left):
        timeusage = left - current
        file.write(', ' + str(timeusage))

p = Record()
p.Openfile()