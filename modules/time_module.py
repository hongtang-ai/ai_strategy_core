from .base_module import BaseModule
import time

class TimeModule(BaseModule):

    def execute(self, task):
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print("Time:", now)
        return now