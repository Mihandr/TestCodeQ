"""
Нет проверки типов, ломается если create_handlers(2)
в lambda должно быть присвоение чтобы использовалась локальная, а не глобальная переменная
"""
from typeguard import typechecked

@typechecked
def create_handlers(callback: object) -> list:
    handlers = []
    for step in range(5):
        handlers.append(lambda step=step: callback(step))
    return handlers

@typechecked
def execute_handlers(handlers: list[object]) -> None:
    for handler in handlers:
        handler()

