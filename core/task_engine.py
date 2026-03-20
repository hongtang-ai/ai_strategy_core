from core.pipeline_runner import PipelineRunner


class TaskEngine:

    def __init__(self, strategy_engine, registry):
        self.strategy_engine = strategy_engine
        self.registry = registry
        self.pipeline_runner = PipelineRunner(registry)

    def run(self, task):

        pipeline = self.strategy_engine.select_pipeline(task)

        context = task

        result = self.pipeline_runner.run(pipeline, context)

        return result