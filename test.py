import csv

user = 'mc1757'
with open('Users.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for field in row:
            if field == user:
                    print("This user is in system")
            else:
                    print('''You either typed your NetID, ''' + user + ''' ,wrong or you are not in the system.
                                 If this is your first time printing or you believe you are not in the system please email...'''
                              )
