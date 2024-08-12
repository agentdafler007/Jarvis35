class MultiAgentWorkflow:
    def __init__(self, agents):
        self.agents = agents

    def execute_collaborative_task(self, task):
        print(f"Executing collaborative task: {task.description}")
        for agent in self.agents:
            agent.perform_task(task)
        self.adapt_workflow()

    def adapt_workflow(self):
        # Adapt workflow based on agent performance
        print("Adapting multi-agent workflow...")