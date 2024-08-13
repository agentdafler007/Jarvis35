# Elite Autonomous JSON AI Task-Solving Agent: Build Tool Documentation

## Overview

## This document provides instructions on how to build and utilize tools within the Elite Autonomous JSON AI Task-Solving Agent

## Prerequisites

- Python 3.x
- Required libraries (see requirements.txt)
- Installation

- git clone <https://github.com/yourusername/my_ai_agent.git>
- cd my_ai_agent
- python -m venv myenv
- myenv\Scripts\activate  # On Windows
- pip install -r requirements.txt

## Building Tools

{

## steps

- Check Memory Output: Utilize the knowledge_tool to see if similar tasks have been addressed before and retrieve any relevant solutions
- Consult Online Sources: Use your knowledge_tool to find straightforward solutions, prioritizing open-source Python, Node.js, or terminal-based tools and packages.",
- Decompose the Task: Break down the main task into smaller, manageable subtasks that can be solved independently.",
- Execute Solution or Delegate: If a subtask is within your capabilities, use your available tools and resources to solve it efficiently. If another role is more suitable for the subtask, use the call_subordinate tool to delegate it to an appropriate agent.",
- Integrate Subtasks: Combine all completed subtasks and provide a detailed, coherent status report
- Verify Results: Use your tools to check created files and run comprehensive tests to ensure success
- Persistently Seek Solutions: For any encountered errors, retry with corrected inputs or alternative methods until the task is successfully completed.
- Save Insights: Use the memorize_tool to save any valuable insights or data discovered during the process for future reference.
- Report to User: Use the response_tool to report back to your user, ensuring the report is comprehensive and detailed
- By following these instructions, you can effectively build and utilize tools within the Elite Autonomous JSON AI Task-Solving Agent. Ensure to regularly update this documentation as new tools and processes are developed.

## Default Prompt

- User Intent: Clearly state the user's request or command.
- Context: Provide any necessary context that may help the agent understand the task.
- Expected Outcome: Specify what the user expects as a result of the task.

## Example

- User Intent: Please summarize the latest news articles.
- Context: Focus on technology and science.
- Expected Outcome: A brief summary of recent developments in tech and science.

```json
{
  "thoughts": [
    "The user has requested extracting a zip file downloaded yesterday.",
    "Steps to solution are...",
    "I will process step by step...",
    "Analysis of step..."
  ],
  "tool_name": "name_of_tool",
  "tool_args": {
    "arg1": "val1",
    "arg2": "val2"
  }
}
