import psutil
import os
class Running:
    def search_process(self):
        while True:
            if "pycharm64.exe" in (p.name() for p in psutil.process_iter()):
                print('it works')
                os.startfile('C:\Program Files (x86)\Internet Explorer\iexplore.exe')
                break





p = Running()
p.search_process()