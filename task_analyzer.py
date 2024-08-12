class TaskAnalyzer:
    def __init__(self, language_model):
        self.language_model = language_model

    async def break_down_task(self, task_description: str) -> list:
        prompt = f"Break down the following task into detailed subtasks:\n{task_description}"
        response = await self.language_model.process(prompt)
        return response.split('\n')

    async def combine_results(self, results: list) -> str:
        prompt = f"Combine the following subtask results into a coherent final result:\n{' '.join(results)}"
        return await self.language_model.process(prompt)
