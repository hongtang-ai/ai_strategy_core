from core.task_engine import TaskEngine
from core.strategy_engine import StrategyEngine

from registry.module_registry import ModuleRegistry

from modules.echo_module import EchoModule
from modules.calculator_module import CalculatorModule
from modules.time_module import TimeModule


def main():

    registry = ModuleRegistry()

    registry.register("echo", EchoModule())
    registry.register("calc", CalculatorModule())
    registry.register("time", TimeModule())

    strategy = StrategyEngine(registry)

    engine = TaskEngine(strategy, registry)

    tasks = [
        {"type": "echo", "message": "hello pipeline"},
        {"type": "calc", "a": 5, "b": 7},
        {"type": "time"}
    ]

    for task in tasks:
        result = engine.run(task)
        print("Result:", result)


if __name__ == "__main__":
    main()