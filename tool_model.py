# models/tool_model.py

import subprocess
import logging

class ToolModel:
    def __init__(self, tool_name: str):
        self.tool_name = tool_name
        self.logger = self.setup_logger()

    def setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.tool_name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def execute_tool(self, command: str) -> str:
        self.logger.info(f"Executing command: {command}")
        try:
            # Execute the command using subprocess
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            self.logger.info(f"Command output: {result.stdout}")
            return result.stdout
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed with error: {e.stderr}")
            return f"Error executing {self.tool_name}: {e.stderr}"
        except Exception as e:
            self.logger.exception(f"Unexpected error: {e}")
            return f"Unexpected error executing {self.tool_name}: {e}"

    def validate_command(self, command: str) -> bool:
        # Add logic to validate the command before execution
        self.logger.debug(f"Validating command: {command}")
        # Example validation logic
        if not command:
            self.logger.warning("Empty command received.")
            return False
        # Additional validation checks can be added here
        return True

    def execute_with_validation(self, command: str) -> str:
        if not self.validate_command(command):
            return "Invalid command. Please provide a valid command."
        return self.execute_tool(command)

    def get_tool_info(self) -> str:
        # Return detailed information about the tool
        return f"ToolModel for {self.tool_name}: Capable of executing validated commands with logging and error handling."
