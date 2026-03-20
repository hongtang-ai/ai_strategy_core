class ModuleRegistry:
    """
    Store mapping task_type -> module
    """

    def __init__(self):
        self.modules = {}

    def register(self, task_type, module):
        self.modules[task_type] = module

    def get(self, task_type):
        return self.modules.get(task_type)