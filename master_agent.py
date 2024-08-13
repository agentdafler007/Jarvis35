import json
import asyncio
from typing import Dict
from agents.base_agent import BaseAgent
from models.language_model import LanguageModel
from agents.subordinate_agent import SubordinateAgent
from utils.task_analyzer import TaskAnalyzer
from utils.error_analyzer import ErrorAnalyzer

class MasterAgent(BaseAgent):
    def __init__(self, name: str, user_name: str, language_model_path: str, memory_path: str, tools_dir: str):
        super().__init__(name)
        self.user_name = user_name
        self.language_model = LanguageModel(language_model_path)
        self.subordinates: Dict[str, SubordinateAgent] = {}
        self.task_analyzer = TaskAnalyzer(self.language_model)
        self.error_analyzer = ErrorAnalyzer(self.language_model)
        self.decision_history = []

        # Initialize specialist agents
        self.specialist_agents = {
            'code': self.initialize_code_agent(),
            'research': self.initialize_research_agent(),
            'creative': self.initialize_creative_agent(),
            'photoshop': self.initialize_photoshop_agent()
        }

    def initialize_code_agent(self):
        from agents.specialist_agents.code_agent import CodeAgent
        return CodeAgent()

    def initialize_research_agent(self):
        from agents.specialist_agents.research_agent import ResearchAgent
        return ResearchAgent()

    def initialize_creative_agent(self):
        from agents.specialist_agents.creative_agent import CreativeAgent
        return CreativeAgent()

    def initialize_photoshop_agent(self):
        from agents.specialist_agents.photoshop_agent import PhotoshopAgent
        return PhotoshopAgent()

    async def handle_task(self, task_type: str, task_description: str):
        self.log(f"MasterAgent handling task: {task_type}")
        if task_type in self.specialist_agents:
            result = await self.specialist_agents[task_type].perform_task(task_description)
        elif task_type == 'guide':
            result = await self.language_model.load_markdown_guide(task_description)
        else:
            result = await self.language_model.process(task_description)
        return result

    async def interact(self, user_input: str) -> str:
        context = await self.language_model.load_markdown_guide("default_prompt")
        response = await self.language_model.process(user_input, context=context)
        await self.update_interaction(user_input, response)
        return response

    async def update_interaction(self, user_input: str, ai_response: str):
        # Update interaction history and friendship/respect levels
        self.decision_history.append((user_input, ai_response))

    async def make_decision(self, decision: str, importance: int) -> str:
        if importance > 7:
            return f"I think {decision}, but I'll defer to your judgment on this important matter, {self.user_name}."
        else:
            suggestion = f"I suggest {decision}. What do you think, {self.user_name}?"
            user_response = await self.get_user_input(suggestion)
            self.decision_history.append((decision, user_response))
            return f"Understood. We'll go with {'my suggestion' if 'yes' in user_response.lower() else 'your decision'}, {self.user_name}."

    async def get_user_input(self, prompt: str) -> str:
        # Simulate user input for demonstration purposes
        return input(f"{prompt} (yes/no): ")

    async def learn_from_interaction(self):
        # Analyze interactions and improve friendship/respect levels
        pass

    def log(self, message: str):
        """
        Log a message for debugging or monitoring purposes.
        """
        print(message)
