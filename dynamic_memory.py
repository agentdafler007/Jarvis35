class DynamicMemory:
    def __init__(self):
        self.memory = {}

    def store_context(self, context, data):
        # Store context-aware data
        self.memory[context] = data
        print(f"Stored data for context: {context}")

    def retrieve_context(self, context):
        # Retrieve data for a given context
        return self.memory.get(context, None)