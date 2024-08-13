from .base_agent import BaseAgent
from models.language_model import LanguageModel

class SubordinateAgent(BaseAgent):
    def __init__(self, name: str, model_path: str, tools_dir: str, agent_type: str):
        super().__init__(name)
        self.model = LanguageModel(model_path)
        self.tools_dir = tools_dir
        self.agent_type = agent_type

    async def perform_task(self, task_description: str) -> str:
        self.log(f"Starting task: {task_description}")
        result = await self.model.process(task_description)
        self.log(f"Task result: {result}")
        return result

    async def specialize(self):
        if self.agent_type == "code":
            await self.model.fine_tune_for_coding()
        elif self.agent_type == "research":
            await self.model.fine_tune_for_research()
        elif self.agent_type == "creative":
            await self.model.fine_tune_for_creativity()
