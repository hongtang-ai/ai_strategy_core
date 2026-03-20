class PipelineRunner:

    def __init__(self, registry):
        self.registry = registry

    def run(self, pipeline, context):

        result = None

        for module_name in pipeline:
            module = self.registry.get(module_name)

            if module is None:
                raise ValueError(f"Module not found: {module_name}")

            result = module.execute(context)

        return result