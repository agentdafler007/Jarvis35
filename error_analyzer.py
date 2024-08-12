class ErrorAnalyzer:
    def __init__(self, language_model):
        self.language_model = language_model

    async def analyze_error(self, error_message: str, context: str) -> str:
        prompt = f"Analyze the following error in the given context:\nError: {error_message}\nContext: {context}"
        return await self.language_model.process(prompt)

    async def suggest_fix(self, error_analysis: str) -> str:
        prompt = f"Suggest a fix for the following error analysis:\n{error_analysis}"
        return await self.language_model.process(prompt)

    async def analyze_update_failure(self, update_log: str) -> str:
        prompt = f"Analyze the following update failure log and identify the root cause:\n{update_log}"
        return await self.language_model.process(prompt)

    async def suggest_update_fix(self, failure_analysis: str) -> str:
        prompt = f"Suggest a fix for the following update failure analysis:\n{failure_analysis}"
        return await self.language_model.process(prompt)
