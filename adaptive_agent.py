class AdaptiveAgent:
    def __init__(self, name):
        self.name = name
        self.role = "generalist"

    def adjust_role(self, task):
        # Adjust role based on task requirements
        if task.type == "research":
            self.role = "researcher"
        elif task.type == "development":
            self.role = "developer"
        print(f"{self.name} adjusted role to {self.role}")

    def perform_task(self, task):
        self.adjust_role(task)
        print(f"{self.name} is performing task as a {self.role}")