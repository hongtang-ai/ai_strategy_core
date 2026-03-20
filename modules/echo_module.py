from .base_module import BaseModule

class EchoModule(BaseModule):

    def execute(self, task):
        message = task.get("message", "")
        print("Echo:", message)
        return message