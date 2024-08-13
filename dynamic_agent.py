class DynamicAgent:
    def __init__(self, name):
        self.name = name
        self.experience = 0

    def evolve(self, task_complexity, outcome):
        # Adapt based on task complexity and outcome
        self.experience += task_complexity * outcome
        print(f"{self.name} evolved to experience level {self.experience}")

    def perform_task(self, task):
        # Perform task and adapt
        outcome = self.execute(task)
        self.evolve(task.complexity, outcome)

    def execute(self, task):
        # Execute the task and return outcome
        print(f"{self.name} is executing task: {task.description}")
        return 1  # Placeholder for task outcome