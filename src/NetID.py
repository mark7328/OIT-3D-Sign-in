import csv

class Netid:
    def checkin(user):
        with open('Users.csv', 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == str(user):
                        print("This user is in system")
                        return True
                    return False
