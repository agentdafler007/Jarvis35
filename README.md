# My AI Agent

This project is a highly advanced AI agent designed to be a friend and assistant. It can handle complex tasks, delegate to specialized subordinates, and learn from interactions.

## Setup

Run the following command to set up the project:

```bash
./setup.sh
```

## Usage

To start the AI agent, run:

```bash
python main.py
```

## Folder Structure

my_ai_agent/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── master_agent.py
│   ├── subordinate_agent.py
│   ├── specialist_agents/
│       ├── __init__.py
│       ├── code_agent.py
│       ├── research_agent.py
│       ├── creative_agent.py
├── models/
│   ├── __init__.py
│   ├── language_model.py
│   ├── tool_model.py
│   ├── multimodal_model.py
├── workflows/
│   ├── __init__.py
│   ├── conversational_workflow.py
│   ├── task_execution_workflow.py
│   ├── agent_management_workflow.py
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   ├── config.py
│   ├── memory.py
│   ├── task_queue.py
│   ├── knowledge_base.py
├── api/
│   ├── __init__.py
│   ├── routes.py
│   ├── middleware.py
├── work/
│   └── # This folder will contain work-related files
├── tools/
│   └── # This folder will contain created tools
├── data/
│   ├── knowledge_base/
│   ├── models/
│   ├── logs/
├── main.py
├── requirements.txt
├── setup.sh
└── README.md
