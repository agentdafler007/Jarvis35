# agents/hybrid_agent.py

from agents.master_agent import MasterAgent

class HybridAgent(MasterAgent):
    def __init__(self, name, user_name, language_model_path, memory_path, tools_dir):
        super().__init__(name, user_name, language_model_path, memory_path, tools_dir)
        self.load_guidelines_from_markdown()

    def load_guidelines_from_markdown(self):
        # Load guidelines and values from markdown files
        try:
            with open('agent.system.md', 'r') as f:
                self.system_guidelines = f.read()
            with open('agent.memory.md', 'r') as f:
                self.memory_guidelines = f.read()
        except FileNotFoundError as e:
            print(f"Error loading guidelines: {e}")
            self.system_guidelines = ""
            self.memory_guidelines = ""

    async def interact(self, user_input: str) -> str:
        # Use guidelines to inform interaction
        context = await self.get_interaction_context()
        response = await self.language_model.generate(f"{context}\nUser: {user_input}\nAI:")
        await self.update_interaction(user_input, response)
        return response

    async def get_interaction_context(self) -> str:
        # Incorporate guidelines into the interaction context
        return f"{self.identity}\n{self.core_values}\n{self.system_guidelines}\n{self.memory_guidelines}"
