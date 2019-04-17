import psutil
from src.record_data import Record


class Running:
    def __init__(self):
        #prg = 'C:\Program Files (x86)\Internet Explorer\iexplore.exe'
        while True:
            if "pycharm64.exe" in (p.name() for p in psutil.process_iter()):
                p = Record()
                break



p = Running()

