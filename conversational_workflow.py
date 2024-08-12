class ConversationalWorkflow:
    def __init__(self, language_model, memory, response_tool):
        self.language_model = language_model
        self.memory = memory
        self.response_tool = response_tool

    async def handle_conversation(self, user_input):
        # Retrieve context from memory
        context = self.memory.retrieve_context("conversation")
        # Generate response using the language model
        response = await self.language_model.process(user_input, context)
        # Store conversation context
        self.memory.store_context("conversation", user_input + " " + response)
        # Use response tool to deliver the response
        self.response_tool.send(response)
        return response