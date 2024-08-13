import abc

class BaseAgent(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def perform_task(self, *args, **kwargs):
        pass

    def log(self, message):
        print(f"[{self.name}] {message}")
