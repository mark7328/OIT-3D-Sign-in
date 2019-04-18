import datetime
from src.NetID import Netid

class Record:
    def __init__(self):
        file = open('file.csv', 'a')
        Record.currenttime(file)

    def currenttime(file):
        current = datetime.datetime.now()
        file.write('\n' + str(current.strftime("%Y-%m-%d %H:%M")))
        current = current.minute
        Record.netid(file, current)

    def netid(file, current):
        state = False
        count = 1
        while state != True:
            if count == 1:
                user = input('Enter your netid: ')
            else:
                print('''You either typed your NetID, ''' + user + ''' ,wrong or you are not in the system.''')
                print('If this is your first time printing or you believe you are not in the system please email...')
                user = input('Enter your netid: ')
            state = Netid.checkin(user)
            count += 1
        file.write(', ' + user.lower())
        Record.left(file, current)

    def left(file, current):
        leave = False
        while leave == False:
            ans = (input('Are you ready to leave, yes or no?: '))
            ans = ans.lower()
            if ans == 'yes':
                leave = True
        left = datetime.datetime.now()
        file.write(', ' + str(left.strftime("%m/%d/%Y %H:%M")))
        left = left.minute
        Record.timeusage(file, current, left)

    def timeusage(file, current, left):
        timeusage = left - current
        file.write(', ' + str(timeusage))



