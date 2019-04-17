import csv


class User:
    def checkid(user):
        #username = str(user)
        #print(username)
        with open('Users.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == str(user):
                        print("This user is in system")
                        return True
                    else:
                        print('''You either typed your NetID, ''' + str(user) + ''' ,wrong or you are not in the system.
                              If this is your first time printing or you believe you are not in the system please email...'''
                              )
                        return False

