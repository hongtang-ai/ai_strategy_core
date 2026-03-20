from .base_module import BaseModule

class CalculatorModule(BaseModule):

    def execute(self, task):

        a = task.get("a", 0)
        b = task.get("b", 0)

        result = a + b

        print("Calc:", result)

        return result